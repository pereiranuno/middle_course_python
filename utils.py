import pandas as pd

def convert_tabular_file_content_to_dictionary(filename,registry_keys) -> list:
    """
    Converts a tabular file content to a list of dictionaries.

    Args:
        filename (str): The file to read.
        registry_keys (list): The keys to use for the dictionaries.

    Returns:
        list: A list of dictionaries, where each dictionary represents a row in the file.
    """
    
    try:  
        df = pd.read_csv(filename, sep="\t", header=None)
        df.columns = registry_keys
        return(df.to_dict(orient="records"))
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except ValueError as e:
        print(f"Error processing the file '{filename}': {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while reading the file '{filename}': {e}")
        return []