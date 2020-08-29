import random

print("H A N G M A N\n")
word_list = ['python', 'java', 'kotlin', 'javascript']

random_word = random.choice(word_list)

your_guess = (len(random_word)) * "-"  # All the characters you have guessed

for count in range(8):
    print(your_guess)
    print("Input a letter: ")
    letter = input()
    if letter in random_word:
        new_word = ""  # To make changes in your_guess word in current loop
        for i in range(len(random_word)):
            if letter == random_word[i]:
                new_word = new_word + letter  # Add letter for your_guess word
            elif your_guess[i] != "-":
                new_word = new_word + your_guess[i]  # Update new_word if character already present in your_guess word
            else:
                new_word = new_word + "-"
        your_guess = new_word  # Assign all changes from this loop in your_guess word
    else:
        print("No such letter in the word\n")

print("Thanks for playing!")
print("We'll see how well you did in the next stage")