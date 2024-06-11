
# Task 1 

def name_len_checker():
    while True:
        first_name = input("Please enter your first name: ")

        if len(first_name)>= 2:
            print(f"Your first name is {len(first_name)} letters long.")
            break
        elif len(first_name) < 2:
            print("Error: First name is not long enough. Please try again")
            
    
    while True:
        last_name = input("Please enter your last name: ")

        if len(last_name)>= 2:
            print(f"Your last name is {len(last_name)} letters long.")
            break
        elif len(last_name) < 2:
            print("Error: Last name is not long enough. Please try again")
            
    print(f"Your full name is {first_name} {last_name}.")

# Task 2

def password_checker():
    while True:
        has_upper = False
        has_lower = False
        has_number = False

        pass_input = input("Please input your password:  ")

        if len(pass_input) < 8:
            print(f"Error: Your password must be at least 8 characters long.  Please try again.")
            continue

        for char in pass_input:
            if char.isupper():
                has_upper = True
            if char.islower():
                has_lower = True
            if char.isdigit():
                has_number = True

        if has_upper == False:
            print("Error: Password needs at least one upper case letter.  Please try again.")
            continue
        elif has_lower == False:
            print("Error: Password needs at least one lower case letter.  Please try again.")
            continue
        elif has_number == False:
            print("Error: Password needs at least one number.  Please try again.")
            continue
        else:
            print("That is a valid password!")
            

        break


# Task 3

def email_standardizer(database):

    first_name_input = input("Please enter your first name: ")
    last_name_input = input("Please enter your last name: ")
    tag = "@codingtemple.com"

    taken_counter = 1

    while True:

        email_address = first_name_input[0] + last_name_input + str(taken_counter) + tag

        if email_address not in database:
            break
        else:
            taken_counter += 1

    return print(f"Your email address is {email_address}!")


database = ["BPeloso1@codingtemple.com", "jim2@codingtemple.com"]

name_len_checker()
password_checker()
email_standardizer(database)



