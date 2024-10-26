from event_manager import EventManager
from utils import convert_tabular_file_content_to_dictionary as convert_tsv_to_dict
import pandas as pd
import matplotlib.pyplot as plt


def test_application(graph_type_output):
   # Tests using assert and store results in a dictionary
    """
    Runs unit tests on the EventManager class and its methods.

    :param graph_type_output: The type of graph to output the test results in.
        Currently supports "plot_bar" only.

    :return: None
    """

    test_results = {}
    try:
        # Test 1: Check if events are passed correctly on EventManager initialization
        test_registry = [
            {"show": "The Witcher", "event": "start", "timestamp": 0, "user_id": 1},
            {"show": "The Witcher", "event": "stop", "timestamp": 1, "user_id": 1}
        ]
        event_manager = EventManager(test_registry)
        assert len(event_manager.events) == 2, "Test failed: Incorrect number of events in EventManager"
        test_results["Test - EventManager initialization"] = "Passed"
    except AssertionError as e:
        test_results["Test - EventManager initialization"] = str(e)

    try:
        # Test 2: Check active user calculation
        active_users = event_manager.calculate_active_users_per_show()
        assert active_users == {"The Witcher": set()}, "Test failed: Active users calculation is incorrect"
        test_results["Test - Active user calculation"] = "Passed"
    except AssertionError as e:
        test_results["Test - Active user calculation"] = str(e)

    try:
        # Test 3: Check export function output
        event_manager.export_active_users_per_show("test_output.csv")
        df = pd.read_csv("test_output.csv")
        assert "The Witcher" in df["Show"].values, "Test failed: Export function did not output correctly"
        test_results["Test - Export function output"] = "Passed"
    except AssertionError as e:
        test_results["Test - Export function output"] = str(e)

    # Graph test results
    try:
        test_names = list(test_results.keys())
        test_outcomes = [1 if result == "Passed" else 0 for result in test_results.values()]
        if graph_type_output == "plot_bar":
            plt.figure(figsize=(10, 6))
            plt.bar(test_names, test_outcomes, color=['green' if outcome == 1 else 'red' for outcome in test_outcomes])
            plt.xlabel('Test Name')
            plt.ylabel('Outcome (1 = Passed, 0 = Failed)')
            plt.title('Test Results Overview')
            plt.ylim(0, 1.5)
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            plt.show()
    except Exception as e:
        print(f"Error creating graph for test results: {e}")

    # Print the results
    for test, result in test_results.items():
        print(f"{test}: {result}")

#************************Main Program************************
if __name__ == "__main__":
    registry_list = convert_tsv_to_dict("events.tsv",registry_keys = ["show", "event", "timestamp", "user_id"])
    if registry_list:
        event_manager = EventManager(registry_list)
        event_manager.export_active_users_per_show("output.csv")
        test_application('plot_bar')

 