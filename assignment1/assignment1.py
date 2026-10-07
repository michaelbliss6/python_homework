# Write your code here.

#Task 1
def hello():
    print("Hello!")
hello()

#Task 2
def greet(name):
    print("Hello, " + name + "!")
greet("Michael")

#Task 3
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                raise ValueError(f"Unknown operation '{operation}'")

    except ZeroDivisionError:
        return "You can't divide by 0!"

    except TypeError:
        return f"You can't {operation} those values!"

#Task 4
def data_type_conversion(value, type):
    converters = {"float": float, "str": str, "int": int}

    try:
        return converters[type](value)
    
    except (ValueError, TypeError, KeyError):
            return f"You can't convert {value} into a {type}."

#Task 5
def grade(*args):
    try:
       average = sum(args) / len(args)

    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."
        
    if average >= 90:
        return "A"
    elif average <= 80:
        return "B"
    elif average <= 70:
            return "C"
    elif average <= 60:
            return "D"
    else:
        return "F"

#Task 6
def repeat(string, count):
    result = ""
    for i in range(count):
        result += string
    return result

#Task 7
def student_scores(mode, **kwargs):
    if mode == "best":
        best_name = None
        best_score = None
        for name, score in kwargs.items():
            if best_score is None or score > best_score:
                best_name = name
                best_score = score
        return best_name
    elif mode == "mean":
        return sum(kwargs.values()) / len(kwargs)

#Task 8
little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}

def titlize(title):
    words = title.lower().split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in little_words:
            result.append(word.capitalize())
        else:
            result.append(word)
    return " ".join(result)

titles = [
    "the lord of the rings",
    "a tale of two cities",
    "don't stop believing",
]

for title in titles:
    print(titlize(title))

#Task 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result = result + letter
        else:
            result = result + "_"
    return result
print(hangman("alphabet", "ab"))

#Task 10
def pig_latin_word(word):
    vowels = "aeiou"
    i = 0
    while i < len(word) and word[i] not in vowels:
        if word[i] == "q" and i + 1 < len(word) and word[i + 1] == "u":
            i = i + 2
        else:
            i = i + 1
    return word[i:] + word[:i] + "ay"

def pig_latin(sentence):
    words = sentence.split()
    result = []
    for word in words:
        result.append(pig_latin_word(word))
    return " ".join(result)

print(pig_latin("the quick brown fox"))