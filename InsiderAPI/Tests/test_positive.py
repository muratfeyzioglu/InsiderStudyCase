import pytest

from Models.APIModel import APIModel



class TestPositive:

    model = APIModel()

    def test_create_pet(self):
        pet_data = self.model.pet_data()
        response = self.model.create_pet(pet_data)
        print(response.json())
        assert response.status_code == 200
        assert response.json()["id"] == pet_data["id"]

    def test_get_existing_pet(self):
        pet_data = self.model.pet_data()
        self.model.create_pet(pet_data)
        response = self.model.get_pet(pet_data["id"])
        print(response.json())

        assert response.status_code == 200
        assert response.json()["id"] == pet_data["id"]


    def test_update_pet(self):
        pet_data = self.model.pet_data()
        self.model.create_pet(pet_data)

        new_name = "Max"
        updated_pet_data = pet_data.copy()
        updated_pet_data["name"] = new_name

        pet_id = pet_data["id"]
        response = self.model.update_pet(pet_data["id"], updated_pet_data)

        assert response.status_code == 200
        assert response.json()["name"] == new_name


    def test_delete_pet(self):
        pet_data = self.model.pet_data()
        self.model.create_pet(pet_data)
        response = self.model.delete_pet(pet_data["id"])
        assert response.status_code == 200

        response = self.model.get_pet(pet_data["id"])
        assert response.status_code == 404


    if __name__ == "__main__":
        pytest.main([__file__, '-v'])
