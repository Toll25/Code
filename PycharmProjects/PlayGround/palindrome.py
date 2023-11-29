#!/usr/bin/env python3

import os

file = open(os.path.dirname(__file__) + "/palindrom_input.txt")
palindromes = []


class Palindrome:
    def __init__(self, value, length):
        self.value = value
        self.length = length

    def __str__(self):
        return f"Palindrome(value: {self.value}, length: {self.length}"


def findPalindromes(string):
    string = string.strip()
    if isinstance(string, str):
        for i in range(0, len(string)):
            for k in range(i, len(string)+1):
                newString = string[i:k]
                if newString == newString[::-1]:
                    if len(newString) >= 3:
                        palindromes.append(Palindrome(newString, len(newString)))


for j in file:
    findPalindromes(j)

longest = Palindrome("", 0)
for y in palindromes:
    if longest.length < y.length:
        longest = y

if longest.length == 0:
    print("No Palindromes")
else:
    print(longest)

'''
#Erweiterung

if len(palindromes) != 0:
    for y in palindromes:
        print(y)
else:
    print("No Palindromes")
'''

