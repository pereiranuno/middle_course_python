import pandas as pd
from event import Event


class EventManager:
    def __init__(self, events):
        """
        Initialize an EventManager object with the given events.

        Parameters
        ----------
        events : list of dict
            A list of dictionaries with the following elements:
                - show: str
                - event: str
                - timestamp: int
                - user_id: int

        Returns
        -------
        None
        """
        self.events = []
        for event in events:
            show = event["show"]
            event_type = event["event"]
            timestamp = event["timestamp"]
            user_id = event["user_id"]
            self.events.append(Event(show, event_type, timestamp, user_id))
        self.events.sort(key=lambda x: x.timestamp)
        self.index = 0

    def __iter__(self):       
        """
        Returns an iterator object that allows iteration over the events.

        This method resets the index for iteration and returns the instance
        itself, which is iterable. It is automatically called when an iteration
        over the EventManager instance is initiated, making the instance ready
        to provide elements one by one through the use of the __next__ method.
        
        Returns
        -------
        self : EventManager
            The instance itself, which is iterable.
        """
        self.index = 0 
        return self

    def __next__(self):
        """
        Returns the next event in the sorted list of events.

        This method is automatically called when using a for loop or the
        next() function. It returns the next event in the sorted list of
        events, or raises StopIteration when the end of the list is reached.

        Returns
        -------
        Event: The next event in the sorted list of events.
        """
        if self.index < len(self.events):
            current_event = self.events[self.index]
            self.index += 1
            return current_event
        else:
            raise StopIteration

    def __getitem__(self, index):        
        if 0 <= index < len(self.events):
            return self.events[index]
        else:
            raise IndexError("Index out of range.")
        

    def __contains__(self, event):
        return event in self.events     

    def calculate_active_users_per_show(self):
        try:
            active_users_show = {}

            for event in self:
                if event.event == 'start':
                    if event.show not in active_users_show:
                        active_users_show[event.show] = set()
                    active_users_show[event.show].add(event.user_id)
                elif event.event == 'stop':
                    if event.show in active_users_show and event.user_id in active_users_show[event.show]:
                        active_users_show[event.show].remove(event.user_id)

            return active_users_show
        except Exception as e:
            print(f"Error calculating active users per show: {e}")
            return {}
        

    def active_users_per_show_generator(self):
        active_users_show = self.calculate_active_users_per_show()

        for show, users_list in active_users_show.items():
            yield (show, len(users_list))    

    def export_active_users_per_show(self, filename):
        try:

            data_generator = self.active_users_per_show_generator()
            shows = []
            active_users = []

            for show, user_count in data_generator:
                shows.append(show)
                active_users.append(user_count)

            # Converter os dados para um DataFrame
            data = {
                "Show": shows,
                "Active Users": active_users
            }

            df = pd.DataFrame(data)

            # Export the DataFrame to a CSV file
            df.to_csv(filename, index=False)
            print(f"Data successfully exported to {filename}")
        except Exception as e:
            print(f"Error exporting active users per show to file: {e}")