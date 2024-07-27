import json
from datetime import datetime

def lambda_handler(event, context):
    print("Printing event as it is: \n", event)
    print("Added 0 index")
    print(event[0])
    start_date = datetime.strptime(event[0].get("startDate"), "%Y-%m-%d")
    end_date = datetime.strptime(event[0].get("endDate"), "%Y-%m-%d")
    
    date_diff = end_date - start_date
    if date_diff.days > 1:
        print("Difference between End Date and Start end is ", date_diff)
        return json.dumps(event[0])
    else:
        return None
