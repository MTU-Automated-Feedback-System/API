from flask import Blueprint, request
import repositories.dynamodb as db
import shortuuid
import json

submissions = {}
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

@bp.route('/submission/<id>', methods=["GET"])
def get_submission(id):
    return {db.submission_table.get_item(Key={'SubmissionId': id})}

@bp.route('/submission/all', methods=["GET"])
def get_all_submissions():
    print(db.submission_table.scan()['Items'])
    return {"submissions":db.submission_table.scan()['Items']}
