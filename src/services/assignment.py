from flask import Blueprint, request
import repositories.dynamodb as db
import shortuuid
import json

submissions = {}
bp = Blueprint('assignment', __name__, template_folder='/src/templates')

@bp.route('/assignment', methods=["POST"])
def post_assignment():
    ...

@bp.route('/assignment/<id>', methods=["GET"])
def get_assignment(id):
    ...

@bp.route('/assignment/all', methods=["GET"])
def get_all_assignments():
    ...
