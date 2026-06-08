# Create a working Python version of Articulate with slight changes
# The program should ask for the number of users and tracks the number of correct answers of each player
# Question Types: Person, World, Object, Action, Nature, Random (May ignore)
# The winner is decided by who has the highest score after 5 turns

import time


class Player:

    def __init__(self, name):
        self._score = 0
        self._name = name

    def add_score(self, n):
        self._score += n

    def return_score(self):
        return self._score

    def return_name(self):
        return self._name

    def change_name(self, name):
        self._name = name
        return "Name changed."


class Trivia:

    def __init__(self):
        self.parameters = 0
        self._solo_mode = False
        self._categories = ['P', 'W', 'O', 'A', 'N']
        self._category_score = {'P': 0, 'W': 0, 'O': 0, 'A': 0, 'N': 0}
        self._player_no = 0
        self._players = []
        self._round = 1
        self._round_max = 5
        self._category = ''
        self._hints = {}
        self._turn_time = 30

    def set_max_rounds(self, n):
        self._round_max = n

    def return_max_rounds(self):
        return f"Total number of rounds: {self._round_max}"

    def set_turn_time(self, n):
        self._turn_time = n

    def return_turn_time(self):
        return f"Time for a player's turn: {self._turn_time} seconds"

    def intro(self):
        print(
            "Welcome! I hope you are ready to play my variant of the hit-game Articulate!")
        print("This is a game where one player is given a word and the other player needs to guess it.")
        print("Normally, the player given the word would need to describe it as well as possible.")
        print("But, for our game, I will give a single clue which you will have to use to guess the word!")
        print("Sounds more difficult, right?")
        print("\nDon't worry, on the plus side, you have unlimited skips.")
        print("Try your best to succeed!")

    def invalid_value(self):
        print("This value is invalid. Please try again.")

    def start(self):
        # Start
        want_full_intro = input(
            "\nPlease enter 1 if you want full instructions on how to play the game or enter 0 to start: ")
        want_full_intro = int(want_full_intro)

    # Full Instructions
    def full_intro(self):
        print("...")

    # Game Start
    def number_of_players(self):
        self._player_no = int(input("Enter number of player playing: "))
        if self._player_no == 1:
            self._solo_mode = True

    def load_data(self):
        self._hints = {'P': {"British Prime Minister from 1940-1945 and again from 1951-1955, most famous for successfully leading Britain out of World War II": 1,
                             "Famous Hero in Greek Mythology, killed the monstrous Lernaean Hydra and ascended Mount Olympus": 2,
                             "Orange Tabby cat who loves to eat lasagna": 3,
                             "Wife of arguably the dumbest man in Springfields, iconic for her sky-high beehive blue hair": 4,
                             "Famous disney character raised in the rainforest by apes": 5
                             },
                       'W': {"America's largest manufacturer of ketchup, with an overall market share of more than 50%; founded in Pittsburgh": 1,
                             "Capital of the Czech Republic; Surrounded by Germany, Poland, Slovakia and Austria; known for Charles Bridge, one of the largest castles in the world": 2,
                             "Iron lattice tower landmark in Paris, France; 1000ft tall, most visited paid monument in the world": 3
                             },
                       'O': {"Musical instrument with black and white keys": 1,
                             "Small shelter for sleeping when camping": 2,
                             "A place to bake a cake or roast a turkey": 3,
                             "Electrical device used for washing clothes": 4,
                             },
                       'A': {"This is an activity where you use either a piece of machinery or a needle and thread kit to weave together a type of textile or fabric": 1,
                             "Faster than walking, slower than running": 2,
                             "Searching and gathering food and provisions from nature.": 3,
                             },
                       'N': {"The largest and heaviest bird that live in Australia": 1,
                             "Tadpoles grow into these hopping creatures": 2,
                             "A typically red flower representing love": 3,
                             }}

        self._answers = {'P': {1: "winston churchill",
                               2: "hercules",
                               3: "garfield",
                               4: "marge simpson",
                               5: "tarzan"
                               },
                         'W': {1: "heinz",
                               2: "prague",
                               3: "eiffel tower"
                               },
                         'O': {1: "piano",
                               2: "tent",
                               3: "oven",
                               4: "washing machine"
                               },
                         'A': {1: "sewing",
                               2: "jogging",
                               3: "foraging"
                               },
                         'N': {1: "ostrich",
                               2: "frog",
                               3: "rose"
                               }}

    def players_init(self):
        i = 0
        while i < self._player_no:
            name = input(f"Enter Player {i}'s name: ")
            player = Player(name)
            self._players.append(player)
            i += 1

    def return_category(self, category):
        if category == 'P':
            return "Person"
        elif category == 'W':
            return "World"
        elif category == 'O':
            return "Object"
        elif category == 'A':
            return "Action"
        else:
            return "Nature"

    def add_category_score(self, category, n):
        for option in self._category_score.keys():
            if category == option:
                self._category_score[option] += n

    def return_category_score(self, category):
        for option in self._category_score.keys():
            if category == option:
                return self._category_score[option]

    def guess_analyser(self, guess):
        guess = guess.lower()
        if guess.count(" ") == 1:
            space = guess.index(" ")
            guess_1 = guess[:space]
            guess_2 = guess[space+1:]
        else:
            guess_1 = guess
            guess_2 = guess
        return guess, guess_1, guess_2

    def game_program(self, player_no):
        timer_start = time.time()
        add_score = 0
        player = self._players[player_no]
        current_index = self.return_category_score(
            self._category) % len(self._hints[self._category])
        for hint, index in self._hints[self._category].items():
            time.sleep(0.8)
            if index > current_index:
                print(hint)
                guess = input(f"Word: ")
                guess, guess_1, guess_2 = self.guess_analyser(guess)
                if guess == "skip":
                    print("Word skipped.")
                else:
                    answer = self._answers[self._category][index]
                    answer = answer.lower()
                    while guess != answer and answer.count(guess_1) != 1 and answer.count(guess_2) != 1:
                        sub_time_taken = time.time() - timer_start
                        if sub_time_taken > self._turn_time:
                            break
                        print("Incorrect. Try again.")
                        guess = input(f"Word: ")
                        guess, guess_1, guess_2 = self.guess_analyser(guess)
                    if guess == answer or answer.count(guess_1) == 1 or answer.count(guess_2) == 1:
                        print("Correct!")
                        add_score += 1
                timer_end = time.time()
                main_time_taken = timer_end - timer_start
                if main_time_taken > self._turn_time - 5:
                    print("Time over.")
                    break
                print("Next Word.")
        return add_score

    def score_comparison(self, n):
        print("\nThe current scores are,")
        for player in self._players:
            print(f"{player.return_name()}: {player.return_score()}")

    def winner(self):
        print("\nThe game is now over.")
        print("Each players' final scores are now,")
        time.sleep(0.1)
        print(".")
        time.sleep(0.2)
        print("..")
        time.sleep(0.4)
        print("...")
        time.sleep(0.5)
        player_names = []
        player_scores = []
        for player in self._players:
            player_names.append(player.return_name())
            player_scores.append(player.return_score())
        scores_names = zip(player_scores, player_names)
        scores_names = sorted(scores_names)
        for i, score_name in enumerate(scores_names):
            print(f"Player: {score_name[1]} - Final Score: {score_name[0]}")
            if i == len(scores_names) - 1:
                print(f"Congratulations, {score_name[1]}! You are the winner.")

    def exit_program(self):
        exit = input("Would you like to stop the game? (Yes/No) ")
        exit = exit.lower()
        if exit == "yes":
            return -1
        else:
            return 0

    def game(self):
        print("Let us start the game.")
        self.number_of_players()
        self.players_init()
        self.load_data()
        time.sleep(1.5)
        while self._round <= self._round_max:
            if (self._round) == self._round_max:
                print("Final round!")
            else:
                print(f"Round {self._round}")
            for i, player in enumerate(self._players):
                print(f"{player.return_name()}'s turn")
                time.sleep(1)
                self._category = self._categories[player.return_score() % 5]
                print(
                    f"The category is {self.return_category(self._category)}.")
                print("First Word!")
                score = self.game_program(i)
                self._players[i].add_score(score)
                self.add_category_score(self._category, score)
            if (self._round) == self._round_max:
                print("Final round is over!")
            else:
                print(f"Round {self._round} is over.")
                self.score_comparison(self._round)
                ready = input("Ready for next round (Yes/No)? ").lower()
                while ready != "yes":
                    exit = self.exit_program()
                    if exit == -1:
                        return "Program exited."
                    time.sleep(10)
                    ready = input("Ready for next round (Yes/No)? ").lower()
            self._round += 1
        self.winner()

    def main(self):
        self.intro()
        self.start()
        self.game()


Game = Trivia()

Game.main()
