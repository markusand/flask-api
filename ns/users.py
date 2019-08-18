from flask_restplus import Namespace, Resource
import flask_jwt_extended as jwt

from models.users import User
import schemas.users as schemas


ns = Namespace('users', description='Users endpoint')

@ns.route('')
class ListUsers(Resource):
	@ns.marshal_with(schemas.list_users)
	def get(self):
		return User.query.all()


@ns.route('/me')
class SelfUser(Resource):
	@jwt.jwt_required
	@ns.marshal_with(schemas.self_user)
	def get(self):
		username = jwt.get_jwt_identity()
		user = User.query.filter_by(username=username).first()
		if user is None:
			ns.abort(404, 'User ' + username + ' does not exist')
		return user


@ns.route('/<string:username>')
class SingleUser(Resource):
	@ns.marshal_with(schemas.single_user)
	def get(self, username):
		user = User.query.filter_by(username=username).first()
		if user is None:
			ns.abort(404, 'User ' + username + ' does not exist')
		return user
