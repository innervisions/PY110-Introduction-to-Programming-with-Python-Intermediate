statement = "The Flintstones Rock"

letter_frequency = {}
for char in statement:
    if char.isalpha():
        letter_frequency[char] = letter_frequency.get(char, 0) + 1

print(letter_frequency)
