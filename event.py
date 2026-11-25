class Event:
    def __init__(self, event_id, name, capacity):
        self.event_id = event_id
        self.name = name
        self.capacity = capacity
        self.confirmed = []
        self.waiting_list = []

    def register_participant(self, pid):
        # 1. Check if person is already signed up
        if pid in self.confirmed or pid in self.waiting_list:
            return False, "Error: Already registered."
        
        # 2. If there are free seats, add to confirmed
        if len(self.confirmed) < self.capacity:
            self.confirmed.append(pid)
            return True, "Success: Added to confirmed seats."
        
        # 3. Otherwise, add to the waiting list
        else:
            self.waiting_list.append(pid)
            return True, "Notice: Added to waiting list."

    def cancel_participant(self, pid):
        # If they are in confirmed, remove them and move someone up
        if pid in self.confirmed:
            self.confirmed.remove(pid)
            
            # If people are waiting, move the first one to confirmed
            if len(self.waiting_list) > 0:
                next_person = self.waiting_list.pop(0)
                self.confirmed.append(next_person)
                
            return True, "Participant removed from confirmed."
        
        # If they are in the waiting list, just remove them
        elif pid in self.waiting_list:
            self.waiting_list.remove(pid)
            return True, "Participant removed from waiting list."
        
        return False, "Error: Participant not found."

    def get_free_seats(self):
        return self.capacity - len(self.confirmed)

    def get_fill_percentage(self):
        if self.capacity == 0:
            return 0
        return (len(self.confirmed) / self.capacity) * 100