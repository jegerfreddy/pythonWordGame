from handleWordFile import random_word

secret_word: str = random_word()
hidden_word: [str] = ["*", "*", "*", "*", "*"]
num_of_tries: int = 0
guessed_the_word: bool = False

print("\n")
print("     Hello! Welcome to Word Guesser!\n", "-- Type /rules to learn how to play! --", "\n\n")


def check_guess(correct_word: str, user_guess: str):
    global num_of_tries, guessed_the_word, hidden_word

    num_of_tries += 1

    if user_guess.lower() == correct_word.lower():
        guessed_the_word = True

        print(f"\nCongratulations! '{user_guess.lower()}' is the correct word!")
        print(f"You managed to find the word in {num_of_tries} guess(es).\n\n", "Restart to try again!")

    if not guessed_the_word:

        i = 0

        for _ in hidden_word:
            hidden_word[i] = "*"
            i += 1

        i = 0

        for letter in user_guess:

            charsInCorrect = correct_word.count(letter) # Counts instances of a letter in the correct word.
            charsInGuessS = hidden_word.count(letter) # Counts instances of lowercase letters guessed by user.
            charsInGuessB = hidden_word.count(letter.upper()) # Counts instances of uppercase letters guessed by user.

            if letter == correct_word[i]:

                hidden_word[i] = letter.upper()

            elif (letter in correct_word) and (hidden_word[i].lower() != correct_word[i]) and (charsInCorrect > (charsInGuessS + charsInGuessB)):

                hidden_word[i] = letter.lower()

            i += 1

    return hidden_word


print("      *** PyWord ***\n", "  --------------------\n", hidden_word, "\n")

while not guessed_the_word:
    guess: str = input("Guess the word: ")

    if guess == "/rules":
        print(
            "\nWhen you guess a word, lets say 'Cramp', a list of letters will show up like this:\n"
            "(Correct word is CHAIR)\n"
            "['C', 'r', 'A', '*', '*'].\n"
            "'Lowercase' = correct letter but wrong placement.\n"
            "'Uppercase' = correct letter AND correct placement.\n"
            "   '*'    = Letter not in solution\n"
            "Good luck! :)\n"
        )

    elif guess == "/thebigh4ck":

        message = "?edoc ecruos eht daer uoy diD"

        print("The word is: '", secret_word, f"' -- {message[::-1]}", "\n")

    elif len(guess) < 6:
        hidden_word: [str] = check_guess(secret_word, guess)

        if not guessed_the_word:
            print(f"{hidden_word}\n")

    else:
        print("Your guess can only contain up to 5 letters")
