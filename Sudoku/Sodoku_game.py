from random import sample

class Game:
    def __init__(self):
        print("Welcome to Sudoku!")
        self.get_board = Board()
        self.sudoku_board,self.hidden_board, = self.get_board.generate_board()
        self.main()

    def user_choice(self):
        print("Enter a square followed by the value you want to input into it seperated by spaces.")
        print("For example: X Y VALUE")
        x, y, userchoice = input("> ").split()
        x = int(x)
        y = int(y)
        x -=1
        y -=1
        userchoice = int(userchoice)

        return y, x, userchoice
        

    def y_n(self):
        while True:
            yes_or_no = input("[Y/N] > ")
            yes_or_no = yes_or_no.lower()

            if yes_or_no == "y" or yes_or_no == "n":
                return yes_or_no

            else:
                print("Please enter Y or N!")


    def game_over(self, vic_or_lose):

        if vic_or_lose == "Victory":
            print("You win! Congratulations!")
            print("Play again?")

        elif vic_or_lose == "Lose":
            print("You lose!")
            print("Try again?")

        restart_or_quit = self.y_n()

        if restart_or_quit == "y":
            Game()
        elif restart_or_quit == "n":
            exit(0)


    def main(self):
        wrong_guesses = 0

        while True:

            x, y, userchoice = self.user_choice()

            if self.sudoku_board[x][y] == userchoice:
                self.hidden_board[x][y] = self.sudoku_board[x][y]

            else:
                wrong_guesses += 1
                print(" ")
                print(" ")
                print("Incorrect guess.")

                if wrong_guesses == 3:
                    print(" ")
                    print(" ")
                    self.game_over("Lose")
                    

                print(f"{wrong_guesses}/3 wrong guesses.")

            start = 1
            self.get_board.outputboard(self.hidden_board, start)
            self.sudoku_board = [ [self.get_board.nums[self.get_board.pattern(r,c)] for c in self.get_board.cols] for r in self.get_board.rows ]

            board_as_a_single_list_for_checking_win = []
            
            for x in self.hidden_board:

                board_as_a_single_list_for_checking_win.extend(x)

                if 0 not in board_as_a_single_list_for_checking_win:
                    self.game_over("Victory")

            board_as_a_single_list_for_checking_win.clear()

            
class Board:

    def __init__(self):
        self.base = 3
        self.side = self.base * self.base
        self.rBase = range(self.base) 
        self.rows  = [ g*self.base + r for g in self.shuffle(self.rBase) for r in self.shuffle(self.rBase) ] 
        self.cols  = [ g*self.base + c for g in self.shuffle(self.rBase) for c in self.shuffle(self.rBase) ]
        self.nums  = self.shuffle(range(1,self.base*self.base+1))


    def outputboard(self,board, start):

        if start == 0:
            squares = self.side*self.side
            empties = squares * 3//4 

            for p in sample(range(squares),empties):
                board[p//self.side][p%self.side] = 0

        numSize = len(str(self.side))
        x = 1

        for line in board:
            print((f"{x}")+"["+"  ".join(f"{n or '.':{numSize}}" for n in line)+"]")
            x+=1

        print("  1  2  3  4  5  6  7  8  9")
        

    def pattern(self,r,c):
        return (self.base*(r%self.base)+r//self.base+c)%self.side


    def shuffle(self,s): 
        return sample(s,len(s)) 


    def generate_board(self):

        [6, 2, 5, 8, 4, 3, 7, 9, 1]
        [7, 9, 1, 2, 6, 5, 4, 8, 3]
        [4, 8, 3, 9, 7, 1, 6, 2, 5]
        [8, 1, 4, 5, 9, 7, 2, 3, 6]
        [2, 3, 6, 1, 8, 4, 9, 5, 7]
        [9, 5, 7, 3, 2, 6, 8, 1, 4]
        [5, 6, 9, 4, 3, 2, 1, 7, 8]
        [3, 4, 2, 7, 1, 8, 5, 6, 9]
        [1, 7, 8, 6, 5, 9, 3, 4, 2]

        sudoku_board = [ [self.nums[self.pattern(r,c)] for c in self.cols] for r in self.rows ]
        hidden_board = sudoku_board
        
        start = 0

        self.outputboard(hidden_board, start)
        sudoku_board = [ [self.nums[self.pattern(r,c)] for c in self.cols] for r in self.rows ]

        return sudoku_board, hidden_board, 
    
Game()




