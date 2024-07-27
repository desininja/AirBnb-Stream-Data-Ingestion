import json
import boto3
import random
import uuid
from datetime import datetime, timedelta

sqs_client = boto3.client("sqs")

QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/025066280149/AirBnb-Booking-queue"

def generate_booking_data():

    booking_id = str(uuid.uuid4())
    states = [ "Alaska", "Arizona", "California" "Texas", "Utah", "Vermont", "Virginia", "Washington",
               "West Virginia", "Wisconsin", "Wyoming","New Delhi"]
    countries = ["Afghanistan", "Albania","Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania",
               "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta",
               "Mexico","Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", 
                "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
                "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City",
                "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe","India"]
    start_date = datetime.now() + timedelta(days=random.randint(0, 365))  
    end_date = start_date + timedelta(days=random.randint(1, 30))
    return {
"bookingId": booking_id,
"userId": "User"+f"{random.randint(1,1000)}", 
"propertyId": "Property"+f"{random.randint(1,300)}", 
"location": f"{random.choice(states)}, {random.choice(countries)}", 
"startDate": start_date.strftime("%Y-%m-%d"), 
"endDate": end_date.strftime("%Y-%m-%d"), 
"price": round(random.uniform(0,1000.0),2)
}



def lambda_handler(event, context):
    i=0
    while(i<200):
        booking_details = generate_booking_data()
        print(booking_details)
        sqs_client.send_message(QueueUrl=QUEUE_URL,MessageBody=json.dumps(booking_details))

        i+=1
    

    return {
        'statusCode': 200,
        'body': json.dumps('Booking details published to SQS!')
    }

