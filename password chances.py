class PasswordManager:
    def __init__(self, correct_password, max_attempts):
        self.correct_password = correct_password
        self.max_attempts = max_attempts

    def validate_password(self):
        for attempt in range(1, self.max_attempts + 1):
            entered_password = input(f"Attempt {attempt}/{self.max_attempts} - Enter your password: ")

            if entered_password == self.correct_password:
                print("Access granted.")
                return
            else:
                print("Incorrect password.")

        print("Account is invalid.")

if __name__ == "__main__":
    manager = PasswordManager(correct_password="mypassword", max_attempts=3)
    manager.validate_password()
