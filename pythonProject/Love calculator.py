import random

# Function to calculate the love score
def love_calculator(name1, name2):
    # Convert both names to lowercase to avoid case-sensitive comparison
    name1 = name1.lower()
    name2 = name2.lower()

    # Combine the names together into one string
    combined_names = name1 + name2

    # Calculate a "love score" by counting the number of vowels in the combined names
    vowels = "aeiou"
    love_score = 0
    for char in combined_names:
        if char in vowels:
            love_score += 1

    # The love score will be between 0 and 100 (we can use randomization to make it more fun)
    love_score = random.randint(50, 100) if love_score < 50 else love_score

    # Return the score and a message
    if love_score > 80:
        return f"Your love score is {love_score}%! 💖 You two are made for each other!"
    elif love_score > 40:
        return f"Your love score is {love_score}%! ❤️ There's a good connection!"
    else:
        return f"Your love score is {love_score}%! 💔 It might need some work!"

# Main function
def main():
    # Take inputs from the user
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")

    # Calculate the love score
    result = love_calculator(name1, name2)

    # Display the result
    print(result)

# Run the program
if __name__ == "__main__":
    main()
