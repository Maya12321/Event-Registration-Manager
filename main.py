from event_manager import EventManager

def main():
    print("Welcome to the Event Registration Manager")

    manager = EventManager()
   
    while True:
        print("        Menu        ")
        print("--------------------")
        print("1. Adding an event")
        print("2. Registering a participant")
        print("3. Cancelling a registration")
        print("4. Displaying all events")
        print("5. Searching for a participant")
        print("6. Saving data")
        print("7. Loading data")
        print("8. Exiting")
        print()

        choice = input("Please choose one of the options by number: ")
        
        match choice:
            case "1":
                event_id = input("Enter event ID: ")
                name = input("Enter event name: ")
                while True:
                    try: 
                        capacity = int(input("Enter event capacity: "))
                        break
                    except ValueError:
                        print("Error: Capacity should be a number.")
                
                success, message = manager.add_event(event_id, name, capacity)
                print(message)

            case "2":
                event_id = input("Enter event ID: ")
                event = manager.find_event(event_id)
                if event is None:
                    print("No event was found.")                
                else:
                    pid = input("Enter participant ID to register: ")
                    if pid not in manager.participants:
                        name = input("Enter participant name: ")
                    else:
                        name = manager.participants[pid]
                    success, message = event.register_participant(pid)
                    if success and pid not in manager.participants:
                        manager.participants[pid] = name
                    print(message)
                
            case "3":
                event_id = input("Enter event ID: ")
                event = manager.find_event(event_id)
                if event is None:
                    print("No event was found.")                
                else:
                    pid = input("Enter participant ID to cancel: ")
                    success, message = event.cancel_participant(pid)
                    print(message)

            case "4":
                manager.display_all_events()

            case "5":
                pid = input("Enter participant ID: ")
                manager.search_participants(pid)

            case "6":
                manager.save_data()

            case "7":
                manager.load_data()

            case "8":
                print("Goodbye!")
                break

            case _:
                print("Invalid input. Please enter a valid option.")

if __name__ == '__main__':
    main()
