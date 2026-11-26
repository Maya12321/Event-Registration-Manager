import event
import json

class EventManager: 
    def __init__(self):
        self.events = {}
        self.participants = {}
    
    def add_event(self, event_id, name, capacity):
        # 1. Check if the event's ID already exists 
        if event_id in self.events:
            return False, "Error: event already exists."
        
        # 2. Check if the event's capacity is valid
        if capacity <= 0:
            return False, "Error: event capacity invalid."

        # 3. Create the new event and add to existing events
        ev = event.Event(event_id, name, capacity)
        self.events[event_id] = ev
        return True, "Event added successfully." 
    
    def find_event(self, event_id):
        if event_id in self.events: # check if the event exists by its ID
             return self.events[event_id] # if event exists return the event object 
        # if event doesn't exist auto return None
         
    def search_participants(self, pid):
        if pid in self.participants:
            name = self.participants[pid]
            confirmed = []
            waiting_list = []

            for event in self.events.values():
                if pid in event.confirmed:
                    confirmed.append(event)
                    
                if pid in event.waiting_list:
                    waiting_list.append(event)

            print(f"Participant: {name} ({pid}) \n")

            if not confirmed and not waiting_list:
                print("Participant isn't registered in any event.")

            if confirmed:
                print("Confirmed Events:")
                for event in confirmed:
                    print(f"{event.event_id} - {event.name}")
            
            if waiting_list:
                print("Waiting List:")
                for event in waiting_list:
                    print(f"{event.event_id} - {event.name}")
                
        else:
            print("Participant ID not found.")
        
    def display_all_events(self):
        if not self.events:
            print("No events available.")
        
        else:
            for event in self.events.values():
                print(f"Event ID: {event.event_id}")
                print(f"Name: {event.name}")
                print(f"Capacity: {event.capacity}")

                if event.confirmed:
                    print("Confirmed Participants: ", end = '')
                    for pid in event.confirmed:
                        if pid == event.confirmed[-1]:
                            print(self.participants[pid])
                        else:
                            print(self.participants[pid], end = ', ')
                else:
                    print("No confirmed participants for this event.")

                if event.waiting_list:
                    print("Waiting List: ", end = '')
                    for pid in event.waiting_list:
                        if pid == event.waiting_list[-1]:
                            print(self.participants[pid])
                        else:
                            print(self.participants[pid], end = ', ')
                else:
                    print("No waiting participants for this event.")

                print(f"Free Seats: {event.get_free_seats()}")
                print(f"Fill Percentage: {event.get_fill_percentage():.2f}%")
                print(f"---------------------------------")

    def save_data(self): 
        # preparing the data dictionary
        data = {
            "participants" : self.participants,
            "events" : []
        }
        # collecting and converting events' info
        for event in self.events.values():
            event_data = {
                "event_id": event.event_id,
                "name": event.name,
                "capacity": event.capacity,
                "confirmed": event.confirmed,
                "waiting_list": event.waiting_list
            }
            # append event_data
            data["events"].append(event_data)

        # saving data to the JSON file
        try:
            with open("data.json", "w") as file:
                json.dump(data, file, indent = 4)
        except PermissionError:
            print("The program has no permission to write to the file.")
        except OSError:
            print("Error in accessing or writing the file.")
        else:
            print("Data saved successfully!")


    def load_data(self):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
            
            self.events.clear()
            self.participants = data["participants"]

            for event in data["events"]:
                event_id = event["event_id"]
                name = event["name20"]
                capacity = event["capacity"]
                event_obj = event.Event(event_id, name, capacity)
                event_obj.confirmed = event["confirmed"]
                event_obj.waiting_list = event["waiting_list"]
                self.events[event_id] = event_obj
             
        except FileNotFoundError:
            print("File doesn't exist.")

        except json.JSONDecodeError:
            print("File invalid.")

        else:
            print("Data loaded successfully!")
