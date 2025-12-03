def by_age():
    while True:
        try:
            age = int(input("What is your age? "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if 0 < age < 10:
            print("Enjoy your childhood")
            break
        elif 10 <= age < 20:
            print("Happy teenagehood")
            break
        elif age >= 20:
            print("Congrats, you are an adult")
            break
        else:
            print("Please enter a positive number.")

# Call
if __name__ == "__main__":
    by_age()
