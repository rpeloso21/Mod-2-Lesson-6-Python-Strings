# Task 1

def command_parser():
    command_input = input("Please input a command: ")

    if "help" in command_input:
        print("I can help... What do you need help with?")

    elif "issue" in command_input:
        print("I understand that you're having an issue.")

        # Task 2
        
        issue_input = input("Please further explain your issue: ")
        if "login" in issue_input:
            print("I understand that you are having a login issue.  I can get you to someone who can help you with that.")
        elif "performance" in issue_input:
            print("I understand that you are having a performance issue.  I can get you to someone who can help you with that.")
        elif "error" in issue_input:
            print("I understand that you are having an error issue.  I can get you to someone who can help you with that.")
            
    elif "contact support" in command_input:
        print("Here are the contact methods for our support team: ph. email... ")

    

command_parser()