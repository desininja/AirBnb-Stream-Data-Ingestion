
from datetime import datetime
def lambda_handler(event, context):
    start_date = datetime.strptime(event.get("startDate"), "%Y-%m-%d")
    end_date = datetime.strptime(event.get("endDate"), "%Y-%m-%d")
    
    date_diff = end_date - start_date
    if date_diff.days > 1:
        return event
    else:
        return None
