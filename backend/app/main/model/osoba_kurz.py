from .. import db


osoba_kurz = db.Table('osoba_kurz',
    db.Column('osoba_id', db.Integer, db.ForeignKey('osoba.id'), primary_key=True),
    db.Column('kurz_id', db.Integer, db.ForeignKey('kurz.id'), primary_key=True)
)

class Osoba_Kurz(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20),unique=True, nullable=False)
	description = db.Column(db.String(256))

	#relations
	kurzy = db.relationship('Kurz', secondary=osoba_kurz, lazy='dynamic',backref=db.backref('kurzy', lazy='dynamic'))
