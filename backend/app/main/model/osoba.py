from .. import db

class Osoba(db.Model):
    """Model pro ukládání jenotlivých jmen, příjmení, osobní číslo, FK-hodnost, FK-kurz, FK-utvar."""
    __tablename__="osoba"


    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    jmeno = db.Column(db.String(20), nullable=False)
    prijmeni = db.Column(db.String(64), nullable=False)
    osobni_cislo = db.Column(db.String(64), unique=True, nullable=False)

    hodnost_id = db.Column(db.Integer, db.ForeignKey('hodnost.id'), nullable=False)
    hodnost = db.relationship('Hodnost', backref=db.backref('osoby', lazy='dynamic'))

    #kurz_id = db.Column(db.Integer, db.ForeignKey('ID_KURZ'), nullable=False)
    #kurz = db.relationship('Kurz', backref=db.backref('posts', lazy=True))

    #utvar_id = db.Column(db.Integer, db.ForeignKey('ID_UTVAR'), nullable=False)
    #utvar = db.relationship('Utvar', backref=db.backref('posts', lazy=True))


    def __init__ (self, jmeno, prijmeni, osobni_cislo):
        self.jmeno=jmeno
        self.prijmeni=prijmeni
        self.osobni_cislo=osobni_cislo
        

    def __repr__(self):
        return f"jmeno: {self.jmeno} prijmeni: {self.prijmeni} osobni_cislo: {self.osobni_cislo}"