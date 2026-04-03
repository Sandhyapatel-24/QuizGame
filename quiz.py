import random
import time

class QuizGame:

    def __init__(self):
        self.questions = {"easy": [], "medium": [], "hard": []}
        self.score = 0

    def load_questions(self):
        try:
            with open("questions.txt", "r") as file:
                for line in file:
                    parts = line.strip().split("|")
                    if len(parts) == 3:
                        level, q, a = parts
                        self.questions[level].append((q, a))
        except:
            print("Error loading questions!")

    def choose_level(self):
        print("\nSelect Level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        choice = input("Enter: ")
        return {"1": "easy", "2": "medium", "3": "hard"}.get(choice, None)

    def ask_questions(self, level):
        q_list = self.questions[level]
        random.shuffle(q_list)

        self.score = 0

        print(f"\n----- {level.upper()} QUIZ STARTED -----")
        print("Type 'hint' for help or 'exit' to quit\n")

        for i, (q, a) in enumerate(q_list, 1):
            print(f"Q{i}: {q}")

            start = time.time()
            user = input("Answer: ")

            # EXIT
            if user.lower() == "exit":
                print("Exiting quiz...")
                return

            # HINT
            if user.lower() == "hint":
                print(f"💡 Hint: Answer starts with '{a[0]}'")
                user = input("Try again: ")

            end = time.time()

            if end - start > 15:
                print("⏰ Time's up!\n")
                continue

            if user.lower() == a.lower():
                print("✅ Correct!\n")
                self.score += 1
            else:
                print(f"❌ Wrong! Correct Answer: {a}\n")

    def show_result(self, total):
        percentage = (self.score / total) * 100

        print("\n========== RESULT ==========")
        print(f"Score: {self.score}/{total}")
        print(f"Percentage: {percentage:.2f}%")

        # Rank System
        if percentage >= 90:
            print("🏆 Rank: Expert")
        elif percentage >= 70:
            print("🥈 Rank: Intermediate")
        else:
            print("🥉 Rank: Beginner")

        print("📊 Performance Analysis Complete!")

        # Save score
        with open("highscore.txt", "a") as f:
            f.write(f"{percentage:.2f}%\n")

    def show_high_scores(self):
        print("\n===== HIGH SCORES =====")
        try:
            with open("highscore.txt", "r") as file:
                scores = file.readlines()

                if scores:
                    print("Last 5 Scores:")
                    for s in scores[-5:]:
                        print(s.strip())
                else:
                    print("No scores yet!")
        except:
            print("No high score file found.")

    def start(self):
        self.load_questions()

        while True:
            print("\n========== QUIZ GAME ==========")
            print("1. Start Quiz")
            print("2. View High Scores")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                level = self.choose_level()

                if level and self.questions[level]:
                    self.ask_questions(level)
                    self.show_result(len(self.questions[level]))
                else:
                    print("Invalid level or no questions!")

            elif choice == "2":
                self.show_high_scores()

            elif choice == "3":
                print("Thank you for playing! 👋")
                break

            else:
                print("Invalid choice! Try again.")


# Run game
game = QuizGame()
game.start()