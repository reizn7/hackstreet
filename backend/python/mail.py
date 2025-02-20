import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email credentials
SENDER_EMAIL = "contactme.piyush@gmail.com"  # Replace with your email
APP_PASSWORD = "khao zpfb nyoc ljlo"  # Replace with your app password

def send_mail(html_content):
    """
    Sends an HTML email with the specified subject and content.

    Args:
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        html_content (str): The HTML content to include in the email body.
    """
    try:
        recipient_email = "contactme.piyush@gmail.com"  # Replace with recipient email
        subject = "Minutes of Meeting (MoM)"

        # Configure the email message
        msg = MIMEMultipart("alternative")
        msg["From"] = SENDER_EMAIL
        msg["To"] = recipient_email
        msg["Subject"] = subject

        # Attach the HTML content
        msg.attach(MIMEText(html_content, "html"))

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
            print(f"Email sent successfully to {recipient_email}!")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")


# Example Usage
if __name__ == "__main__":
    # Replace with your dynamic HTML content generated by Gemini
    generated_html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
            }
            h1 {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                text-align: center;
                border-radius: 8px;
            }
            .section-title {
                color: #4CAF50;
                margin-top: 20px;
                font-size: 18px;
                text-decoration: underline;
            }
            .content {
                margin-left: 20px;
            }
            .footer {
                margin-top: 20px;
                font-size: 12px;
                color: #555;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h1>Minutes of Meeting (MoM)</h1>
        <p><strong>Date:</strong> February 20, 2025</p>
        <p><strong>Time:</strong> 2:00 PM - 3:30 PM</p>
        <p><strong>Meeting Title:</strong> Project Collaboration and Real-Time Translation Bot Discussion</p>
        <p><strong>Participants:</strong></p>
        <ul>
            <li>Alex Johnson (Team Lead)</li>
            <li>Priya Sharma (AI/ML Developer)</li>
            <li>David Thompson (Backend Developer)</li>
            <li>Sara Williams (Frontend Developer)</li>
            <li>Maria Garcia (QA Analyst)</li>
        </ul>
        <div class="footer">
            <p>Generated automatically by the Real-Time Translation Bot system.</p>
        </div>
    </body>
    </html>
    """
    
    # Send email
    send_mail(generated_html_content)
