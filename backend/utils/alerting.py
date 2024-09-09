from twilio.rest import Client

def send_alert(message, phone_number):
    account_sid = 'your_twilio_account_sid'
    auth_token = 'your_twilio_auth_token'
    
    client = Client(account_sid, auth_token)
    
    client.messages.create(
        body=message,
        from_='+1234567890',  # Twilio phone number
        to=phone_number
    )
