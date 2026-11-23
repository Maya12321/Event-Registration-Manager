import event
class EventManager: 
    def __init__(self):
        self.events = {}
        self.participants = {}
    
    def add_events(self, event_ID, name, capacity):
        # 1. Check if the event's ID already exists 
        if event_ID in self.events:
            return False, "Error: event already exists."
        
        # 2. Check if the event's capacity is valid
        if capacity <= 0:
            return False, "Error: event capacity invalid."

        # 3. Create the new event and add to existing events
        event = Event(event_ID, name, capacity)
        self.events[event_ID] = event
        return True, "Event added successfully." 
    
    def find_event(self, event_ID):
        # Check if the event's ID already exists
        # if it exists then return the event asked for
         if event_ID in self.events:  
             return True, self.events[event_ID]
        
        # Otherwise return none
         else:
             return None
         
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
        
    def display_all_events(self, ):

    def save_data():

    def load_data():

    
