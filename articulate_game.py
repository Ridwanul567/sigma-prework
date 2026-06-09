# Create a working Python version of Articulate with slight changes
# The program should ask for the number of users and tracks the number of correct answers of each player
# Question Types: Person, World, Object, Action, Nature, Random (May ignore)
# The winner is decided by who has the highest score after 5 turns

import time
import random
from rich import print


class Player:
    """Player class with associated name and score along with
    relevant functions to access the attributes."""

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
        self._category_values = {'P': [], 'W': [], 'O': [], 'A': [], 'N': []}
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
        """Introduction"""
        print(
            "[bold red]Welcome :grinning:![/] I hope you are ready to play my variant of the hit-game [bold purple]Articulate[/]!")
        print(
            "The aim of the game is to reach as high a [bold green]score[/] as possible.")
        print(
            "You have only [blue]1[/] hint for each word but, you get unlimited [bold yellow]skips[/] as well.")
        print("Try your best to succeed!")

    def start(self):
        """Asks whether the players would like full instructions."""
        print(
            "\nPlease enter [blue]1[/] if you want full instructions on how to play the game (recommended if you have not played before) or enter [blue]0[/] to start: ")
        want_full_instruct = input()
        want_full_instruct = int(want_full_instruct)
        return want_full_instruct

    def full_instructions(self):
        """Full instructions on how to play the game."""
        print("...")

    def number_of_players(self):
        """Sets number of players."""
        print("Enter [bold green]number[/] of [bold red]players[/]: ", end="")
        self._player_no = int(input())
        if self._player_no == 1:
            self._solo_mode = True

    def load_data(self):
        """Loads all hints and answers for each category."""
        self._hints = {'P': {1: "British :flag_for_united_kingdom:  Prime Minister from 1940-1945 and again from 1951-1955, most famous for successfully leading Britain out of World War II",
                             2: "Famous Hero in Greek Mythology, killed the monstrous Lernaean Hydra and ascended Mount Olympus",
                             3: "Orange Tabby cat who loves to eat lasagna",
                             4: "Wife of arguably the dumbest man in Springfields, iconic for her sky-high beehive blue hair",
                             5: "Famous disney character raised in the rainforest by apes",
                             6: "Austrian Movie Star, California's Governor and the Terminator",
                             7: "The King of Pop; he created the signature moonwalk dance",
                             8: "German Philosopher; founder of one of the most famous idealogies against capitalism",
                             9: "German Physicist; famous for his theories of relativity and E = mc2",
                             10: "English Physicist and Mathematician; He saw an apple fall onto the ground",
                             11: "A wooden-doll turned human boy whose nose grows longer for every lie he tells"
                             },
                       'W': {1: "America's largest manufacturer of ketchup, with an overall market share of more than 50%; founded in Pittsburgh",
                             2: "Capital of the Czech Republic; Surrounded by Germany, Poland, Slovakia and Austria; known for Charles Bridge, one of the largest castles in the world",
                             3: "Iron lattice tower landmark in Paris, France; 1000ft tall, most visited paid monument in the world",
                             4: "Capital city of Irag, the epicenter of research and academics in the Islamic Golden Age",
                             5: "A national memorial of the USA where the faces of presidents are carved into the mountain",
                             6: "A world heritage site in India, an ivory-white mausoleum incoorporating Indo-Islamic and Mughal architecture",
                             7: "The heart of the American film industry in LA, California",
                             8: "The capital of the UK, a financial hub with rich history",
                             9: "An independent city-state, serving as the global headquarters of the Roman Catholic Church",
                             10: "One of the most famous streets in the world where the decisions made on this street affect the global economy"
                             },
                       'O': {1: "Musical instrument with black and white keys",
                             2: "Small shelter for sleeping when camping",
                             3: "A place to bake a cake or roast a turkey",
                             4: "Electrical device used for washing clothes",
                             5: "A square of fabric used for personal hygiene, it is slightly outdated now",
                             6: "An execution device with a tall frame and an angled blade suspended at the top",
                             7: "A small spoon typically used to stir or add sugar to tea",
                             8: "The flexible appendage at the rear of animal not present in humans",
                             9: "A chart used to track the days and months across a year",
                             10: "A metal percussion instrument that is bended into a particular shape",
                             11: "A thick rubber ring that surrounds the wheels of a vehicle"
                             },
                       'A': {1: "This is an activity where you use either a piece of machinery or a needle and thread kit to weave together a type of textile or fabric",
                             2: "Faster than walking, slower than running",
                             3: "Searching and gathering food and provisions from nature.",
                             4: "The rhythmic process of inhaling and exhaling air to enable life",
                             5: "Removing clothes from oneself",
                             6: "Taking another person's possessions without permission",
                             7: "Casting light on an area to make it brighter (or describing something that provides clarity)",
                             8: "Removing material from a surface possibly the leftovers in a pot",
                             9: "Gathering close together as a group, sharing warmth and protecting one another",
                             10: "The unintentional lose of saliva from the mouth possibly when daydreaming",
                             },
                       'N': {1: "The largest and heaviest bird that live in Australia",
                             2: "Tadpoles grow into these hopping creatures",
                             3: "A typically red flower representing love",
                             4: "A small, heavily armored mammal that is known for rolling up into a ball",
                             5: "The smallest dog breed in the world that is typically very feisty",
                             6: "Bright red berry that is iconically shown as a pair",
                             7: "Small crustaceans that love to stick on top of rocks, other sea animals and even the underside of ships",
                             8: "A venomous, slithery creature that alert predators with a shake of their tail",
                             9: "A baby version of a cow",
                             10: "A small organism that drifts in the water, eaten by creatures as small as krill to as large as whales",
                             }}

        self._answers = {'P': {1: "winston churchill",
                               2: "hercules",
                               3: "garfield",
                               4: "marge simpson",
                               5: "tarzan",
                               6: "arnold schwarzenegger",
                               7: "michael jackson",
                               8: "karl marx",
                               9: "albert einstein",
                               10: "isaac newton",
                               11: "pinocchio"},
                         'W': {1: "heinz",
                               2: "prague",
                               3: "eiffel tower",
                               4: "baghdad",
                               5: "mount rushmore",
                               6: "taj mahal",
                               7: "hollywood",
                               8: "london",
                               9: "vatican city",
                               10: "wall street"},
                         'O': {1: "piano",
                               2: "tent",
                               3: "oven",
                               4: "washing machine",
                               5: "handkerchief",
                               6: "guillotine",
                               7: "teaspoon",
                               8: "tail",
                               9: "calendar",
                               10: "triangle",
                               11: "tyre"
                               },
                         'A': {1: "sewing",
                               2: "jogging",
                               3: "foraging",
                               4: "breathing",
                               5: "undressing",
                               6: "stealing",
                               7: "illuminating",
                               8: "scraping",
                               9: "huddling",
                               10: "drooling"
                               },
                         'N': {1: "ostrich",
                               2: "frog",
                               3: "rose",
                               4: "armadillo",
                               5: "chihuahua",
                               6: "cherry",
                               7: "barnacle",
                               8: "rattlesnake",
                               9: "calf",
                               10: "plankton"
                               }}

        self._category_values['P'] = list(
            range(1, len(self._answers['P'])+1, 1))
        self._category_values['W'] = list(
            range(1, len(self._answers['W'])+1, 1))
        self._category_values['O'] = list(
            range(1, len(self._answers['O'])+1, 1))
        self._category_values['A'] = list(
            range(1, len(self._answers['A'])+1, 1))
        self._category_values['N'] = list(
            range(1, len(self._answers['N'])+1, 1))

    def players_init(self):
        """Asks for each player's name."""
        i = 0
        names = []
        while i < self._player_no:
            print(
                f"Enter [bold red]Player[/] [bold blue]{i+1}[/]'s [bold green]name[/]: ", end=" ")
            name = input()
            for used_name in names:
                while name == used_name:
                    print(
                        "This [bold green]name[/] is already used. Please use another [bold green]name[/].")
                    print(
                        f"Enter [bold red]Player[/] [bold blue]{i+1}[/]'s [bold green]name[/]: ", end=" ")
                    name = input()
            player = Player(name)
            self._players.append(player)
            names.append(name)
            i += 1

    def return_category(self, category):
        """Returns the category name for a chosen category."""
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
        """Adds to the total number of correct answers in a chosen category."""
        for option in self._category_score.keys():
            if category == option:
                self._category_score[option] += n

    def return_category_score(self, category):
        """Returns the total number of correct answers in a chosen category."""
        for option in self._category_score.keys():
            if category == option:
                return self._category_score[option]

    def guess_analyser(self, guess, answer):
        """Breaks down guesses made so that all valid answers can be considered
            e.g. for answer: Albert Einstein, guessing Einstein is valid."""
        guess = guess.lower()
        guess_1 = guess
        guess_2 = guess
        answer = answer.lower()
        answer_1 = answer
        answer_2 = answer
        if guess.count(" ") == 1:
            space_g = guess.index(" ")
            guess_1 = guess[:space_g]
            guess_2 = guess[space_g+1:]
        if answer.count(" ") == 1:
            space_a = answer.index(" ")
            answer_1 = answer[:space_a]
            answer_2 = answer[space_a+1:]
        if self._category == 'P':
            if guess == answer or guess_1 == answer_1 or guess_2 == answer_2:
                return True
            else:
                return False
        elif guess != answer and (guess_1 == answer_1 or guess_2 == answer_2):
            return "Close"
        else:
            if guess == answer:
                return True
            else:
                return False

    def game_program(self, player_no):
        """Runs all processes for a single player to make as many guesses from hints in 30s."""
        timer_start = time.time()
        add_score = 0
        player = self._players[player_no]
        main_time_taken = 0
        while main_time_taken < self._turn_time:
            time.sleep(0.8)
            if self._category_values[self._category] == []:
                print("[bold red]All Hints Used![/]")
                return add_score
            hint_index = random.choice(self._category_values[self._category])
            hint = self._hints[self._category][hint_index]
            print(hint)
            print("[bold green]Word[/]: ", end="")
            guess = input()
            guess = guess.lower()
            if guess == "skip":
                print("[bold green]Word[/] [bold yellow]skipped[/].")
            elif guess == "!exit":
                return -1
            else:
                answer = self._answers[self._category][hint_index]
                answer = answer.lower()
                check = self.guess_analyser(guess, answer)
                while check == False or check == "Close":
                    if check == False:
                        print("[bold red]Incorrect.[/]")
                    else:
                        print("[bold yellow]Close.[/] You are a missing a term.")
                    sub_time_taken = time.time() - timer_start
                    if sub_time_taken > self._turn_time:
                        break
                    print("Try again.")
                    guess = input(f"Word: ")
                    guess = guess.lower()
                    check = self.guess_analyser(guess, answer)
                    if guess == "skip":
                        print("[bold green]Word[/] [bold yellow]skipped[/].")
                        break
                    elif guess == "!exit":
                        return -1
                if check == True:
                    print("[bold green]Correct![/]")
                    add_score += 1
                    self._category_values[self._category].remove(hint_index)
                    # self._category_values[self._category] = np.delete(
                    #    self._category_values[self._category], hint_index - 1)
            timer_end = time.time()
            main_time_taken = timer_end - timer_start
            if main_time_taken > self._turn_time - 5:
                print("[red]Time over.[/]")
                break
            print("Next Word.")
        return add_score

    def score_comparison(self, n):
        """Presents the current scores across every player."""
        print("\nThe current [bold green]scores[/] are,")
        for player in self._players:
            print(
                f"[bold green]{player.return_name()}[/]: [bold blue]{player.return_score()}[/]")

    def winner(self):
        """Called after the final round.
            Shows the final scores across every player and congratulates the winner."""
        print("\nThe game is now over.")
        print(
            "Each [bold green]players'[/] [bold purple]final[/] [bold green]scores[/] are now,")
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
        tie_index = []
        for i, score_name in enumerate(scores_names):
            print(
                f"[bold green]Player[/]: {score_name[1]} - [bold purple]Final[/] [bold green]Score[/]: [bold blue]{score_name[0]}[/]")
            if score_name[0] == scores_names[self._player_no-1][0]:
                tie_index.append(i)
        if len(tie_index) > 1:
            print(f"\nWow, we have a {len(tie_index)}-way tie!")
            print(f"The [bold yellow]winners[/] are: ", end="")
            for player_no in tie_index:
                if player_no == self._player_no - 1:
                    print(
                        f"[bold green]{scores_names[player_no][1]}[/]. [bold yellow]Congratulations![/]")
                else:
                    print(
                        f"[bold green]{scores_names[player_no][1]}[/], ", end="")
        else:
            print(
                f"[bold yellow]Congratulations[/], [bold green]{scores_names[self._player_no-1][1]}[/]! You are the [bold yellow]winner[/].")

    def exit_program(self):
        """Asks after a round whether the players would to stop playing."""
        print(
            "Would you like to stop the game? ([bold green]Yes[/]/[bold red]No[/]) ", end="")
        exit = input()
        exit = exit.lower()
        if exit == "yes":
            return -1
        elif exit == "no":
            return 0
        else:
            print("That was an [bold red]invalid[/] answer.")
            print(
                "Please, enter [bold red]No[/] if you would like to continue the game otherwise you will be [bold purple]force[/] exited.")
            exit = input()
            exit.lower()
            if exit == "no":
                return 0
            else:
                return -1

    def game(self):
        """Runs each round of the game while tracking scores and the hints that have been used."""
        print("Let us [bold green]start[/] the [bold purple]game[/].")
        self.number_of_players()
        self.players_init()
        self.load_data()
        time.sleep(1.5)
        while self._round <= self._round_max:
            if (self._round) == self._round_max:
                print("[bold purple]Final round![/]")
            else:
                print(f"[bold green]Round {self._round}[/]")
            for i, player in enumerate(self._players):
                print(f"[bold green]{player.return_name()}[/]'s turn")
                time.sleep(1)
                self._category = self._categories[player.return_score() % 5]
                print(
                    f"The [bold yellow]category[/] is [bold yellow]{self.return_category(self._category)}[/].")
                print("[bold green]First Word![/]")
                score = self.game_program(i)
                if score == -1:
                    print("[bold purple]Program Exited.[/]")
                    return None
                self._players[i].add_score(score)
                self.add_category_score(self._category, score)
            if (self._round) == self._round_max:
                print("[bold purple]Final round is over![/]")
            else:
                print(f"[bold green]Round {self._round} is over.[/]")
                self.score_comparison(self._round)
                print(
                    "Ready for next round ([bold green]Yes[/]/[bold red]No[/])?", end=" ")
                ready = input().lower()
                while ready != "yes":
                    exit = self.exit_program()
                    if exit == -1:
                        print("[bold purple]Program Exited.[/]")
                        return None
                    time.sleep(10)
                    print(
                        "Ready for next round ([bold green]Yes[/]/[bold red]No[/])?", end=" ")
                    ready = input().lower()
            self._round += 1
        self.winner()

    def main(self):
        """Required to be called for the game to proceed."""
        self.intro()
        self.start()
        self.game()


Game = Trivia()

Game.set_max_rounds(3)
Game.set_turn_time(50)
Game.main()


# Need to add docstrings / Clean code for better logic
# Randomise what words are called - Tick
# Improve UI (so that not too much info)
# Learn how to improve design on terminal
# Add Tie Option at end - Tick
# Give help when part of word is mentioned e.g. Eiffel for Eiffel Tower - Tick
