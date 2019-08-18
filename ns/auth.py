from flask_restplus import Namespace, Resource, reqparse
import flask_jwt_extended as jwt

from models.users import User


ns = Namespace('auth', description='Authorization')

@ns.route('')
class Authentication(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('username', type=str, required=True, help='Username cannot be blank.')
	parser.add_argument('password', type=str, required=True, help='Password cannot be blank.')

	# Validate user credentials and obtain access + refresh tokens
	def post(self):
		args = self.parser.parse_args()
		user = User.query.filter_by(username=args['username']).first()
		if user is not None:
			if user.check_password(args['password']):
				return {
				 	'access_token': jwt.create_access_token(identity=args['username']),
					'refresh_token': jwt.create_refresh_token(args['username'])
				}
			return { 'message': 'Invalid password' }, 401
		return { 'message': 'Invalid username' }, 401

	# Renew access token from refresh token
	@jwt.jwt_refresh_token_required
	def put(self):
		user = jwt.get_jwt_identity()
		return { 'access_token': jwt.create_access_token(identity=user) }
