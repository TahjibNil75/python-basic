

from abc import ABC, abstractmethod

# Implement Only What’s Needed

class EmailNotification(ABC):
    @abstractmethod
    def sendEmail(self, to, subject, body):
        print(f"Sending email to {to} with subject '{subject}  and body '{body}'")

class SMSNotification(ABC):
    @abstractmethod
    def sendSMS(self, phone_number, message):
        print(f"Sending SMS to {phone_number} with message '{message}'")

class PushNotification(ABC):
    @abstractmethod
    def sendPush(self, device_id, message):
        print(f"Sending Push Notification to {device_id} with message '{message}'")



class UserNotifierOne(EmailNotification, SMSNotification):
    def sendEmail(self, to, subject, body):
        print(f"Sending email to {to} with subject '{subject}' and body '{body}'")

    def sendSMS(self, phone_number, message):
        print(f"Sending SMS to {phone_number} with message '{message}'")


class UserNotifierTwo(EmailNotification, PushNotification):
    def sendEmail(self, to, subject, body):
        print(f"Sending email to {to} with subject '{subject}' and body '{body}'")

    def sendPush(self, device_id, message):
        print(f"Sending Push Notification to {device_id} with message '{message}'")

# Usage
notifier1 = UserNotifierOne()
notifier1.sendEmail("john@example.com", "Welcome!", "Thanks for signing up.")
notifier1.sendSMS("+1234567890", "Your code is 1234.")

notifier2 = UserNotifierTwo()
notifier2.sendEmail("alice@example.com", "Account Update", "Your profile has been updated.")
notifier2.sendPush("device123", "You have a new message.")