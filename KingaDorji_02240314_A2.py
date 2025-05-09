import random

def guess_number_game():
    number = random.randint(1, 10)
    Score = 0
    while True:
        try:
            guess = int(input("Guess any number between 1 to 10: "))
            if guess == number:
                print("well! You guessed it correctly")
                Score += 1

            else:
                print("You Guessed WRONG number") 
            print(f"Score: {Score}")

            break
        except ValueError:
            print("enter valid number")


def rock_paper_scissor_game():
    choices = ["rock", "paper", "scissor"]
    computer_choice = random.choice(choices)
    score = 0
    while True:
        try:
            user_input = input("enter your choice:(rock, paper, scissor)")

            if user_input == computer_choice:
                print("Blast")
            elif (user_input == "rock" and computer_choice == "scissor") or \
                 (user_input == "paper" and computer_choice == "rock") or \
                 (user_input == "scissor" and computer_choice == "paper"):
                print("You Win")
                score += 1
            else:
                print("You Lose")
            print(f"Score: {score}")
            break
        except ValueError:
            print("Give Valid Input")

def trivia_quiz_game():
    score = 0
    questions = [
        {
            "question": "What is the capital of Bhutan?",
            "options": ["A. Thimphu", "B. Paro", "C. Punakha", "D. Trongsa"],
            "answer": "A"
        },
        {
            "question": "What is the Name of First King of Bhutan?",
            "options": ["A. Gongsa Ugyen Wangchuck", "B. Jigme Namgyal", "C. Jigme Singye Wangchuck", "D. Jigme Dorji Wangchuck"],
            "answer": "A"
        },
        {
            "question": "What is the National Bird of India?",
            "options": ["A. Crow", "B. Eagle", "C. Sparrow", "D. Peacock"],
            "answer": "D"  # Corrected the answer to Peacock
        },
        {
            "question": "Who is the present Prime Minister of Bhutan?",
            "options" : ["A. Lotay Tshering", "B. Jigme Y Thinley", "C. Tshering Tobgye", "D. Lyonchen Thinley Wanchuk"],
            "answer": "A"  # Assuming this is the correct answer
        },
    ]
    
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            print(option)
        answer = input("enter your choice(A, B, C, D): ").upper()
        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect:")
    print(f"Your Final Score: {score}/{len(questions)}")


def pokemon_card_binder_manager():
    # Initialize the binder data structure
    # Using a dictionary to store Pokemon cards with Pokedex number as key
    binder = {}
    MAX_POKEDEX_NUMBER = 1025
    CARDS_PER_PAGE = 64
    ROWS_PER_PAGE = 8
    COLS_PER_PAGE = 8
    
    print("Welcome to Pokemon Card Binder Manager!")
    
    while True:
        print("\nMain Menu:")
        print("1. Add Pokemon card")
        print("2. Reset binder")
        print("3. View current placements")
        print("4. Exit")
        
        option = input("Select option: ")
        
        if option == "1":
            # Add Pokemon card
            try:
                pokedex_num = int(input("Enter Pokedex number: "))
                
                # Validate Pokedex number
                if pokedex_num < 1 or pokedex_num > MAX_POKEDEX_NUMBER:
                    print(f"Invalid Pokedex number. Please enter a number between 1 and {MAX_POKEDEX_NUMBER}.")
                    continue
                
                # Check if card already exists
                if pokedex_num in binder:
                    page = binder[pokedex_num]["page"]
                    row = binder[pokedex_num]["row"]
                    col = binder[pokedex_num]["col"]
                    print(f"Output:\nPage: {page}\nPosition: Row {row}, Column {col}\nStatus: Pokedex #{pokedex_num} already exists in binder")
                else:
                    # Calculate position based on sequential placement
                    # The position is determined by the Pokedex number
                    position = pokedex_num
                    page = ((position - 1) // CARDS_PER_PAGE) + 1
                    position_on_page = (position - 1) % CARDS_PER_PAGE
                    row = (position_on_page // COLS_PER_PAGE) + 1
                    col = (position_on_page % COLS_PER_PAGE) + 1
                    
                    # Add card to binder
                    binder[pokedex_num] = {
                        "page": page,
                        "row": row,
                        "col": col
                    }
                    
                    print(f"Output:\nPage: {page}\nPosition: Row {row}, Column {col}\nStatus: Added Pokedex #{pokedex_num} to binder")
                    
                    # Check if collection is complete
                    if len(binder) == MAX_POKEDEX_NUMBER:
                        print("You have caught them all!!")
            except ValueError:
                print("Please enter a valid number.")
                
        elif option == "2":
            # Reset binder
            print("WARNING: This will delete ALL Pokemon cards from the binder.")
            print("This action cannot be undone.")
            confirmation = input("Type 'CONFIRM' to reset or 'EXIT' to return to the Main Menu: ")
            
            if confirmation == "CONFIRM":
                binder = {}
                print("The binder reset was successful! All cards have been removed.")
            elif confirmation == "EXIT":
                continue
            else:
                print("Invalid input. Returning to Main Menu.")
                
        elif option == "3":
            # View current placements
            print("Current Binder Contents:")
            print("-------------------------")
            
            if not binder:
                print("The binder is empty.")
            else:
                # Sort by Pokedex number for display
                for pokedex_num in sorted(binder.keys()):
                    card = binder[pokedex_num]
                    print(f"Pokedex #{pokedex_num}:  Page: {card['page']}  Position: Row {card['row']}, Column {card['col']}")
            
            print("-------------------------")
            print(f"Total cards in binder: {len(binder)}")
            completion_percentage = (len(binder) / MAX_POKEDEX_NUMBER) * 100
            print(f"% completion: {completion_percentage:.1f}%")
            
        elif option == "4":
            # Exit
            print("Thank you for using Pokemon Card Binder Manager!")
            # Return the score (number of cards in binder)
            return len(binder)
        else:
            print("Invalid option. Please try again.")


def menu_display():
    print("\nGame Menu")
    print("1. Guessing Game")
    print("2. Rock paper scissor game")
    print("3. Trivia Quiz Game")
    print("4. Pokemon Card Binder Manager")
    print("5. Exit")

    choice = input("Enter your choice:")
    return choice


def main():
    while True:
        
        choice = menu_display()
        if choice == '1':
            guess_number_game()
        elif choice == '2':
            print("Rock paper scissor Gameplay")
            rock_paper_scissor_game()
        elif choice == '3':
            print("Trivia Gameplay")
            trivia_quiz_game()
        elif choice == '4':
            print("Pokemon Card Binder Manager")
            score = pokemon_card_binder_manager()
            print(f"Your final score: {score}")
        elif choice == '5':
            print("Game Exit")
            break
        else:
            print("Error Occured")
        

if __name__ == "__main__":
   main()
