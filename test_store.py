from jsonschema import validate
import pytest
import random
import schemas
import api_helpers
from hamcrest import assert_that, equal_to


@pytest.fixture
def create_order():
   
    # Step 1: Create a new pet with a unique random ID
    unique_id = random.randint(10000, 99999)
    new_pet = {
        "id": unique_id,
        "name": "testpet",
        "type": "dog",
        "status": "available"
    }
    pet_response = api_helpers.post_api_data("/pets/", new_pet)
    assert pet_response.status_code == 201

    # Step 2: Place an order for that pet
    order_data = {
        "pet_id": new_pet["id"]
    }
    order_response = api_helpers.post_api_data("/store/order", order_data)
    assert order_response.status_code == 201

    order = order_response.json()
    return order["id"], new_pet["id"]


@pytest.mark.parametrize("new_status", [
    "sold",
    "available",
    "pending",
])
def test_patch_order_by_id(create_order, new_status):
    """Test PATCH /store/order/{order_id} updates order and pet status."""
    order_id, pet_id = create_order

    # Step 3: Send PATCH request to update the order status
    patch_data = {
        "status": new_status
    }
    patch_response = api_helpers.patch_api_data(f"/store/order/{order_id}", patch_data)

    # Step 4: Validate the response code
    assert patch_response.status_code == 200

    # Step 5: Validate the success message
    response_json = patch_response.json()
    assert_that(response_json["message"], equal_to("Order and pet status updated successfully"))

    # Step 6: Verify the pet's status was also updated
    pet_response = api_helpers.get_api_data(f"/pets/{pet_id}")
    assert pet_response.status_code == 200
    assert_that(pet_response.json()["status"], equal_to(new_status))