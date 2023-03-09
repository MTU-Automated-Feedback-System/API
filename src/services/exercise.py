from flask import Blueprint, request
import repositories.dynamodb as db
import shortuuid
import json

bp = Blueprint('exercise', __name__, template_folder='/src/templates')


@bp.route('/exercise', methods=["POST"])
def post_exercise():
    payload = json.loads(request.data)
    exercise_id = shortuuid.uuid()
    payload["exercise_id"] = exercise_id
    db.exercise_table.put_item(Item=payload)
    return {"id": exercise_id}


@bp.route('/exercise/<id>', methods=["GET"])
def get_exercise(id):
    exercise = db.exercise_table.get_item(Key={'exercise_id': id})
    return {"data": exercise}


@bp.route('/exercise/all', methods=["GET"])
def get_all_exercises():
    print(db.exercise_table.scan()['Items'])
    return {"exercises": db.exercise_table.scan()['Items']}
