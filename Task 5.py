# Design a User Authentication System:
# Implement a User class where users can register with a username and password, users can log in and check if their credentials are correct, use encapsulation to ensure passwords are not exposed directly.

# _protected_variable is a convention (not enforced, but should be respected).
# __private_variable makes it truly private using name mangling.
# We can also have private methods that cannot be accessed directly


class User():
    def __init__(self, username: str, password: str):
        self.username = username
        self.__password = password
    
    def check_password(self, user_inptd_pass):
        return self.__password == user_inptd_pass # Encapsulation (data hiding)
    

class AuthenticationSystem():
    def __init__(self):
        self.users = {} # Need to store usernames AND passwords 

    def register_new_user(self, username: str, password: str):
        if username in self.users:
            return f"This user is not unique."
        else:
            self.users[username] = User(username, password)
            return f"User {username} registered successfully."
        
    def logging_in(self, username: str, password: str):
        # Note that the .get() function gets the values for the key we want to get
        user = self.users.get(username)
        if user.check_password(password) and user: #making sure that both the password AND username are valid
            return f"Both username and password are correct."
        return f"Invalid username/password."
    

auth_system = AuthenticationSystem()
print(auth_system.register_new_user("john_doe", "mypassword")) 
print(auth_system.logging_in("john_doe", "mypassword"))
print(auth_system.logging_in("john_doe", "wrongpassword"))  
print(auth_system.register_new_user("john_doe", "newpassword"))  