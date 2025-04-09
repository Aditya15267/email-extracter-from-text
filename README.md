# Email Extracter

A simple command-line tool that extracts all the email addresses from a block of text using regular expressions.

## Features

- Extract all email addresses from any text input
- Uses regex pattern matching
- Option to save extracted emails to `extracted_emails.txt`
- Pure Python - no dependencies

## How to use

1. Clone the repository:
    ```bash
    git clone https://github.com/Aditya15267/email-extracter-from-text.git
2. Run the script:
    ```bash
    python email_extracter.py
    ```

## Example

```bash
Contact us at hello@site.com or admin@domain.org

Found Emails:
- hello@site.com
- admin@domain.org

Do you want to save the emails to a file? (y/n): y
Emails saved to extracted_emails.txt
```

## Tech Stack

- Python 3
- Regular Expressions (`re`)