from .. import db


role_user = db.Table('role_user',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

class Role(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20),unique=True, nullable=False)
	description = db.Column(db.String(256))

	#relations
	users = db.relationship('User', secondary=role_user, lazy='dynamic',backref=db.backref('roles', lazy='dynamic'))
