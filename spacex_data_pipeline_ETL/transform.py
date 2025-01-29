import os
import json

def get_bronze_path(dataset):
    """
    Gets the path of the Bronze layer.
    The Bronze layer is typically where raw data is stored.
    """
    return os.path.join(os.getcwd(), "delta_lake_data", "bronze", dataset)

def get_silver_path(dataset):
    """
    Gets the path of the Silver layer.
    The Silver layer is typically used for cleaned or transformed data.
    """
    return os.path.join(os.getcwd(), "delta_lake_data", "silver", dataset)

def transform_data(dataset_name, transform_function):
    """
    Transforms data from the Bronze layer and saves it in the Silver layer.
    
    Parameters:
    - dataset_name: The name of the dataset to be transformed.
    - transform_function: A function that defines how to transform the data.
    """
    # Define paths for the Bronze and Silver layers
    bronze_path = os.path.join(get_bronze_path(dataset_name), f"{dataset_name}.json")
    silver_path = os.path.join(get_silver_path(dataset_name), f"{dataset_name}_transformed.json")

    # Load data from the Bronze layer
    with open(bronze_path, "r") as file:
        data = json.load(file)

    # Apply the transformation function to the data
    transformed_data = transform_function(data)

    # Ensure the Silver layer directory exists, creating it if necessary
    os.makedirs(os.path.dirname(silver_path), exist_ok=True)

    # Save the transformed data in the Silver layer
    with open(silver_path, "w") as file:
        json.dump(transformed_data, file, indent=4)
    print(f"Transformed data saved at: {silver_path}")

if __name__ == "__main__":
    def sample_transformation(data):
        """
        Example of a transformation function.
        Filters data to include only the 'id' and 'name' fields.
        
        Parameters:
        - data: The raw data loaded from the Bronze layer.
        
        Returns:
        - A list of dictionaries containing only the 'id' and 'name' fields.
        """
        return [{"id": item.get("id"), "name": item.get("name")} for item in data]

    # Transform and save the 'rockets' dataset
    transform_data("rockets", sample_transformation)
    
    # Transform and save the 'launches' dataset
    transform_data("launches", sample_transformation)
