from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
import pickle

# Define the Gmail API scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def authenticate_gmail():
    """Authenticate the user and return the Gmail API service."""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def search_messages(service, query):
    """Search for messages in Gmail using a query."""
    results = service.users().messages().list(userId='me', q=query).execute()
    return results.get('messages', [])

def get_message_body(service, message_id):
    """Retrieve the body of a message."""
    message = service.users().messages().get(userId='me', id=message_id, format='full').execute()
    for part in message['payload'].get('parts', []):
        if part['mimeType'] == 'text/plain':
            return part['body']['data']
    return ""

def move_to_trash(service, message_id):
    """Move a message to the trash."""
    service.users().messages().trash(userId='me', id=message_id).execute()

def clean_inbox():
    """Main function to clean the inbox."""
    service = authenticate_gmail()
    
    # Search for emails that do NOT contain "guhan" in the body
    query = 'Pinterest'  # Search for emails without "guhan" in the body
    messages = search_messages(service, query)
    
    if not messages:
        print("No unnecessary emails found!")
        return

    print(f"Found {len(messages)} emails to move to trash.")
    for message in messages:
        move_to_trash(service, message['id'])
        print(f"Moved email with ID {message['id']} to trash.")

if __name__ == '__main__':
    clean_inbox()

