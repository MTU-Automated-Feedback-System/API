from flask import Blueprint, request
import repositories.exercise_repo as db_exercise
import shortuuid, json
from datetime import datetime

bp = Blueprint('exercise', __name__, template_folder='/src/templates')


@bp.route('/exercise', methods=["POST"])
def post_exercise():
    payload = json.loads(request.data)
    exercise_id = shortuuid.uuid()
    payload["exercise_id"] = exercise_id
    payload["date_time"] = datetime.now().isoformat()
    db_exercise.add(payload)
    return {"id": exercise_id}


@bp.route('/exercise/i/', methods=["GET"])
def get_exercise():
    exercise_id = request.args.get('exercise_id')
    date_time = request.args.get('date_time')
    return {"exercise": db_exercise.get_item(exercise_id, date_time)} 


@bp.route('/exercise/<id>', methods=["GET"])
def get_exercise_query(id):
    return {id: db_exercise.get_query(id)}


@bp.route('/exercise/all', methods=["GET"])
def get_all_exercises():
    return {"exercises": db_exercise.get_all()}
