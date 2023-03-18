import dynamodb as db
from boto3.dynamodb.conditions import Key


def add(payload):
    db.exercise_table.put_item(Item=payload)
    # Add exception handling    
    
def get_item(exercise_id, date_time):
    exercise = db.exercise_table.get_item(Key={
        "exercise_id":  exercise_id,
        "date_time": date_time
        }
    )
    # Handle exception and/or more
    return exercise

def get_query(exercise_id):
    exercise = db.exercise_table.query(KeyConditionExpression=Key('exercise_id').eq(exercise_id))
    # Handle exception and/or more
    return exercise

def get_all():
    exercises = db.exercise_table.scan()['Items']
    # Handle exception and/or more
    return exercises