# FastAPI Price Indexer

This is a FastAPI-based web application that provides two endpoints for retrieving price index data.

## Installation

1. Clone the repository to your local machine:

2. Install the project dependencies:

```bash
pip install -r requirements.txt

```
## Usage

### Start the FastAPI Server

To start the FastAPI server locally, run the following command:

```bash
uvicorn main:app --reload
```
This command will start the server on `http://localhost:8000`.


This command will start the server on `http://localhost:8000`.

### Endpoints

The application provides the following endpoints:

#### 1. Get Products with Date Interval


**Endpoint**: `/products`

**Method**: `GET`

**Parameters**:
- `product_id` (integer): The ID of the product for which to retrieve price index data.
- `start_date` (string): The start date of the date interval in the format "DD/MM/YYYY".
- `end_date` (string): The end date of the date interval in the format "DD/MM/YYYY".

**Example Request**:

GET /products?product_id=12482&start_date=01/10/2021&end_date=31/10/2021


**Example Response**:

```json
[
    {
        "index_price": 105.2,
        "product": 12345,
        "activity_date": "2021-10-01"
    },
    {
        "index_price": 98.5,
        "product": 12345,
        "activity_date": "2021-10-02"
    },
    ...
]
```

#### 2. Get Products without interval 

**Endpoint**: `/products_without_interval`

**Method**: `GET`

**Parameters**:
- `product_id` (integer): The ID of the product for which to retrieve price index data.
- `start_date` (string): The start date of the date interval in the format "DD/MM/YYYY".
- `end_date` (string): The end date of the date interval in the format "DD/MM/YYYY".

**Example Request**:

GET /products?product_id=12482&start_date=01/10/2021&end_date=31/10/2021


**Example Response**:

```json
[
    {
        "index_price": 105.2,
        "product": 12345,
        "activity_date": "2021-10-01"
    },
    {
        "index_price": 98.5,
        "product": 12345,
        "activity_date": "2021-10-02"
    },
    ...
]
```
## Running Tests

```bash
pytest test.py

```
## Docker

The application can also be run inside a Docker container. Follow the steps below to build and run the Docker image

1. Build the Docker image:


```bash
docker build -t price-indexer .

```
2. Run the Docker container

```bash

docker run -d -p 8000:8000 price-indexer

```