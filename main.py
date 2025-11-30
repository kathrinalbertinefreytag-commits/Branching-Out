def by-age():
    while True:
    age = input("What is your age?")
    if age >0 < 10:
        print("Enjoy your childhood")
        break
    elif age >10 and age <20:
        print("Happay teenagehood")
        break
    elif age >20:
        print("Congrats you are an adult")
        break
    else:
        "Please enter a number"