import pandas as pd
import datetime
import smtplib
import os
from getpass import getpass

# Get current working directory
current_path = os.getcwd()
print(f"Current working directory: {current_path}")
os.chdir(current_path)

# Getting credentials securely
GMAIL_ID = input("Enter your email: ")
GMAIL_PSWD = getpass("Enter password for your email (password will not be displayed): ")

def send_email(to, subject, message):
    """Sends an email with the specified subject and message."""
    try:
        print(f"Email to {to} sent: \nSubject: {subject}, \nMessage: {message}")
        # Creating the server to send mail
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            # Start a TLS session
            server.starttls()
            # Login with Gmail credentials
            server.login(GMAIL_ID, GMAIL_PSWD)
            # Sending the email
            server.sendmail(GMAIL_ID, to, f"Subject: {subject}\n\n{message}")
    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Check your email or password.")
    except Exception as e:
        print(f"Error sending email to {to}: {e}")

def load_data(file_path):
    """Loads the data from the Excel file and handles potential errors."""
    try:
        return pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Please check the file path.")
        return None
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return None

def update_birthday_status(df, write_indices, year_now):
    """Updates the LastWishedYear column after sending birthday wishes."""
    for index in write_indices:
        old_year = df.loc[index, 'LastWishedYear']
        df.loc[index, 'LastWishedYear'] = f"{old_year}, {year_now}"
    try:
        df.to_excel('data.xlsx', index=False)
        print("Data successfully updated in 'data.xlsx'")
    except Exception as e:
        print(f"Error saving data to 'data.xlsx': {e}")

def main():
    # Load the data from the Excel file
    df = load_data("data.xlsx")
    if df is None:
        return

    today = datetime.datetime.now().strftime("%d-%m")
    year_now = datetime.datetime.now().strftime("%Y")
    
    write_indices = []

    # Iterate through each friend and check if it's their birthday
    for index, item in df.iterrows():
        try:
            bday = item['Birthday']
            bday = datetime.datetime.strptime(bday, "%dd-%mm-%YY")
            bday = bday.strftime("%d-%m")

            if today == bday and year_now not in str(item['LastWishedYear']):
                # Send the birthday email
                send_email(item['Email'], "Happy Birthday", item['Dialogue'])
                write_indices.append(index)

        except Exception as e:
            print(f"Error processing birthday for {item['Email']}: {e}")

    # If there were any birthdays, update the Excel file with the new year
    if write_indices:
        update_birthday_status(df, write_indices, year_now)
    else:
        print("No birthdays today.")

if __name__ == "__main__":
    main()
