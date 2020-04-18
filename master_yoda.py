def master_yoda(sentence):
    reversedSentence = sentence.split()
    reversedSentence.reverse();
    return " ".join(reversedSentence)

x = master_yoda("How are you doing")
y = master_yoda("Today was a good day")

print(f"How are you doing: {x}")
print(f"Today was a good day: {y}")
