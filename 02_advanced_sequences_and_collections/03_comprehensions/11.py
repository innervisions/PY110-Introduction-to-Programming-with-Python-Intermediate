dict1 = {
    "first": ["the", "quick"],
    "second": ["brown", "fox"],
    "third": ["jumped"],
    "fourth": ["over", "the", "lazy", "dog"],
}

# Your code goes here
def get_vowels(word):
    return ''.join([char for char in word if char in 'aeiou'])

list_of_vowels = [[get_vowels(word) for word in words] for words in dict1.values()]

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
