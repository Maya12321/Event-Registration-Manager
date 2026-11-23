from event_manager import EventManager

def main():
    print("Welcome to the Event Registration Manager")
   
    while True:
        print("        Menu        ")
        print("--------------------")

        print("1. Adding an event \n 2. Registering a participant \n" \
        "3. Cancelling a registration \n 4. Displaying all events \n " \
        "5. Searching for a participant \n 6. Saving data \n 7. Loading data " \
        "\n 8. Exiting \n")

        choice = input("Please choose one of the options by number: ")
        
        match choice:
            case "1":

            case "2":

            case "3":

            case "4":

            case "5":

            case "6":

            case "7":

            case "8":
                break

            case _:
                print("Invalid input. Please enter a valid option.")

if __name__ == '__main__':
    main()
