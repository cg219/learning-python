def animal_crackers(word):
    wordList = word.lower().split()

    return wordList[0][0] == wordList[1][0]:

match = animal_crackers('Levelheaded Llama')
nomatch = animal_crackers('Crazy Kangaroo')

print(f"Levelheaded Llama: {match}")
print(f"Crazy Kangaroo: {nomatch}")
