import boto3
import random
import time
from decimal import Decimal

# Initialize DynamoDB resource
session = boto3.Session(profile_name='default', region_name='ap-south-1')
dynamodb = session.resource('dynamodb')
table = dynamodb.Table('OrdersRawTable') 

def generate_order_data():
    """Generate random order data with DynamoDB-compatible types."""
    orderid = str(random.randint(1, 10000))
    product_name = random.choice(['Laptop', 'Phone', 'Tablet', 'Headphones', 'Charger'])
    quantity = random.randint(1, 5)
    price = Decimal(str(round(random.uniform(10.0, 500.0), 2)))  # Decimal for DynamoDB
    
    return {
        'orderid': orderid,
        'product_name': product_name,
        'quantity': quantity,
        'price': price
    }

def insert_into_dynamodb(data):
    """Insert data into DynamoDB."""
    try:
        table.put_item(Item=data)
        print(f"Inserted data: {data}")
    except Exception as e:
        print(f"Error inserting data: {str(e)}")

if __name__ == '__main__':
    try:
        while True:
            data = generate_order_data()
            insert_into_dynamodb(data)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScript stopped by manual intervention!")
