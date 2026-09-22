
print("Welcome to the Data Analyzer and Transformer Program")

data = []
total_values = 0

def input_data():
    global data, total_values

    try:
        values = input("Enter data separated by commas: ")

        if values.strip() == "":
            print("Please enter some data.")
            return

        values = values.replace(",", " ")
        data = list(map(int, values.split()))
        total_values = len(data)

        print("Data has been stored successfully!")
        print("Your Data:", data)

    except ValueError:
        print("Invalid input! Please enter numbers only.")


def display_summary():
    print("\nData Summary:")
    print("Total elements:", len(data))
    print("Minimum value:", min(data))
    print("Maximum value:", max(data))
    print("Sum of all values:", sum(data))

    average = sum(data) / len(data)
    print("Average value:", round(average, 2))


def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def calculate_factorial():
    try:
        number = int(input("Enter a number to calculate its factorial: "))

        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print("Factorial of", number, "is:", factorial(number))

    except ValueError:
        print("Invalid input! Please enter a whole number.")


def filter_data():
    try:
        threshold = int(input("Enter a threshold value: "))

        result = list(filter(lambda x: x >= threshold, data))

        print("Filtered Data:", result)

    except ValueError:
        print("Invalid threshold value.")


def sort_data():
    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Sorted Data in Ascending Order:")
        print(sorted(data))

    elif choice == "2":
        print("Sorted Data in Descending Order:")
        print(sorted(data, reverse=True))

    else:
        print("Invalid choice.")


def show_statistics():
    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total / len(data)

    print("\nDataset Statistics:")
    print("Minimum value:", minimum)
    print("Maximum value:", maximum)
    print("Sum of all values:", total)
    print("Average value:", round(average, 2))


while True:
    print("\nMain Menu")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")

    choice = input("Please enter your choice: ")

    if choice == "1":
        input_data()

    elif choice == "2":
        if len(data) == 0:
            print("Please enter data first.")
        else:
            display_summary()

    elif choice == "3":
        calculate_factorial()

    elif choice == "4":
        if len(data) == 0:
            print("Please enter data first.")
        else:
            filter_data()

    elif choice == "5":
        if len(data) == 0:
            print("Please enter data first.")
        else:
            sort_data()

    elif choice == "6":
        if len(data) == 0:
            print("Please enter data first.")
        else:
            show_statistics()

    elif choice == "7":
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

    continue