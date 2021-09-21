#2.6.1.9 Scenario
# Your task is to complete the code in order to evaluate the results of four basic arithmetic operations.
# The results have to be printed to the console.
float_a = float(input("A:")) 
float_b = float(input("B:"))
print ('output the result of addition of float_a and float_b is', (float_a + float_b))
print ("output the result of subtraction of float_a and float_b is", (float_a - float_b))
print ("output the result of multiplication of float_a and float_b is", (float_a * float_b))
print ("output the result of division of float_a and float_b is ", (float_a / float_b))
print("\nThat's all, folks!")

#2.6.1.10 
# Your task is to complete the code in order to evaluate the following expression:
# The result should be assigned to y. Be careful - watch the operators and keep their priorities in mind. Don't hesitate to use as many parentheses as you need.
# You can use additional variables to shorten the expression (but it's not necessary). Test your code carefully.
x = float(input("x :"))
y = 1/(x+1/(x+1/(x+1/x)))
print ("y= ", y)

#2.6.1.11
# Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.
# For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
big_hand = ((dura + mins) // 60 + hour) % 12
little_hand = (mins + dura) % 60
#print('End time: ',big_hand, ':',little_hand,sep='')

name = input("Enter future sirname in 2022: ")
if name == "Thomson":
    print("Yes - You lucky thing Julia!")
elif name == "Kozaryn":
    print("No, Your wrong Julia!")
elif name == "Statham":
    print("Nearly!")
else:
    print("Thomson! Not", name + "!")