# Exercise 1.1

#  1. In a print statement, what happens if you leave out one of the parentheses, or both?
#  2. If you are trying to print a string, what happens if you leave out one of the quotation marks,
#  or both?
#  3. You can use a minus sign to make a negative number like-2. What happens if you put a plus
#  sign before a number? What about 2++2?

#  4. In math notation, leading zeros are ok, as in 09. What happens if you try this in Python?
#  What about 011?
#  5. What happens if you have two values with no operator between them

# # print("Hello, World!")
# # print("Hello, World!")
# ("Hello, World!")
# print("Hello, World!")
# print("Hello, World")
# print(HelloWorld)
# print("Hello, World!)

# print(2++3)
# print(2+++3)
# print(2+-3)

# print(0o11)

# print(5 5)


# deprecated = "This feature is no longer used"
# print(deprecated)


#Excercise 1.2

# Start the Python interpreter and use it as a calculator.
#  1. Howmanyseconds are there in 42 minutes 42 seconds?
#  2. Howmanymiles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
#  3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per
#  mile in minutes and seconds)? What is your average speed in miles per hour

minutes = 42
seconds = 42

total_seconds = (minutes * 60) + seconds
print("total seconds",total_seconds)

# minutes = 42
# seconds = 42
# total_seconds = (minutes * 60) + seconds
# print(total_seconds)

# miles = 10
# kilometers = miles * 1.61
# print("kilometers",kilometers)

# km = 10
# miles = km * 1.61
# print("miles",miles)

# km = 10
# miles = km / 1.61
# print("miles",miles)

min = 42
sec=42
km = 10
miles = km/1.61
print("miles",miles)

total_time = (min +(sec/60)) /60
print("total time",total_time)

pace = (min + sec/60) / miles
print("pace",pace)

pace_min = int(pace)
pace_sec = round((pace-pace_min)*60)
print("pace in minutes and seconds",pace_min,pace_sec)

speed = miles / total_time
print("speed",speed)