class User:
    def __init__(self, username, password):  # Fixed __init__ method
        self._username = username
        self.__password = password  # Private attribute with double underscores

    def get_username(self):
        return self._username

    def set_password(self, new_password):
        self.__password = new_password
        print("Password updated successfully!")

    def login(self, username, password):
        # Correctly accessing attributes
        return self._username == username and self.__password == password

# Creating a User object
user = User("Sravi", "12345678")

# Input for login
username = input("Enter username: ")
password = input("Enter password: ")

if user.login(username, password):
    print(f"Welcome, {user.get_username()}!")
else:
    print("Invalid login details.")
    option = input("Do you want to reset your password? (yes/no): ").lower()
    if option == "yes":
        new_password = input("Enter your new password: ")
        user.set_password(new_password)
    else:
        print("Goodbye!")
