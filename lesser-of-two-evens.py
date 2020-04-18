def lesser_of_evens(a,b):
    if (a % 2 == 0) and (b % 2 == 0):
        return a if a < b else b
    else:
        return a if a > b else b

evens = lesser_of_evens(2,4)
odds = lesser_of_evens(2,5)

print(f"Evens (2,4): {evens}")
print(f"Odds (2,5): {odds}")
