def delete_emails(service, query):
    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])
    count = 0

    if not messages:
        print("No matching emails found.")
        return

    for msg in messages:
        try:
            service.users().messages().delete(userId='me', id=msg['id']).execute()
            count += 1
        except Exception as e:
            print(f"Error deleting message {msg['id']}: {e}")

    print(f"Deleted {count} emails matching query: '{query}'")
