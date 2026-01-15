print("Hello, started my data science journey today")

#a program that asks the user to enter their name and their age and prints out a message addressed to them that tells them the year that they will turn 100 years old
name= input("Please enter your name")
age = input("Please enter your age")
yearsAhead= 100- int(age)
YearToBe= 2026+ int(yearsAhead)
print(f"{name} you'd be hundred in {YearToBe}")


#a program that prints out all the elements of the list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lessnum = []

for num in a:
    if num< 5:
        lessnum.append(num)
        lessnum.sort()
print(lessnum)
