import requests

def test_get_products():
    # Define the base URL of the server
    base_url = 'http://localhost:8000'

    # Specify the query parameters
    params = {
        'product_id': 12482,
        'start_date': '01/10/2021',
        'end_date': '01/10/2021'
    }

    # Send a GET request to the server
    response = requests.get(f"{base_url}/products", params=params)

    # Check the response status code
    assert response.status_code == 200

    # Parse the response JSON
    results = response.json()

    # Perform assertions on the results
    assert isinstance(results, list)
    assert len(results) > 0

    for result in results:
        assert 'index_price' in result
        assert 'product' in result
        assert 'activity_date' in result

def test_get_products_with_interval():
    # Define the base URL of the server
    base_url = 'http://localhost:8000'

    # Specify the query parameters
    params = {
        'product_id': 12482,
        'start_date': '01/10/2021',
        'end_date': '01/10/2021'
    }

    # Send a GET request to the server
    response = requests.get(f"{base_url}/products_without_interval", params=params)

    # Check the response status code
    assert response.status_code == 200

    # Parse the response JSON
    results = response.json()

    # Perform assertions on the results
    assert isinstance(results, list)
    assert len(results) > 0

    for result in results:
        assert 'index_price' in result
        assert 'product' in result
        assert 'activity_date' in result