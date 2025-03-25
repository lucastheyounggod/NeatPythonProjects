import getpass

class Student:
    def __init__(self, name, student_id, gpa, password, security_questions):
        self.name = name
        self.__student_id = student_id
        self.__gpa = gpa
        self.__password = password
        self.security_questions = security_questions
        self.failed_attempts = 0
        self.account_locked = False

    def authenticate(self):
        """Verify password before updating GPA."""
        if self.account_locked:
            print("Account is locked due to multiple incorrect attempts.")
            return False

        password_attempt = getpass.getpass(f"Enter password for {self.name}: ")
        if password_attempt == self.__password:
            self.failed_attempts = 0
            return True
        else:
            self.failed_attempts += 1
            print("Incorrect password!")

            if self.failed_attempts >= 3:
                self.account_locked = True
                print("Too many incorrect attempts! Account is now locked.")

        return False

    def unlock_account(self):
        """Allow the user to unlock their account via security questions."""
        if not self.account_locked:
            print("Account is not locked.")
            return

        print(f"To unlock {self.name}'s account, answer the security questions.")
        for question, answer in self.security_questions.items():
            user_answer = input(question + " ")
            if user_answer.lower() != answer.lower():
                print("Incorrect answer. Cannot unlock the account.")
                return

        self.failed_attempts = 0
        self.account_locked = False
        print(f"{self.name}'s account has been unlocked!")

    @property
    def student_id(self):
        """Getter for student ID (read-only)."""
        return self.__student_id

    @property
    def gpa(self):
        """Getter for GPA."""
        return self.__gpa

    @gpa.setter
    def gpa(self, new_gpa):
        """Setter for GPA with validation."""
        if self.authenticate():
            if 0.0 <= new_gpa <= 4.0:
                self.__gpa = new_gpa
                print(f"{self.name}'s GPA updated to {self.__gpa}")
            else:
                print("Invalid GPA! Must be between 0.0 and 4.0.")
        else:
            print("Authentication failed. GPA update denied.")

    def display_student_info(self):
        """Display student details."""
        print(f"Student: {self.name}, ID: {self.__student_id}, GPA: {self.__gpa}")

class Admin:
    def __init__(self, admin_password):
        self.__admin_password = admin_password

    def authenticate_admin(self):
        """Admin authentication."""
        password_attempt = getpass.getpass("Enter admin password: ")
        return password_attempt == self.__admin_password

    def view_student_records(self, students):
        """Allow the admin to view student records."""
        if self.authenticate_admin():
            print("\n--- Student Records ---")
            for student in students:
                student.display_student_info()
        else:
            print("Incorrect admin password!")

# Create Students with security questions
student1 = Student("Alice", "S1001", 3.5, "alicepass", {"What is your pet's name?": "Fluffy", "What is your favorite color?": "Blue"})
student2 = Student("Bob", "S1002", 3.8, "bobpass", {"What is your birth city?": "Lagos", "What is your favorite sport?": "Soccer"})

# Create an Admin
admin = Admin("admin123")

# List of Students
students = [student1, student2]

# Simulate Login and Actions
student1.display_student_info()

# Try updating GPA (with password authentication)
student1.gpa = 3.9

# Failed login attempts (locks account)
student1.authenticate()
student1.authenticate()
student1.authenticate()

# Unlock account using security questions
student1.unlock_account()

# Admin views student records
admin.view_student_records(students)