import random

def get_guess():
    print("guess a letter!")
    letter = input("> ")
    letter = letter.lower()
    return letter


def yes_or_no():
    while True:
        y_or_n = input("[Y/N] > ") 
        y_or_n = y_or_n.lower()

        if y_or_n == "y" or y_or_n == "n":
            return y_or_n
        
        else:
            print("Please type y or n!")


def get_word():
    words = ['golf', 'surprising', 'insight', 'galaxy', 'variation', 'founder', 'mount', 'belt', 'discussion', 'tent', 'speech', 'them',
     'classic', 'habitat', 'colonial', 'thing', 'stir', 'dramatically', 'judge', 'utility', 'incentive', 'accident', 'advance', 'ultimately',
      'investigation', 'sequence', 'philosophy', 'basket', 'introduction', 'exchange', 'overcome']

    random.shuffle(words)

    word = words[0]

    return word


def hide_letters(word):
    word_length = len(word)
    divide = word_length/4
    divide = round(divide)

    hide = divide
    
    result = []
    letters = []
    print_word = []

    for x in range(word_length):
        letters.append(x)

    random.shuffle(letters)

    for y in range(hide):
        result.append(word[letters[y]])

    for z in word:

        if z in result:
            print_word.append(z)

        elif z not in result:
            print_word.append("_")

    word_final = ""

    for l in print_word:
        word_final = word_final + l

    return word_final


def fill_gaps(word, word_final, guess):
    word_as_list = []
    word_final_as_list = []

    for x in word:
        word_as_list.append(x)
    
    for y in word_final:
        word_final_as_list.append(y)

    first_index = 0

    for z in word_as_list[first_index:]:

        if guess == z:

            index_letter = word_as_list.index(guess)
            word_as_list.pop(index_letter)
            word_as_list.insert(index_letter, '')
            
            word_final_as_list.pop(index_letter)
            word_final_as_list.insert(index_letter, guess)

            first_index = first_index +1

    word_final = ""

    for words in word_final_as_list:
        word_final = word_final + words

    return word_final


def main():

    while True:

        wrong_guesses = 0
        max_guesses = 5
        word = get_word()
        word_final = hide_letters(word)

        while True:

            print(word_final)
            guess = get_guess()
            
            if guess in word:
                word_final = fill_gaps(word, word_final, guess)

            else:
                wrong_guesses += 1

            print(f'Incorrect guesses: {wrong_guesses}/{max_guesses}')

            if wrong_guesses == max_guesses:
                print("You lose!")
                print(f"The word was {word}.")
                break

            if word == word_final:
                print(f"The word is {word}.")
                print("You win!")
                break
                
        print("Play again?")

        y_or_n = yes_or_no()

        if y_or_n == "y":
            continue
        
        if y_or_n == "n":
            exit(0)


if __name__ == '__main__':
    main()
        

        

    



        


    
