```markdown
# Property Finder Data Fetcher

This script retrieves property data from the Property Finder API, processes it, and sends out email reports.
It includes error handling and notifications for success and failure.

## Requirements
- Python 3.x
- Required Python packages: requests, pandas, smtplib

## Environment Variables
Ensure the following environment variables are set:
- `email_pw`: Office 365 email password
- `pf_token`: Token for accessing the Property Finder API

## Usage
1. Install the required Python packages using `pip install requests pandas`.
2. Set the necessary environment variables.
3. Run the script using `python script_name.py`.

## Script Structure

### Modules and Libraries
- `requests`: Library for making HTTP requests.
- `pandas`: Library for data manipulation and analysis.
- `smtplib`: Library for sending email messages.
- `email.mime`: MIME (Multipurpose Internet Mail Extensions) library for handling email-related functionality.
- `os`: Module providing a way of using operating system-dependent functionality.

### Script Functions
1. **sendSuccessEmail(dataframe)**: Sends an email notification with property data attached as an Excel file.
2. **sendUnsuccessEmail()**: Sends an email notification for unsuccessful operations.
3. **Main Script**: Fetches property data from the Property Finder API, processes it,
and sends out email reports based on success or failure.

## Running the Script
1. Clone the repository or download the script.
2. Navigate to the script directory.
3. Set the required environment variables.
4. Open a terminal or command prompt.
5. Run the script using `python script_name.py`.

## Author
- Aathil Ahamed
  - LinkedIn: [aathilks](https://www.linkedin.com/in/aathilks/)
  - Email: atldeae@gmail.com

```
