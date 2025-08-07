HISTORY_FILE = "history.txt"
def show_history():
    with open(HISTORY_FILE, "r") as file:
        lines = file.readlines()
        if len(lines) == 0:
            print("No history available.")
        else:
            for line in lines:
                print(line.strip())

def clear_history():
    with open(HISTORY_FILE, "w") as file:
        print("History cleared.")

def save_to_history(equation, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(equation + " = " + str(result) + "\n")

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Please enter in the format: number1 operator number2")
        return
    num1 = float(parts[0])
    num2 = float(parts[2])
    op = parts[1]

    if op == "+":
        result = num1 + num2
    elif op == "-":             
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
            result = num1 / num2
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return
        
    if int(result) == result:
        result = int(result)
    print(f'Result : {result}')
    save_to_history(user_input, result)

        
def main():
    print("-----SIMPLE CALCULATOR WITH HISTORY-----")
    while True:
        user_input = input("Enter the calculation (+,-,*,/) or Command (history, clear, exit) : ").lower()

        if user_input == "exit":
            print("Thank for using the calculator!")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
            print("History cleared.")
        else:
            calculate(user_input)

main()
