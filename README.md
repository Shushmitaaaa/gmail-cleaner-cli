# Gmail Cleaner CLI

A command-line tool to declutter your Gmail inbox by deleting or summarizing emails based on filters like promotions, spam, unread status, sender, and age, powered by AI summaries with Gemini.

## Features

- Filter-based Cleanup: Delete or summarize emails by categories such as promotions, spam, unread, or from specific senders.
- Customizable Time Filters: Target emails older than a specified duration (e.g., 6 months, 1 year).
- Summarization with Gemini AI: Get concise summaries of emails before deletion.
- Trash Management: Empty Gmail trash with a single command.
- OAuth 2.0 secure authentication with Google API.

## Prerequisites

- Python 3.6 or higher
- A Google Cloud project with Gmail API enabled
- OAuth 2.0 credentials (client ID and secret)
- Gemini API key for summarization

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Shushmitaaaa/gmail-cleaner-cli.git
   cd gmail-cleaner-cli
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:

   * Create a `.env_vars` file in the project root.
   * Add your Gmail API credentials and Gemini API key:

     ```
     GMAIL_CLIENT_ID=your-client-id
     GMAIL_CLIENT_SECRET=your-client-secret
     GEMINI_API_KEY=your-gemini-api-key
     ```

## Usage

### Authenticate and Authorize

The first time you run any command that accesses Gmail, the tool will open a browser window to authorize with Google OAuth. It saves a token locally for future use.

If you change scopes or face permission errors, delete the `token.pickle` file in the project directory to re-trigger authorization.

### Commands

- Delete all spam emails:

```bash
gmailcleaner clean --spam --delete
```

This command deletes all promotional emails

```bash
gmailcleaner clean --promotions --delete
```

Summarize unread promotional emails without deleting:

```bash
gmailcleaner clean --promotions --summarize
```

### Empty Trash

To empty your Gmail trash:

```bash
gmailcleaner empty-trash
```

### Filters

You can combine flags like:

- `--unread` to target unread emails
- `--sender` to target emails from specific senders (e.g., `--sender linkedin.com`)
- `--older-than` to target emails older than a given period (e.g., `--older-than 6m`)

## Important Notes

- Gmail scopes used are "restricted" by Google due to sensitive access.
- Add your Gmail testing accounts as "Test Users" in your Google Cloud project for OAuth consent.
- Always review summaries before deleting to avoid accidental loss.
- Deleted emails cannot be recovered.
- Ensure your `.env_vars` file contains correct API keys and credentials.
- If you face permission errors, remove stored tokens and reauthenticate.


Feel free to use, share, and contribute! Suggestions welcome.


