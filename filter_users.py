import json


def filter_by_age(age):
    """Filter users by age."""
    try:
        age = int(age)
    except ValueError:
        print("Please enter a valid number for age.")
        return

    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user.get("age") == age_to_search]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print("No users found with that age.")


def filter_users_by_email(email):
    """Filter users by email."""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"].lower() == email.lower()]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print(f"No users found with email '{email}'.")


def filter_users_by_name(name):
    """Filter users by name."""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [
        user for user in users if user["name"].lower() == name.lower()
    ]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print(f"No users found with name '{name}'.")


if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? (name/age/email): "
    ).strip().lower()

    if filter_option == "age":
        age = input("Enter an age to filter users: ").strip()
        filter_by_age(age)

    elif filter_option == "email":
        email = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email)

    elif filter_option == "name":
        name = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name)

    else:
        print("Filtering by that option is not yet supported.")
