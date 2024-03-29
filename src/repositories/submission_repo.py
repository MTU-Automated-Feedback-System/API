import repositories.boto3_client as db
from boto3.dynamodb.conditions import Key


def add(payload):
    db.submission_table.put_item(Item=payload)
    

def update(submission_id, exercise_id, compiled_output, compiled_status, error_type, test_cases, feedback, cases):
    response = db.submission_table.update_item(
                Key={'submission_id': submission_id, 'exercise_id': exercise_id},
                UpdateExpression="set compiled_output=:o, compiled_status=:s, \
                error_type=:er, test_cases=:tc, feedback=:f, cases=:ca",
                ExpressionAttributeValues={
                    ':o': compiled_output, ':s': compiled_status, ':er':error_type, ':tc': test_cases,\
                        ":f": feedback, ":ca": cases},
                ReturnValues="UPDATED_NEW")
    return response['Attributes']


def get_item(submission_id, exercise_id):
    submission = db.submission_table.get_item(Key={
            "submission_id":  submission_id,
            "exercise_id":  exercise_id
        }
    )
    return submission
   
    
def get_query(submission_id):
    submission = db.submission_table.query(KeyConditionExpression=Key('submission_id').eq(submission_id))
    return submission


def get_student_submissions(student_id):
    submissions = db.submission_table.scan(FilterExpression=Key('student_id').eq(student_id))
    return submissions['Items']

def get_student_submissions_exercise(student_id, exercise_id):
    submissions = db.submission_table.scan(FilterExpression=Key('student_id').eq(student_id) & Key('exercise_id').eq(exercise_id))
    return submissions['Items']

def get_all_exercise_submissions(exercise_id):
    submissions = db.submission_table.scan(FilterExpression=Key('exercise_id').eq(exercise_id))
    return submissions['Items']

def get_all():
    return db.submission_table.scan()['Items']