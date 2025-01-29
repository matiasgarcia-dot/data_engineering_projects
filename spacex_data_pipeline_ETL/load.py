import os
import json

def get_silver_path(dataset):
    """
    Gets the path of the Silver layer.
    The Silver layer stores cleaned or transformed data.
    """
    return os.path.join(os.getcwd(), "delta_lake_data", "silver", dataset)

def get_gold_path(dataset):
    """
    Gets the path of the Gold layer.
    The Gold layer stores finalized, ready-to-use data.
    """
    return os.path.join(os.getcwd(), "delta_lake_data", "gold", dataset)

def load_data_to_gold(dataset_name):
    """
    Loads transformed data from the Silver layer into the Gold layer.
    
    Parameters:
    - dataset_name: The name of the dataset to be loaded into the Gold layer.
    """
    # Define paths for the Silver and Gold layers
    silver_path = os.path.join(get_silver_path(dataset_name), f"{dataset_name}_transformed.json")
    gold_path = os.path.join(get_gold_path(dataset_name), f"{dataset_name}_final.json")

    # Load the transformed data from the Silver layer
    with open(silver_path, "r") as file:
        data = json.load(file)

    # Simulate loading the data into the Gold layer (can be replaced with Delta Lake libraries)
    os.makedirs(os.path.dirname(gold_path), exist_ok=True)

    # Save the data into the Gold layer
    with open(gold_path, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data loaded into: {gold_path}")

if __name__ == "__main__":
    # Load the 'rockets' dataset into the Gold layer
    load_data_to_gold("rockets")
    
    # Load the 'launches' dataset into the Gold layer
    load_data_to_gold("launches")
