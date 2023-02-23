from flask import Blueprint, request
import repositories.dynamodb as db
import shortuuid
import json

bp = Blueprint('assignment', __name__, template_folder='/src/templates')


@bp.route('/assignment', methods=["POST"])
def post_assignment():
    payload = json.loads(request.data)
    AssignmentId = shortuuid.uuid()
    payload["AssignmentId"] = AssignmentId
    db.assignment_table.put_item(Item=payload)
    return {"id": AssignmentId}


@bp.route('/assignment/<id>', methods=["GET"])
def get_assignment(id):
    assignment = db.assignment_table.get_item(Key={'AssignmentId': id})
    return {"data": assignment}


@bp.route('/assignment/all', methods=["GET"])
def get_all_assignments():
    print(db.assignment_table.scan()['Items'])
    return {"assignments": db.assignment_table.scan()['Items']}
