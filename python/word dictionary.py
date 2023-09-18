from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter the word:")
    print(dictionary.meaning(word))
    break