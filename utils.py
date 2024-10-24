def convert_tabular_file_content_to_dictionary(filename,registry_fields) -> list:
    try:
        with open(filename, "r") as registry_tabular:
            registry_list = []
            for line in registry_tabular.readlines():
                line = line.strip().split("\t")
                registry = {}
                for i in range(len(registry_fields)):
                    registry[registry_fields[i]] = line[i] if registry_fields[i] == "show" or registry_fields[i] == "event" else int(line[i])
                registry_list.append(registry)
            return registry_list
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except ValueError as e:
        print(f"Error processing the file '{filename}': {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while reading the file '{filename}': {e}")
        return []