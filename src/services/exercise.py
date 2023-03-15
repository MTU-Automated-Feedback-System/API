from flask import Blueprint, request
from boto3.dynamodb.conditions import Key
import repositories.dynamodb as db
import shortuuid, json, datetime

bp = Blueprint('exercise', __name__, template_folder='/src/templates')


@bp.route('/exercise', methods=["POST"])
def post_exercise():
    payload = json.loads(request.data)
    exercise_id = shortuuid.uuid()
    payload["exercise_id"] = exercise_id
    payload["date_time"] = datetime.now().isoformat()
    db.exercise_table.put_item(Item=payload)
    return {"id": exercise_id}


@bp.route('/exercise/i/', methods=["GET"])
def get_exercise(id):
    exercise_id = request.args.get('exercise_id')
    date_time = request.args.get('date_time')
    exercise = db.exercise_table.get_item(Key={
            "exercise_id":  exercise_id,
            "date_time": date_time
        }
    )
    return {"exercise": exercise} 


@bp.route('/exercise/<id>', methods=["GET"])
def get_exercise_query(id):
    return {id: db.exercise_table.query(KeyConditionExpression=Key('exercise_id').eq(id))}



@bp.route('/exercise/all', methods=["GET"])
def get_all_exercises():
    print(db.exercise_table.scan()['Items'])
    return {"exercises": db.exercise_table.scan()['Items']}
