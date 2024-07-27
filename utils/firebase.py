import firebase_admin
from firebase_admin import credentials, messaging

# Path to your service account key JSON file
cred = credentials.Certificate("E:\Website\Indigo Case Study\flight-status-app\serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def send_notification(token, title, body):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=token,
    )
    response = messaging.send(message)
    return response
