from flask import Blueprint, request, Response
import repositories.dynamodb as db
import shortuuid, json
from boto3.dynamodb.conditions import Key
from queues.sqs import send_to_queue
from datetime import datetime

bp = Blueprint('submission', __name__, template_folder='/src/templates')

"""
    Receive a submission
"""
@bp.route('/submission', methods=["POST"])
def post_submission():
    try:
        payload = json.loads(request.data)
        submission_id = shortuuid.uuid()
        payload["submission_id"] = submission_id
        payload["compiled_status"] = "processing"
        payload["date_time"] = datetime.now().isoformat()
        db.submission_table.put_item(Item=payload)
        response = send_to_queue(payload)
        return {"id": submission_id, "response": response}
    except Exception as e:
        return Response(f"{{'error':{e}}}", status=500, mimetype='application/json')


"""
    Update a submission
"""
@bp.route('/submission', methods=["PATCH"])
def update_submission():
    payload = json.loads(request.data)
    submission_id = payload['submission_id']
    exercise_id = payload['exercise_id']
    compiled_output = payload['compiled_output']
    compiled_status = payload['compiled_status']
    response = db.submission_table.update_item(
                Key={'submission_id': submission_id, 'exercise_id': exercise_id},
                UpdateExpression="set compiled_output=:o, compiled_status=:s",
                ExpressionAttributeValues={
                    ':o': compiled_output, ':s': compiled_status},
                ReturnValues="UPDATED_NEW")

    return response['Attributes']

"""
    Use get_item to retrieve a submission using the composite key
    This method is much more efficient but requires more information
"""
@bp.route('/submission/i/', methods=["GET"])
def get_submission():
    submission_id = request.args.get('submission_id')
    exercise_id = request.args.get('exercise_id')
    submission = db.submission_table.get_item(Key={
            "submission_id":  submission_id,
            "exercise_id":  exercise_id
        }
    )
    return {"submission": submission}


"""
    Get an item in the table only using the Partition key "submission_id"
    Will still be fast since the key is unique but less efficient
"""
@bp.route('/submission/<id>', methods=["GET"])
def get_submission_query(id):
    return {id: db.submission_table.query(KeyConditionExpression=Key('submission_id').eq(id))}


@bp.route('/submission/all', methods=["GET"])
def get_all_submissions():
    print(db.submission_table.scan()['Items'])
    return {"submissions": db.submission_table.scan()['Items']}
