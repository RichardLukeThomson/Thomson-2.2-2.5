#3.1.1.4
#Using one of the comparison operators in Python, write a simple two-line program that takes the parameter n as input, which is an integer, and prints False if n is less than 100, and True if n is greater than or equal to 100.
#Don't create any if blocks (we're going to talk about them very soon). Test your code using the data we've provided for you.
#x = int(input("Enter a number: "))
#print(x >= 100)

#3.1.1.10
#Spathiphyllum, more commonly known as a peace lily or white sail plant, is one of the most popular indoor houseplants that filters out harmful toxins from the air. Some of the toxins that it neutralizes include benzene, formaldehyde, and ammonia.
#Imagine that your computer program loves these plants. Whenever it receives an input in the form of the word Spathiphyllum, it involuntarily shouts to the console the following string: "Spathiphyllum is the best plant ever!"
test = input("Whats the best flower ever?: ")
if test == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif test == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
elif test== "Statham":
    print("Nearly!")
else:
    print("Spathiphyllum! Not",test + "!")

#3.1.1.11
# Once upon a time there was a land - a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course - their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:
# if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
# if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
# Your task is to write a tax calculator.
# It should accept one floating-point value: the income.
# Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you - you'll find it in the skeleton code in the editor.
# income = float(input("Enter the annual income: "))
income = float(input("Enter the annual income: "))
if income < 85528:
	tax = income * 0.18 - 556.02
else:
	tax = (income - 85528) * 0.32 + 14839.02
if tax < 0.0:
	tax = 0.0
tax = round(tax, 0)
print("Your tax is:", tax, "thalers")
year = int(input("Enter a year: "))

#3.1.1.12
# As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.
# Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:
# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.
# Look at the code in the editor - it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.
# The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.
# It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period. Tip: use the != and % operators.
# Test your code using the data we've provided.
year = int(input("Enter year: "))
if year < 1582:
	print("Not within the Gregorian calendar")
else:
	if year % 4 != 0:
		print("Common year")
	elif year % 100 != 0:
		print("Leap year")
	elif year % 400 != 0:
		print("Common year")
	else:
		print("Leap year")

#3.2.1.3
# A junior magician has picked a secret number. He has hidden it in a variable named secret_number. He wants everyone who run his program to play the Guess the secret number game, and guess what number he has picked for them. Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.
# Your task is to help the magician complete the code in the editor in such a way so that the code:
# will ask the user to enter an integer number;
# will use a while loop;
# will check whether the number entered by the user is the same as the number picked by the magician. If the number chosen by the user is different than the magician's secret number, the user should see the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again. If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, and the magician should say the following words: "Well done, muggle! You are free now."
# The magician is counting on you! Don't disappoint him.
secret=777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
user_number = int(input("Enter number: "))
while user_number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    user_number = int(input("Enter the number again: "))
print(secret_number, "Well done, muggle! You are free now.")

#3.2.1.6
import time
for second in range(1, 6):
    print(second, "Mississippi")
    time.sleep(1)
    print("Ready or not, here I come!")

#3.2.1.9
while True:
    word = input("You're stuck in an infinite loop!\nEnter the secret word to leave the loop: ")
    if word == "chupacabra":
        break
print("You've successfully left the loop!")

#3.2.1.10
user_word = input("Enter your word: ")
for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
print(letter)

#3.2.1.10
word_without_vowels = ""
user_word = input("Enter your word: ")
user_word = user_word.upper()
for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter
print(word_without_vowels)
#3.2.1.14
blocks = int(input("Enter the number of blocks: "))
height = 0
in_layer = 1
while in_layer <= blocks:
    height += 1
    blocks -= in_layer
    in_layer += 1
print("The height of the pyramid:", height)
#3.2.1.15
c0 = int(input("Enter c0: "))
if c0 > 1:
	steps = 0
	while c0 != 1:
		if c0 %2 != 0:
			cnew = 3 * c0 + 1
		else:
			cnew = c0 // 2
		print(c0)
		c0 = cnew
		steps += 1
	print("steps =",steps)
else:
	print("Bad c0 value")