import random

try:  # Try to open word data file.

    word_file = open("textfiles/words.txt", "r+")

    print("Word data file exists.")

    # Here we read all the text from the text file using .readLines method and store the list in a variable.
    words = word_file.readlines()
    word_file.close()

    print(f"{len(words)} words in file.")

    # This function returns a random word from the words-list.
    def random_word():
        i: int = random.randint(0, len(words) - 1)
        return words[i].strip()

except FileNotFoundError:  # If no word data file exists then...

    # First we create an array of strings to write to a text file, this will act as our word database.
    list_of_words: [str] = [
        "slide",
        "dough",
        "error",
        "admit", "dozen", "equal", "grant", "weigh", "train", "trade", "elite", "budge", "still",
        "sheet", "carve", "fraud", "embox", "leash", "stamp", "claim", "handy", "alarm", "stall",
        "total", "stock", "curve", "ideal", "glide", "faith", "brave", "begin", "point", "rally",
        "split", "round", "loose", "party", "bride", "quiet"
    ]

    word_file = open("textfiles/words.txt", "w+")

    for word in list_of_words:
        word += "\n"
        word_file.writelines(word)

    word_file.close()
    print("Created word data file. Relaunch program.")
    #################
