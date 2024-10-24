class Event:
    def __init__(self, show, event, timestamp, user_id):
        """
        Initialize an Event object with given show, event, timestamp, and user_id

        Parameters
        ----------
        show : str
            The name of the show
        event : str
            The type of event (start or stop)
        timestamp : int
            The timestamp of the event
        user_id : int
            The ID of the user
        """
        self.show = show
        self.event = event
        self.timestamp = timestamp
        self.user_id = user_id