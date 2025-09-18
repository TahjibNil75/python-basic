import json
import smtplib

class UserRepository:
    """Handles User data persistence"""

    def __init__(self, filePath="user.json"):
        self.filePath = filePath

    def saveUser(self, users):
        with open(self.filePath, "w") as f:
            json.dump(users, f)


class EmailNotification:
    """Handles sending email notifications"""

    def __init__(self, smtp_server="smtp.example.com", port=587):
        self.smtp_server = smtp_server
        self.port = port

    def sendEmail(self, to_email, subject, body):
        server = smtplib.SMTP(self.smtp_server, self.port)
        server.starttls()
        server.login("admin@gmail.com", "passsword")
        email_message = f"Subject: {subject}\n\n\{body}"
        server.sendmail("admin@gmail.com", to_email,email_message)
        server.quit()

class UserService:
    """Handles user-related operations"""

    def __init__(self, repisorory: UserRepository, notifier: EmailNotification):

        self.users = {}  # pretend database {email: password}
        self.repository = repisorory
        self.notifier = notifier

    def registerUser(self,email,password):
        if email in self.users:
            print(f"Refistrayion failed !! User with {email} already existed")
            return
        if "@" not in email or "." not in email:
            print("Registration failed !! Invalid email")
            return
        if len(password) < 5:
            print("Registration failed !! password must 6 character long")
            return
        self.users[email] = password
        self.repository.saveUser(self.users)
        self.notifier.sendEmail(email, "Welcome!", "Thank you for registering.")
        print(f"User with {email} created")


## Usage:
repo = UserRepository()
notifier = EmailNotification()
user_service = UserService(repo, notifier)
user_service.registerUser("tahjib@gmail.com", "ghjklp")