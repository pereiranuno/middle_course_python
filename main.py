
from event_manager import EventManager
from utils import convert_tabular_file_content_to_dictionary as convert_tsv_to_dict
import pandas as pd

if __name__ == "__main__":
    registry_list = convert_tsv_to_dict("events.tsv",registry_fields = ["show", "event", "timestamp", "user_id"])
    if registry_list:
        event_manager = EventManager(registry_list)
        event_manager.export_active_users_per_show("output.csv")

    # Tests using assert
    try:
        # Test 1: Check if events are read correctly from the file
        sample_registry = [
            {"show": "The Witcher", "event": "start", "timestamp": 0, "user_id": 1},
            {"show": "The Witcher", "event": "stop", "timestamp": 1, "user_id": 1}
        ]
        event_manager = EventManager(sample_registry)
        assert len(event_manager.events) == 2, "Test failed: Incorrect number of events in EventManager"

        # Test 2: Check active user calculation
        active_users = event_manager.calculate_active_users_per_show()
        assert active_users == {"The Witcher": set()}, "Test failed: Active users calculation is incorrect"

        # Test 3: Check export function (manual verification needed)
        event_manager.export_active_users_per_show("test_output.csv")
        df = pd.read_csv("test_output.csv")
        assert "The Witcher" in df["Show"].values, "Test failed: Export function did not output correctly"

        print("All tests passed successfully.")
    except AssertionError as e:
        print(e)
