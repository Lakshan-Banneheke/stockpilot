from flask import Blueprint, render_template
from db_access import db_action


USER_BP = Blueprint('USER_BP', __name__)


@USER_BP.route('/register', methods=['POST'])
def register():
    result = db_action("insert_one",[{"first_name":"nimal","last_name":"perera","age":23,"email":"nimal@skl.com"},"users"],"admin")
    print(result)
    return("Done")




