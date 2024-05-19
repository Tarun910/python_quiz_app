class QuizApp:
    def __init__(self):
        self.users = {}
        self.logged_in_user = None
        self.questions = {
            "What is the capital of France?": "Paris",
            "What is the largest mammal?": "Blue whale",
            "What is 2 + 2?": "4"
        }
        self.scores = {}

    def display_interface(self):
        print("Welcome to the Quiz App!")
        print("1. Home Page")
        print("2. Registration")
        print("3. Login")
        print("4. Attempt Quiz")
        print("5. Display Result")
        print("6. Logout")
        print("7. Help")
        print("8. Contact")
        print("9. Exit")

    def home_page(self):
        print("Welcome to the Home Page!")
        if self.logged_in_user:
            print(f"Logged in as: {self.logged_in_user}")

    def register(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        self.users[username] = password
        print("Registration successful!")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in self.users and self.users[username] == password:
            print("Login successful!")
            self.logged_in_user = username
        else:
            print("Invalid username or password.")

    def attempt_quiz(self):
        if not self.logged_in_user:
            print("Please log in first.")
            return

        score = 0
        for question, answer in self.questions.items():
            user_answer = input(question + " ")
            if user_answer.lower() == answer.lower():
                score += 1
        self.scores[self.logged_in_user] = score
        print("Quiz completed! Your score is:", score)

    def display_result(self):
        if not self.logged_in_user:
            print("Please log in first.")
            return

        if self.logged_in_user in self.scores:
            print(f"Your score is: {self.scores[self.logged_in_user]}")
        else:
            print("No score available.")

    def logout(self):
        self.logged_in_user = None
        print("Logged out successfully!")

    def help(self):
        print("This is the help section.")

    def contact(self):
        print("Contact us at example@example.com.")

    def run(self):
        while True:
            self.display_interface()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.home_page()
            elif choice == "2":
                self.register()
            elif choice == "3":
                self.login()
            elif choice == "4":
                self.attempt_quiz()
            elif choice == "5":
                self.display_result()
            elif choice == "6":
                self.logout()
            elif choice == "7":
                self.help()
            elif choice == "8":
                self.contact()
            elif choice == "9":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = QuizApp()
    app.run()
