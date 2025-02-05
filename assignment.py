#1.A programme to check whether a year is a leap year or not
from operator import truediv

year = 2020
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year,"is a leap year")
else:
        print(year,"is not a leap year")

#2.A programme to check whether a letter is a consonant or a vowel
letter = 'b'
if letter in 'aeiou':
        print(letter,"is a vowel")
else:
        print(letter,"is a consonant")