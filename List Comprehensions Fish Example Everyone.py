fish = "halibut"
# Loop through each letter in the string and push to an array
letters = [] #[] means it's an empty list
for letter in fish:
    letters.append(letter) #prints it out, add it to a list

print(letters)

#List comprehensions provide concise syntax for creating lists
letters = [letter for letter in fish] # the for and in inside the script 
#creates a for loop in one line of code
print(letters)

#We can manipulate each element as we go
capital_letters = []
for letter in fish:
    capital_letters.append(letter.upper()) #upper() function turns all letters to uppercase

    #List comprehension for the above
    capital_letters = [letter.upper() for letter in fish]

    print(capital_letters)

    #We can also add conditional logic (if statements) to a list comprehension
    july_temperatures = [87,85, 92, 79, 106]
    hot_days = []
    for temperature in july_temperatures:
        if temperature >90:   #if the temperature is greater than 90, add it to the hot days list
            hot_days.append(temperature)
    print(hot_days)

    # hot_days: [92, 106]
    # list comprehension with conditional
    hot_days = [temperature for temperature in july_temperatures if temperature > 90]
    print(hot_days)