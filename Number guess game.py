import random, time

class NGGame:
    def __init__(self):
        print()
        print("Welcome to the number guessing game!")
        print("Im thinking of a number between 1 and 100")
        print()
        self.start_time = time.perf_counter()
        self.total_time = 0
        self.attempts = 0
        self.number = random.randint(1, 100)
        self.chances = 0
        self.guess = 0
        self.difficulty = self.diff_selection()
        self.chances_know()
        self.wanna_more = ""
        self.guess_handle()

    def diff_selection(self):
        print("Choose difficulty: ")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")

        self.difficulty = input("Enter your choice: ")
        print()
        while self.difficulty != "1" and self.difficulty != "2" and self.difficulty != "3":
            print("Choose difficulty level correctly(1,2,3): ")
            self.difficulty = input("Enter your choice: ")
            print()

        if self.difficulty == "1":
            diff_word = "Easy"
        elif self.difficulty == "2":
            diff_word = "Medium"
        else:
            diff_word = "Hard"
        print(f"Great! You choose difficulty!({diff_word})")
        print("Let's start the game!")
        print()
        return self.difficulty

    def chances_know(self):
        if self.difficulty == "1":
            self.chances = 10
        elif self.difficulty == "2":
            self.chances = 5
        elif self.difficulty == "3":
            self.chances = 3

    def guess_handle(self):
        while self.chances > 0:
            while True:
                try:
                    self.guess = int(input("Enter your guess: "))
                    break
                except ValueError:
                    print("Enter the number!")
            if self.guess != self.number:
                if self.guess < self.number:
                    print(f"Incorrect! number is greater than {self.guess}")
                    self.attempts += 1
                    print()
                elif self.guess > self.number:
                    print(f"Incorrect! number is less than {self.guess}")
                    self.attempts += 1
                    print()
            else:
                self.win()
                break
            self.chances -= 1
            if self.chances == 0:
                self.lose()
                break

    def win(self):
        self.total_time = time.perf_counter() - self.start_time
        print(f"Great! you guessed the number in {self.attempts + 1} attempts and {self.total_time:.2f} seconds!")
        self.wanna_more = input("Wanna play more?(Y/N): ").strip().upper()


    def lose(self):
        self.total_time = time.perf_counter() - self.start_time
        print("Chances are over, you  lose :(")
        self.wanna_more = input("Wanna play more?(Y/N): ").strip().upper()

while True:
    game = NGGame()
    if game.wanna_more != "Y":
        break

