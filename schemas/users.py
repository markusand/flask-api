from flask_restplus import Model, fields


list_users = Model('UserListSchema', {
	'username': fields.String,
	'name': fields.String(attribute=lambda x: x.name + ' ' + x.surname),
	'photo': fields.String(attribute='avatar'),
	'admin': fields.Boolean(attribute= lambda x: True if x.role == 'admin' else False),
})

single_user = Model('UserSchema', {
	'username': fields.String,
	'name': fields.String(attribute=lambda x: x.name + ' ' + x.surname),
	'gender': fields.String(attribute=lambda x: 'male' if x.gender else 'female'),
	'email': fields.String,
	'region': fields.String,
	'birthday': fields.DateTime(dt_format='rfc822'),
	'photo': fields.String(attribute='avatar'),
	'role': fields.String,
})

self_user = Model('UserSelfSchema', {
	'username': fields.String,
	'name': fields.String(attribute=lambda x: x.name + ' ' + x.surname),
	'gender': fields.String(attribute=lambda x: 'male' if x.gender else 'female'),
	'email': fields.String,
	'region': fields.String,
	'birthday': fields.DateTime(dt_format='rfc822'),
	'photo': fields.String(attribute='avatar'),
	'role': fields.String,
	'last_update': fields.DateTime(attribute='ts', dt_format='rfc822')
})
