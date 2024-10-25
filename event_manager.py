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
        self.index = 0
        self.events.sort(key=lambda x: x.timestamp)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.events):
            current_event = self.events[self.index]
            self.index += 1
            return current_event
        else:
            raise StopIteration
        


    def calculate_active_users_per_show(self):
        try:
            active_users_show = {}

            for event in self.events:
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

    def export_active_users_per_show(self, filename):
        try:
            active_users = self.calculate_active_users_per_show()
            # Convert the active users data to a DataFrame
            data = {
                "Show": list(active_users.keys()),
                "Active Users": [len(users) for users in active_users.values()]
            }
            df = pd.DataFrame(data)

            # Export the DataFrame to a CSV file
            df.to_csv(filename, index=False)
            print(f"Data successfully exported to {filename}")
        except Exception as e:
            print(f"Error exporting active users per show to file: {e}")