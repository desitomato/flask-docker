from models.user import UserModel
from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username',
type=str,
required=True,
help='This field cannot be blank'
)
_user_parser.add_argument('password',
type=str,
required=True,
help='This field cannot be blank'
)

class UserRegister(Resource):
    def post(self):
        data = _user_parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'user already exist'}, 400
        
        user = UserModel(data['username'], data['password'])
        user.save_to_db()
        return {'message': 'user created successfully'}, 201


class UserLogin(Resource):
    def post(self):
        data = _user_parser.parse_args()

        user = UserModel.find_by_username(data['username'])

        if user and safe_str_cmp(user.password, data['password']):
            return {'message': 'user logged in'}, 200
        return {'message': 'invalid credential'}, 401


class UserLogout(Resource):
    def delete(self, username):
        user = UserModel.find_by_username(username)
        try:
            user.delete_from_db()
        except:
            return {'message': 'error occur while logout'}
        return {'message': 'user logged out'}
