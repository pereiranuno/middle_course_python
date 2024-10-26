import pandas as pd

def convert_tabular_file_content_to_dictionary(filename,registry_keys) -> list:
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