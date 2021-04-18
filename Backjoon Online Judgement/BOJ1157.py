letters = list(input())
alphabets = []
highest_count = None
count = 0

for letter in letters:
    alphabets.append(letter.lower())

for alphabet in set(alphabets):
    if alphabets.count(alphabet) > count:
        count = alphabets.count(alphabet)
        highest_count = alphabet
    elif alphabets.count(alphabet) == count:
        count = alphabets.count(alphabet)
        highest_count = '?'

print(highest_count.upper())
