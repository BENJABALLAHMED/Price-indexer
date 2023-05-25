from fastapi import FastAPI, HTTPException, Query
import pandas as pd

app = FastAPI()

# Load data from the CSV file on server startup
data = pd.read_csv('data.csv', delimiter=';')

@app.get('/products')
async def get_products(product_id: int, start_date: str, end_date: str):
    
    # Get the reference price for the specified product
    reference_data = data[data['product'] == product_id]
    if reference_data.empty:
        raise HTTPException(status_code=404, detail='No reference price found for the specified product')

    reference_price = reference_data['price'].values[0]
    
    # Filter the data based on date interval
    filtered_data = data[(data['activity_date'] >= start_date) &
                         (data['activity_date'] <= end_date) &
                         (data['product'] != product_id)]

    # Calculate the price index for each different product
    filtered_data['index_price'] = filtered_data['price'] / reference_price * 100

    # Build the list of results
    results = filtered_data[['index_price', 'product', 'activity_date']].to_dict('records')
    return results

@app.get('/products_without_interval')
async def get_products(product_id: int, start_date: str, end_date: str):
    
    # Get the reference price for the specified product
    reference_data = data[data['product'] == product_id]
    if reference_data.empty:
        raise HTTPException(status_code=404, detail='No reference price found for the specified product')

    reference_price = reference_data['price'].values[0]
    
    # Filter the data based on date interval
    filtered_data = data[data['product'] != product_id]

    # Calculate the price index for each different product
    filtered_data['index_price'] = filtered_data['price'] / reference_price * 100

    # Build the list of results
    results = filtered_data[['index_price', 'product', 'activity_date']].to_dict('records')
    return results

