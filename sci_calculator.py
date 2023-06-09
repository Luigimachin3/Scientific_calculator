# Lab 03 - Scientific Calculator by Luis Martinez

# Import math library that will be used later for logarithm
import math
# Execute the code of block until the user enters 0 to exit the program
continue_calculator = True
# Loop intended to prompt the user for the next menu option without redisplay the main menu
no_menu = True
# Assign to the results of mathematical operations the variable current_result and give it an initial value of 0.0
current_result = 0.0
# Give the sum of the calculations an initial value of zero that will later change and update
sum_calculations = 0
# Give the number of the calculations an initial value of zero that will later change and update
number_calculations = 0

while continue_calculator:
    print(f"Current Result: {current_result}\n")
    # Display a menu and prompt the user to enter a menu option
    print("Calculator Menu\n"
          "---------------\n"
          "0. Exit Program\n"
          "1. Addition\n"
          "2. Subtraction\n"
          "3. Multiplication\n"
          "4. Division\n"
          "5. Exponentiation\n"
          "6. Logarithm\n"
          "7. Display Average")

    while no_menu:
        print("Enter Menu Selection: ", end="")
        # Read the chosen option
        user_choice = int(input())
        # Output a result whenever the choice is between 1 and 6
        if 1 <= user_choice <= 6:
            # Prompt the user for two numbers and read them
            print("Enter first operand: ", end="")
            first_operand = float(input())
            print("Enter second operand: ", end="")
            second_operand = float(input())
            print()
            # Add the operands and store the result in the variable user_choice if input is 1
            if user_choice == 1:
                current_result = first_operand + second_operand
            # Subtract the operands and store the result in the variable user_choice if input is 2
            elif user_choice == 2:
                current_result = first_operand - second_operand
            # Multiply the operands and store the result in the variable user_choice if input is 3
            elif user_choice == 3:
                current_result = first_operand * second_operand
            # Divide the operands and store the result in the variable user_choice if input is 4
            elif user_choice == 4:
                if second_operand != 0:
                    # Divide the operands only if the second operand is other than zero
                    current_result = first_operand / second_operand
                else:
                    # Print an error if second_operand is zero
                    print("Error: Cannot divide by zero!")
            # Exponentiation with first operand as the base and the second operand as the exponent (when input is 5)
            elif user_choice == 5:
                # Store the result in the variable user_choice
                current_result = first_operand ** second_operand
            # Logarithm with first operand as the base and the second operand as the yield (when input is 6)
            elif user_choice == 6:
                # Use math library for logarithm operation, and store the result in the variable user_choice
                current_result = math.log(second_operand, first_operand)
            # Update sum of calculations
            sum_calculations += current_result
            # Update number of calculations
            number_calculations += 1
            # The no_menu loop is immediately terminated and goes back to continue_calculator loop to display the
            # current result and the menu
            break
        # Exit the program if the input is zero
        elif user_choice == 0:
            # Say goodbye and terminate all loops to completely exit the program
            print("\nThanks for using this calculator. Goodbye!")
            no_menu = False
            continue_calculator = False
        # Display the sum of calculations, number of calculations, and average of calculations when input is 7.
        elif user_choice == 7:
            # Only display the average if at least one calculation has been completed.
            if number_calculations == 0:
                # If the number of calculations is zero, do not show the statistics but print an error message
                print("Error: No calculations yet to average!\n")
            else:
                print(f"\nSum of calculations: {sum_calculations}")
                print(f"Number of calculations: {number_calculations}")
                print(f"Average of calculations: {(sum_calculations / number_calculations):.2f}")
        else:
            # Alerts the user of an invalid selection and prompts for another choice
            print("\nError: Invalid selection!\n")
