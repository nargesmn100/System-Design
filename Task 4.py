# Create a Notification System:
# Design a notification system with email notification, SMS notifications, push notifications. Use abstraction and inheritance to avoid code duplication.

from abc import ABC, abstractmethod
# Since every notification type must implement send_notification(), it's better to use abstraction via Python’s ABC (Abstract Base Class).

class Notifications(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def send_notification(self):
        pass # This forces child classes to implement this method


class Email(Notifications):
    def __init__(self, address: str, name: str):
        super().__init__(name) # Notifications expects a name argument
        self.address = address
    
    def send_notification(self):
        return f"This is a notification for your {self.address} account."
    

class SMS(Notifications):
    def __init__(self, phone_num: str, name: str):
        super().__init__(name)
        self.phone_num = phone_num

    def send_notification(self):
        return f"This is a notification for your {self.phone_num} number."
    

class PushNotifications(Notifications):
    def __init__(self, push_id: str, name: str):
        super().__init__(name)
        self.push_id = push_id

    def send_notification(self):
        return f"Your push notification id is {self.push_id}."


email = Email("narges.nezhad@gmail.ca", "Narges")
print(email.send_notification())
esms = SMS("1002003000", "Narges")
print(esms.send_notification())
push_alert = PushNotifications("1029384756", "Narges")
print(push_alert.send_notification())