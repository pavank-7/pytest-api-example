from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, equal_to, has_item, has_key
'''
'''
def test_pet_schema():
    test_endpoint = "/pets/1"
    response = api_helpers.get_api_data(test_endpoint)
    assert response.status_code == 200
    # Validate the response schema against the defined schema in schemas.py
    validate(instance=response.json(), schema=schemas.pet)
'''
TODO: Finish this test by...
1) Extending the parameterization to include all available statuses
2) Validate the appropriate response code
3) Validate the 'status' property in the response is equal to the expected status
4) Validate the schema for each object in the response
'''
@pytest.mark.parametrize("status", [
    ("available"),
    ("pending"),
    ("sold"),
])
def test_find_by_status_200(status):
    test_endpoint = "/pets/findByStatus"
    params = {
        "status": status
    }
    response = api_helpers.get_api_data(test_endpoint, params)
    # 2) Validate the appropriate response code
    assert response.status_code == 200
    pets = response.json()
    # 3) Validate every pet in the response has the expected status
    for pet in pets:
        assert_that(pet["status"], equal_to(status))
    # 4) Validate the schema for each object in the response
    for pet in pets:
        validate(instance=pet, schema=schemas.pet)
'''

'''
@pytest.mark.parametrize("pet_id", [
    (9999),          # non-existent positive ID
    (99999),         # another non-existent ID
    (-1),            # negative ID (edge case)
])
def test_get_by_id_404(pet_id):
    test_endpoint = f"/pets/{pet_id}"
    response = api_helpers.get_api_data(test_endpoint)
    # 1) Validate the 404 response vvv
    assert response.status_code == 404