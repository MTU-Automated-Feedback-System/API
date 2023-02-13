from flask import Blueprint, request
import repositories.dynamodb as db
import shortuuid
import json
from boto3.dynamodb.conditions import Key

bp = Blueprint('submission', __name__, template_folder='/src/templates')


@bp.route('/submission', methods=["POST"])
def post_submission():
    payload = json.loads(request.data)
    print(payload)
    SubmissionId = shortuuid.uuid()
    payload["SubmissionId"] = SubmissionId
    payload["status"] = "processing"
    print(payload)
    db.submission_table.put_item(Item=payload)
    return {"id": SubmissionId}


"""
    Use get_item to retrieve a submission using the composite key
    This method is much more efficient but requires more information
"""
@bp.route('/submission/i/', methods=["GET"])
def get_submission():
    SubmissionId = request.args.get('SubmissionId')
    AssignmentId = request.args.get('AssignmentId')
    print(SubmissionId, AssignmentId)
    return {SubmissionId:
        db.submission_table.get_item(Key={
            "SubmissionId":  SubmissionId,
            "AssignmentId":  AssignmentId
        }
    )}


"""
    Get an item in the table only using the Partition key "SubmissionId"
    Will still be fast as the key is unique but less efficient
"""
@bp.route('/submission/<id>', methods=["GET"])
def get_submission_query(id):
    return {id: db.submission_table.query(KeyConditionExpression=Key('SubmissionId').eq(id))}


@bp.route('/submission/all', methods=["GET"])
def get_all_submissions():
    print(db.submission_table.scan()['Items'])
    return {"submissions": db.submission_table.scan()['Items']}
