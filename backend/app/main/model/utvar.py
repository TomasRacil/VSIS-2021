from .. import db

class Utvar(db.Model):
    """
    Model pro ukládání názvu útvaru, jeho lokace a čísla VÚ/VZ
    """
    __tablename__="utvar"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nazev_utvaru = db.Column(db.String(50), nullable=False)
    lokace = db.Column(db.String(30), nullable=False)
    cislo_vu = db.Column(db.Integer, unique=True, nullable=False)

    #osoba_id = db.Column(db.Integer, db.ForeignKey('id_osoba'), nullable=False)
    #osoba = db.relationship('Osoba', backref=db.backref('posts', lazy=True))

    
    # def __init__ (self, nazev_utvaru, lokace, cislo_vu):
    #     self.nazev_utvaru=nazev_utvaru
    #     self.lokace=lokace
    #     self.cislo_vu=cislo_vu

    def __repr__(self):
              return f"nazev_utvaru: {self.nazev_utvaru} lokace: {self.lokace} cislo_vu: {self.cislo_vu}"