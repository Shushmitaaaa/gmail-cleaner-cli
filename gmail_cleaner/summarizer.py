import os
from googleapiclient.errors import HttpError
#from main import client

def summarize_emails(service, query,client, max_results=10):
    """Fetch emails and summarize using Gemini"""
    try:
        results = service.users().messages().list(userId='me', q=query, maxResults=max_results).execute()
        messages = results.get('messages', [])
        if not messages:
            print("No emails found for summarizing.")
            return

        print(f"Found {len(messages)} emails to summarize:\n")
        for msg in messages:
            msg_data = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
            headers = msg_data.get("payload", {}).get("headers", [])
            subject = next((h["value"] for h in headers if h["name"] == "Subject"), "(No Subject)")
            sender = next((h["value"] for h in headers if h["name"] == "From"), "(Unknown sender)")

            # Extract plain-text body
            body = ""
            parts = msg_data.get("payload", {}).get("parts", [])
            if parts:
                for part in parts:
                    if part.get("mimeType") == "text/plain":
                        import base64
                        data = part.get("body", {}).get("data", "")
                        body = base64.urlsafe_b64decode(data).decode("utf-8")
                        break

            # Gemini summarization
            if body:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=f"Summarize this email in 2-3 sentences:\n\n{body}"
                )
                summary = response.text
            else:
                summary = "(No body to summarize)"

            print(f"Subject: {subject}\nFrom: {sender}\nSummary: {summary}\n{'-'*50}")

    except HttpError as error:
        print(f"An error occurred: {error}")
