# Birthday Email Reminder Script

This Python script sends birthday wishes via email to your friends based on the data stored in an Excel file. It reads a list of friends' birthdays and sends them a personalized birthday email on their special day. It keeps track of when you last wished each friend and ensures that you don't send duplicate emails in the same year.

## Features

- **Automated Birthday Wishes**: Sends automated birthday emails on the day of your friend's birthday.
- **Personalized Messages**: Sends personalized messages for each friend, customizable via the `Dialogue` column in the Excel file.
- **Tracking Last Sent Year**: Keeps track of the last year you sent a birthday wish to prevent duplicate emails.
- **Email Security**: Uses `getpass` for password input to prevent the password from being displayed.
- **Error Handling**: Catches common errors related to email sending and file handling.
- **File Handling**: Saves updates to the Excel file after sending birthday wishes.

## Requirements

- Python 3.x
- `pandas` library for handling Excel data
- `openpyxl` for reading and writing Excel files (can be installed along with pandas)
- A Gmail account for sending emails

### Installation

1. **Install Python**: Ensure Python 3.x is installed on your machine. If not, download and install it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**:
   You can install the required libraries using `pip`:
   ```bash
   pip install pandas openpyxl
   ```

### Setting Up Your Excel File

Create an Excel file (e.g., `data.xlsx`) with the following columns:

| Name      | Birthday   | Email              | Dialogue               | LastWishedYear |
|-----------|------------|--------------------|------------------------|----------------|
| John Doe  | 10d-10m-1990 | johndoe@example.com | Happy Birthday John!    | 2022           |
| Jane Doe  | 25d-12m-1992 | janedoe@example.com | Wishing you a wonderful day! | 2021         |

- **Birthday**: The friend's birthdate in `dd-mm-yyyy` format.
- **Email**: The friend's email address.
- **Dialogue**: The birthday message you want to send.
- **LastWishedYear**: A comma-separated list of years when the birthday wish was last sent.

### Usage

1. **Clone or Download the Script**: Download or clone the repository containing the script.

2. **Configure Your Email**:
   - Enter your Gmail credentials when prompted. The script uses SMTP to send emails through Gmail's servers.

3. **Run the Script**:
   - Open a terminal or command prompt and run the script:
     ```bash
     python birthday_email.py
     ```

4. **The script will check for today's birthdays** and send emails accordingly:
   - The script will automatically send emails to any friends who have their birthday on the current day and who haven't already received a birthday wish this year.

5. **Updating the Excel file**:
   - After sending the email, the script will update the `LastWishedYear` column with the current year and save the changes back to the Excel file.

### Example

```bash
Enter your email: youremail@gmail.com
Enter password for your email (password will not be displayed): ********
```

If today is John's birthday (10th October), the script will send an email with the message "Happy Birthday John!" to `johndoe@example.com`.

### Code Overview

The script consists of the following key parts:

- **`send_email(to, subject, message)`**: This function sends an email to the specified recipient with the provided subject and message. It uses Gmail's SMTP server and requires login credentials.
- **`load_data(file_path)`**: Loads the data from the Excel file. If the file is missing or there is an error loading it, the script will terminate gracefully.
- **`update_birthday_status(df, write_indices, year_now)`**: Updates the `LastWishedYear` column for friends whose birthdays were processed today and saves the changes back to the Excel file.
- **`main()`**: The main function that orchestrates the logic, including reading the data, checking for birthdays, and sending emails.

### Error Handling

The script includes error handling for:

- **File Not Found**: If the `data.xlsx` file is missing or can't be accessed.
- **Email Sending Failures**: Handles login issues and SMTP errors.
- **Invalid Data**: Catches issues in the data format (e.g., wrong date format).

### Security Considerations

- The script uses `getpass` to securely enter your Gmail password without displaying it in the terminal.
- **Important**: This script uses plain-text Gmail credentials, so it's recommended to set up an App Password if you're using 2-Step Verification with Gmail.

### Future Enhancements

- **Secure Email Storage**: Storing email and password securely, such as using environment variables or configuration files.
- **Email Templates**: Allowing HTML email templates for richer birthday messages.
- **Task Scheduling**: Automating the script to run daily using cron jobs or Windows Task Scheduler.

## License

This script is released under the MIT License.
