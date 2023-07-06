def remove_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [letter for letter in string if letter.lower() not in vowels]
    result = ''.join(result)
    print(result)

#string = "Write a function that takes in a string and returns the string with all the vowels removed."
#remove_vowel(string)
