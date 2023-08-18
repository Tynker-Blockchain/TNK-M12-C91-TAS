import hashlib
import random

# Declare difficultyLevel variable and add data to it using user input
difficultyLevel = int(input("Set Difficulty Level: "))

# Loop infinitely
while True:
    # Generate a random string and store it in randomString variable
    randomString = str(random.random()).encode('utf-8')

    # Create a hash object and store it in hashObject variable
    hashObject = hashlib.sha256()

    # Update the hash object with the random string using update() method
    hashObject.update(randomString)

    # Get the hexadecimal representation of the hash and store it in hashResult variable
    hashResult = hashObject.hexdigest()

    # Check if the first two characters of the hash are "0"
    if hashResult[:difficultyLevel] == "0" * difficultyLevel:
        
        # Print the hashResult
        print(hashResult)
        # Exit the loop if the condition is met
        break

