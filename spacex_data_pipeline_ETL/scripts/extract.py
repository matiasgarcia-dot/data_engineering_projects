import requests
import os
import json

def get_bronze_path(dataset):
    """
    Gets the path to save data in the Bronze layer.
    The Bronze layer is typically the raw data storage layer.
    """
    base_dir = os.path.join(os.getcwd(), "delta_lake_data", "bronze")
    return os.path.join(base_dir, dataset)

def extract_data_from_api(api_url, dataset_name):
    """
    Extracts data from the API and saves it in the Bronze layer.
    
    Parameters:
    - api_url: The URL of the API to fetch data from.
    - dataset_name: The name of the dataset, used to create the storage path.
    """
    # Send a GET request to the API URL
    response = requests.get(api_url)
    
    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Define the file path to save the data
        save_path = os.path.join(get_bronze_path(dataset_name), f"{dataset_name}.json")
        
        # Ensure the directory exists, creating it if necessary
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # Save the data to the specified path in JSON format
        with open(save_path, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data extracted and saved at: {save_path}")
    else:
        # Print an error message if the API request fails
        print(f"Error accessing the API: {response.status_code}")

if __name__ == "__main__":
    # Example API URLs for SpaceX rockets and launches
    rockets_api = "https://api.spacexdata.com/v4/rockets"
    launches_api = "https://api.spacexdata.com/v4/launches"

    # Extract data from the APIs and save it in the Bronze layer
    extract_data_from_api(rockets_api, "rockets")
    extract_data_from_api(launches_api, "launches")
