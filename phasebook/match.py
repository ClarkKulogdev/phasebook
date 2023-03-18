import time
from flask import Blueprint, request, redirect, url_for

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")




@bp.route("<int:match_id>", methods= ['POST','GET'])


def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"

    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    sorted_fave_numbers_1 = tuple(sorted(fave_numbers_1))
    value_sorted_fave_numbers_1= sorted_fave_numbers_1
    sorted_fave_numbers_2 = tuple(sorted(fave_numbers_2))


    hashing = { key:value for key, value in zip(sorted_fave_numbers_1,value_sorted_fave_numbers_1)}
    for number in sorted_fave_numbers_2:
        try:
            if hashing[number] != number:
                return False
        except:
            return False
    return True

@bp.route("/", methods=['POST','GET'])
def getmatch():
    if request.method == 'POST':
        findID = request.form['findID']
        return redirect(url_for("match.match",match_id = findID))

    else:
        findID = request.args.get('findID')
        return "GET"
