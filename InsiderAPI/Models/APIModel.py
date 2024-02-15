import requests
import random

# Global variables
base_url = "https://petstore.swagger.io/v2/pet"

class APIModel:
    # Helper functions
    def create_pet(self, pet_data):
        response = requests.post(base_url, json=pet_data)
        return response


    def get_pet(self, pet_id):
        url = f"{base_url}/{pet_id}"
        response = requests.get(url)
        return response


    def update_pet(self, pet_id, new_pet_data):
        url = f"{base_url}/{pet_id}"
        response = requests.put(url, json=new_pet_data)
        return response


    def delete_pet(self, pet_id):
        url = f"{base_url}/{pet_id}"
        response = requests.delete(url)
        return response


    def pet_data(self):
        rndNumber = random.randint(1000, 9999)
        return {
            "id": rndNumber,
            "category": {"id": 1, "name": "dog"},
            "name": "Deneme",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available"
        }
