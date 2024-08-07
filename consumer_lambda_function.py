import json
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    target_bucket_name = 'air-bnb-processed-entries'
    event_data = json.loads(event[0])
    if event:
        print(event_data)
        print(type(event_data))
        
        file_key =  event_data.get("bookingId") + ".json"
        s3_client.put_object(Bucket = target_bucket_name, Key=file_key,Body = json.dumps(event_data))
        
        return {
            'statusCode': 200,
            'body': json.dumps('SUCCESSFULLY SAVED DATA TO S3')
            }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps('NO DATA WAS PASSED, HENCE NO DATA SAVED TO S3')
            }
