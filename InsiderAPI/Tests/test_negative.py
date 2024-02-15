
import pytest
from Models.APIModel import APIModel

class TestNegative:
    model = APIModel()

    def test_create_pet_invalid_data(self):
        # Try to create a pet with invalid data
        invalid_pet_data = {"name": ""}  # Missing required fields
        response = self.model.create_pet(invalid_pet_data)
        print(response.json())
        assert response.status_code == 400

    def test_update_nonexistent_pet(self):
        # Try to update a pet that does not exist
        pet_id = 999999
        new_name = "Max"
        updated_pet_data = {"name": new_name}
        response = self.model.update_pet(pet_id, updated_pet_data)
        assert response.status_code == 405

    def test_delete_nonexistent_pet(self):
        # Try to delete a pet that does not exist
        pet_id = 999999
        response = self.model.delete_pet(pet_id)
        assert response.status_code == 404

    def test_get_nonexistent_pet(self):
        response = self.model.get_pet(999999)
        assert response.status_code == 404



