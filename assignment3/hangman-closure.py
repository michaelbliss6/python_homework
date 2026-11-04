def make_hangman(secret_word):
    guesses = []
    
    def hangman_closure(letter):
        guesses.append(letter)
        display = "".join(ch if ch in guesses else "_" for ch in secret_word)
        print(display)
        return all(ch in guesses for ch in secret_word)

    return hangman_closure

def main():
    secret_word = input("Enter the secret word:").strip().lower()
    hangman = make_hangman(secret_word)

    done = False
    while not done:
        letter = input("Guess a letter: ").strip().lower()
        done = hangman(letter)

    print("You guessed the word!")


if __name__ =="__main__":
    main()
