# Required libraries.
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Twilio credentials.
account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)

# Send a WhatsApp message.
def send_whatsapp_msg(recepient_number, message_body):
    try:
        message = client.messages.create(
            from_ = '+14155238886',
            body = message_body,
            to = f'{recepient_number}'
        )
        print(f"Message sent successfully: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")

# User details.
name = input("Enter your name: ")
recepient_number = input("Enter the recepient's WhatsApp number (with country code): ")
message_body = input("Enter the message you want to send: ")

# Parse time and date.
date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM, 24-hour format): ")

# datetime.
schedule_datetime = datetime.strptime(f'{date_str} {time_str}',"%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# Calculate delay.
total_diff = schedule_datetime - current_datetime
delay = total_diff.total_seconds()

if delay <= 0:
    print("The scheduled time is in the past. Please enter a future date and time.")
else:
    print(f"Message scheduled to be sent in {delay} seconds.")
    time.sleep(delay)
    send_whatsapp_msg(recepient_number, f"Hello {name},\n\n{message_body}")
    print("Message sent successfully!")