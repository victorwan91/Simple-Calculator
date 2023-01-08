# Print welcome message.
print("Welcome to Simple Calculator!")

# While loop starts, while True:
while True:

    # Request user to make a choice of 3 options and store in "options".
    options = input("Enter '1' to start calculation, '2' to read the file, '3' to exit the programme: ")

    # If user's input is "1" in options, calculator will be activated.
    if options == "1":

        # Request for 2 number inputs as float and an operator choice and put them in the try block.
        try:
            num1 = float(input("Number 1: "))
            num2 = float(input("Number 2: "))
            operator = input("Choose an operator (+, -, x, /): ")

            # Open a file called "equations.txt" for appending and store in "file"
            with open("equations.txt", "a+") as file:

                # If user chose "+" in operator, "num1" add "num2" and store in "add".
                # Print the result and write the equation and answer to the file.
                if operator == "+":
                    add = num1 + num2
                    print(add)
                    file.write(f"{num1} + {num2} = {add}\n")

                # If user chose "-" in operator, "num1" minus "num2" and store in "minus".
                # Print the result and write the equation and answer to the file.
                elif operator == "-":
                    minus = num1 - num2
                    print(minus)
                    file.write(f"{num1} - {num2} = {minus}\n")

                # If user chose "x" in operator, "num1" times "num2" and store in "multiply".
                # Print the result and write the equation and answer to the file.
                elif operator == "x":
                    multiply = num1 * num2
                    print(multiply)
                    file.write(f"{num1} x {num2} = {multiply}\n")

                # If user chose "/" in operator,
                elif operator == "/":

                    # Under try block, "num1" divided by "num2" and store in "divide".
                    # Print the result and write the equation and answer to the file.
                    try:
                        divide = num1 / num2
                        print(divide)
                        file.write(f"{num1} / {num2} = {divide}\n")

                    # If number is divided by 0, except ZeroDivisionError, print error message.
                    except ZeroDivisionError:
                        print("0 cannot be divided!")

        # If the input is not 1, 2 or 3, except ValueError and print error message.
        except ValueError:
            print("Invalid input! Try again!")

    # Elif user's input is "2" in "options", ask user to input a file name they want to view.
    elif options == "2":
        file_name = input("Enter the name of the file you want to view (e.g xxxx.txt): ")

        # Under try block, open file of user's choice and print each equation on a new line for them to read.
        try:
            with open(file_name, "r") as file1:
                lines = file1.readlines()
                for line in lines:
                    print(line)

            # If file is found, ask if user want save and view the file in the new file by entering Y/N under try block.
            try:
                file_choice = input("Do you want to save and view in the new file (Y/N)? ")

                # If the input is "y" converted to lowercase. Ask user to enter a new file name in "new_filename"
                # Transfer equations from the old file "old_file" to the new file "new_file" named by the user.
                # Display the equations on separated lines.
                if file_choice.lower() == "y":
                    new_filename = input("Enter a new file name: ")
                    with open(file_name, "r") as old_file, open(new_filename, "a") as new_file:
                        for line in old_file:
                            new_file.write(line)
                            print(line)

                # If the choice is "n" converted to lowercase, pass and return to main menu.
                elif file_choice.lower() == "n":
                    pass

                # Else, print error message of wrong input.
                else:
                    print("Invalid input, please enter Y or N.")

            # Except ValueError, print error message of wrong input.
            except ValueError:
                print("Invalid input, Please enter Y or N.")

        # Except FileNotFoundError if the file does not exist, then print error message.
        except FileNotFoundError:
            print("File does not exist.")

    # Elif user's input in "options" is "3", print goodbye message and exit the menu using exit().
    elif options == "3":
        print("Thank You for using Simple Calculator, Goodbye!")
        exit()

    # If the input is not 1, 2 or 3,  print error message.
    else:
        print("Invalid input! Try again!")
