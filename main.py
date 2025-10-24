import os
import click
from gmail_cleaner.auth import gmail_authenticate
from gmail_cleaner.cleaner import delete_emails
from gmail_cleaner.summarizer import summarize_emails
from dotenv import load_dotenv
from google import genai

load_dotenv(".env_vars")  # specify the filename
gemini_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=gemini_api_key)

@click.group()
def cli():
    """Gmail Smart Cleaner CLI"""
    pass


@cli.command()
@click.option('--older-than', help="Delete or summarize emails older than (e.g., 6m, 1y)")
@click.option('--promotions', is_flag=True, help="Target promotional emails")
@click.option('--spam', is_flag=True, help="Target spam emails")
@click.option('--unread', is_flag=True, help="Target unread emails")
@click.option('--sender', help="Target emails from a specific sender (e.g. 'linkedin.com')")
@click.option('--summarize', is_flag=True, help="Summarize emails before action")
@click.option('--delete', is_flag=True, help="Delete the selected emails")
@click.option('--archive', is_flag=True, help="Archive the selected emails instead of deleting")
def clean(older_than, promotions, spam, unread, sender, summarize, delete, archive):
    """Clean or summarize emails based on filters"""

    service = gmail_authenticate()
    query_parts = []

    # Build Gmail search query dynamically
    if promotions:
        query_parts.append("category:promotions")
    if spam:
        query_parts.append("category:spam")
    if unread:
        query_parts.append("is:unread")
    if sender:
        query_parts.append(f"from:{sender}")
    if older_than:
        query_parts.append(f"older_than:{older_than}")

    query = " ".join(query_parts)
    if not query:
        click.echo("No filters specified. Please use flags like --promotions or --older-than.")
        return

    click.echo(f"\n🔍 Searching for emails matching: {query}\n")

    if summarize:
        summarize_emails(service, query,client)

    if delete:
        delete_emails(service, query)
    elif archive:
        click.echo(" Archiving emails feature coming soon...")
    else:
        click.echo("Summary complete (no delete/archive action performed).")


@cli.command()
def empty_trash():
    """Empty Gmail trash"""
    service = gmail_authenticate()
    service.users().messages().emptyTrash(userId='me').execute()
    print("Trash emptied successfully!")


if __name__ == '__main__':
    cli()
