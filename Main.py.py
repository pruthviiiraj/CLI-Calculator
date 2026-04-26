def calculate(number_one, number_two, operation):

    if operation == "+":
        return number_one + number_two

    elif operation == "-":
        return number_one - number_two

    elif operation == "*":
        return number_one*number_two

    elif operation == "/":
        if number_two == 0:
            return None

        else:
            return number_one/number_two

    else:        
        return None
    


history = []
running = True
while running: 
    try: 
        number_one = float(input("Enter the first number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

        continue
    
    while True: 
        operation = input("Select an operation to perform: +, -, *, /").strip()
        if operation not in ["+", "-", "*", "/"]:
            print("Invalid option, choose from +, -, *, /")
            continue
        try: 
            number_two = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

            continue
        
        result = calculate(number_one, number_two, operation)
        if result is None:
            print("Invalid operation or division by zero")
            continue

        print(f"Result: {result}")
        print()

        entry = f"{number_one} {operation} {number_two} = {result}"
        history.append(entry)


        choice = input("1: Continue with the result | 2: New values | 3: History | 4: Exit ").strip()

        if choice == "1":
            number_one = result

        elif choice == "2":
            break   
        
        elif choice == "3":
            if not history:
                print("No history yet")
            else:
                for item in history:
                    print(item)
                print()

        elif choice == "4":
            running = False
            break  

        else:
            print("Invalid choice")