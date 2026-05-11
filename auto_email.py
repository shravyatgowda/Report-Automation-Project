import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Report.configs.user_pwrd import EMAIL_USER, EMAIL_PASSWORD

def send_email(recipient, subject, body):
    """
    Sends an email using Gmail's SMTP server.

    Parameters:
    - recipient (str): Email address of the recipient.
    - subject (str): Subject line of the email.
    - body (str): Body content of the email.
    """
    print("Preparing to send email...")
    print(f"To      : {recipient}")
    print(f"Subject : {subject}")
    print("Body    :")
    print(body)

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail SMTP server and send email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)
        print("✅ Email sent successfully.")
    except Exception as e:
        print(f" Failed to send email: {e}")
