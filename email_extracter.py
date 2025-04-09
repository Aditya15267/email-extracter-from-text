import re

def extract_emails(text):
    """
    Extracts email addresses from the given text.

    Args: text (str): The text to extract emails from.

    Returns: list: A list of extracted email addresses.
    """

    # Regular expression pattern for matching email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Find all matches in the text
    emails = re.findall(email_pattern, text)
    
    return emails

if __name__ == "__main__":
    text = input("Enter text to extract emails from:\n")
    
    emails = extract_emails(text)

    if emails:
        print("\nFound Emails:")
        for email in emails:
            print(f"- {email}")

        save = input("\nDo you want to save the emails to a file? (y/n): ").strip().lower()

        if save == 'y':
            with open("extracted_emails.txt", "w") as file:
                for email in emails:
                    file.write(email + "\n")
            print("Emails saved to extracted_emails.txt")
            
    else:
        print("No email addresses found.")