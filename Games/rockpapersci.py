import random


moves = ['rock', 'paper', 'scissors']


# player class that other classes are created from
class Player():
    my_move = None
    their_move = None

    def move(self):
        return moves[0]

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


# establish human player with choice input ability
class HumanPlayer(Player):

    def move(self):
        while True:
            turn = input("SHOOT! ")
            if turn.lower() not in moves:
                print("Invalid throw. Choose rock, paper, or scissors.")
            else:
                return(turn.lower())


# first of the AI players, rng used to determine choice of AI
class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


# this class reflects the last move of the player, unless there are no throws
class ReflectPlayer(Player):
    def move(self):
        if self.their_move == "None":
            return random.choice(moves)
        elif self.their_move == 'paper':
            return 'paper'
        elif self.their_move == 'scissors':
            return 'scissors'
        else:
            return 'rock'


# class cycles through rock, paper, scissors
class CyclePlayer(Player):
    def move(self):
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'


# game class where the bulk of the game is created
class Game:

    def __init__(self, my_move, their_move):
        self.p1 = my_move
        self.p2 = their_move

    def play_game(self):
        self.p1_score = 0
        self.p2_score = 0
        print("Let's play rock, paper, scissors!\n")
        for round in range(3):
            print(f"Round {round}: Ro, Sham, Bo...")
            self.play_round()
        if self.p1_score > self.p2_score:
            print("The human player has won!")
            print("The superiority of man-kind over machines is maintained.")
            print("The final score is " + str(self.p1_score) +
                  " to " + str(self.p2_score))
            print("Excellent work!!!\n")
        elif self.p1_score < self.p2_score:
            print("The computer won!")
            print("The final score is " + str(self.p1_score) +
                  " to " + str(self.p2_score))
            print("Bow down to your AI overlords!\n")
        else:
            print("A winner could not be determined")
            print("The final score is " + str(self.p1_score) +
                  " to " + str(self.p2_score))
            print("The AI and Player have tied!\n")
        replay = input("To replay, type yes. Otherwise, type anything else.\n")
        while replay.lower() == "yes":
            game.play_game()
        else:
            print("\nMan vs machines - its a fun time!")
            print("Playing an AI is not a zero-sum game.")
            print("Remember that.\n")
            print("Thank you for playing!\n")
            quit()

    def play_round(self):
        throw1 = self.p1.move()
        throw2 = self.p2.move()
        print(f"Man: {throw1}  Machine: {throw2}\n")
        self.p1.learn(throw1, throw2)
        self.p2.learn(throw2, throw1)
        if beats(throw1, throw2):
            print("Man wins this time!\n")
            self.p1_score += 1
        elif beats(throw2, throw1):
            print("Ouch! That's a win for the Machines.\n")
            self.p2_score += 1
        else:
            print("The odds of this happening is high, Tie Game!\n")

        print("Human: " + str(self.p1_score)
              + " Machine: " + str(self.p2_score))


def beats(throw1, throw2):
    return ((throw1 == 'rock' and throw2 == 'scissors') or
            (throw1 == 'scissors' and throw2 == 'paper') or
            (throw1 == 'paper' and throw2 == 'rock'))


if __name__ == '__main__':
    play_style = {
        "1": Player(),
        "2": RandomPlayer(),
        "3": CyclePlayer(),
        "4": ReflectPlayer(),
    }
while True:
    user_input = input("\nTo start, please select a strategy:\n\n"
                       "Press 1 for a less challeging, repetive strategy...\n"
                       "Press 2 for a seemingly crafty random AI...\n"
                       "Press 3 to go through a cycle strategy...\n"
                       "Press 4 for what will seem like an obnoxious AI...\n"
                       )
    if user_input not in play_style:
        print("\nPlease choose a valid play style!")
    else:

        game = Game(HumanPlayer(), play_style[user_input])
        game.play_game()
