import pandas as pd
import matplotlib.pyplot as plt
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

    def graph_active_users_per_show(self,graph_type):
        """
        Plot the number of active users per show using matplotlib.

        This method uses the calculated data from active users per show and 
        plots it in a bar chart for easy visualization.

        Returns
        -------
        None
        """
        try:
            # Use the generator to get the data
            data_generator = self.active_users_per_show_generator()
            shows = []
            active_users = []

            for show, user_count in data_generator:
                shows.append(show)
                active_users.append(user_count)
            if graph_type == "plot_bar":
                # Plotting the bar chart
                plt.figure(figsize=(10, 6))
                plt.bar(shows, active_users)
                plt.xlabel('Show')
                plt.ylabel('Number of Active Users')
                plt.title('Number of Active Users per Show')
                plt.xticks(rotation=45, ha="right")
                plt.tight_layout()
                plt.show()

            elif graph_type == "plot_pie":
                # Plotting the pie chart
                plt.figure(figsize=(10, 6))
                plt.pie(active_users, labels=shows, autopct='%1.1f%%', startangle=140)
                plt.title('Proportion of Active Users per Show')
                plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                plt.show()

        except Exception as e:
            print(f"Error creatting graph of active users per show: {e}")
