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
            self.events.append(Event(event["show"], event["event"], event["timestamp"], event["user_id"]))
        self.events.sort(key=lambda x: x.timestamp)
        self.index = 0

    def __iter__(self):       
        """
        Returns an iterator object that allows iteration over the events.

        This method resets the index for iteration and returns the instance
        itself, which is iterable.
        
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
        """
        Returns the event at the specified index.

        Parameters
        ----------
        index : int
            The index of the event to return.

        Returns
        -------
        Event
            The event at the specified index.

        Raises
        ------
        IndexError
            If the index is out of range.
        """
        if 0 <= index < len(self.events):
            return self.events[index]
        else:
            raise IndexError("Index out of range.")
        

    def __contains__(self, event):
        """
        Checks if an event is in the sorted list of events.

        Parameters
        ----------
        event : Event
            The event to check.

        Returns
        -------
        bool
            True if the event is in the sorted list of events, False otherwise.
        """
        return event in self.events     

    def calculate_active_users_per_show(self):
        """
        Calculates the active users for each show based on the events.

        This method iterates over the events and keeps track of active users
        for each show. A user is considered active if they have a 'start' event
        without a corresponding 'stop' event. The result is a dictionary where
        the keys are the show names and the values are sets of user IDs representing
        the active users.

        Returns
        -------
        dict
            A dictionary with shows as keys and sets of active user IDs as values.
            If an error occurs, an empty dictionary is returned.
        """
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
        """
        Yields a generator of tuples containing the show name and the number of active users for the show.

        This method is a generator that iterates over the result of calculate_active_users_per_show
        and yields a tuple for each show with the show name and the number of active users.

        Yields
        ------
        tuple
            A tuple containing the show name and the number of active users for the show.
        """
        active_users_show = self.calculate_active_users_per_show()

        for show, users_list in active_users_show.items():
            yield (show, len(users_list))    

    def export_active_users_per_show(self, filename):
        """
        Exports the active users per show to a CSV file.

        Parameters
        ----------
        filename : str
            The name of the file to export the data to.

        Returns
        -------
        None
        """
        try:

            data_generator = self.active_users_per_show_generator()
            shows = []
            active_users = []

            for show, user_count in data_generator:
                shows.append(show)
                active_users.append(user_count)

            data = {
                "Show": shows,
                "Active Users": active_users
            }

            df = pd.DataFrame(data)

            df.to_csv(filename, index=False)
            print(f"Data successfully exported to {filename}")
        except Exception as e:
            print(f"Error exporting active users per show to file: {e}")

  