from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import pickle
import os

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/gmail.labels',
    'https://mail.google.com/'        
     ]

def gmail_authenticate():
    creds = None

    
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentialss.json', SCOPES)
            creds = flow.run_local_server(port=0)

        
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    
    service = build('gmail', 'v1', credentials=creds)

   
    results = service.users().getProfile(userId='me').execute()
    print(f"Logged in as: {results['emailAddress']}")

    return service 

if __name__ == '__main__':
    gmail_authenticate()
