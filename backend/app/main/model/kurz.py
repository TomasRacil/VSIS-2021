from .. import db
from datetime import datetime


osoba_kurz = db.Table('osoba_kurz',
    db.Column('osoba_id', db.Integer, db.ForeignKey('osoba.id'), primary_key=True),
    db.Column('kurz_id', db.Integer, db.ForeignKey('kurz.id'), primary_key=True),
    db.Column('ucastnik', db.Boolean,default=True, nullable=False),
    db.Column('vedouci',db.Boolean,default=False, nullable=False)
)

class Kurz(db.Model):
    """
    Model pro ukládání jenotlivých kurzů: jejich název, místo, vojenské označení, začátek a konec kurzu.
    """
    __tablename__="kurz"


    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    nazev = db.Column(db.String(40), unique=True, nullable=False) 
    misto = db.Column(db.String(20), nullable=False)
    #vedouci = db.Column(db.String(32), nullable=False) #kam dat toho vedoucího tedy? jak ho přidáváme tedka?
    voj_oznaceni = db.Column(db.String(20), unique=True, nullable=False)
    zacatek_kurzu = db.Column(db.Date, nullable=False) 
    konec_kurzu = db.Column(db.Date, nullable=False) 

    osoby = db.relationship('Osoba', secondary=osoba_kurz, lazy='dynamic',backref=db.backref('kurzy', lazy='dynamic'))

    # def __init__ (self, nazev, misto, vedouci, voj_oznaceni, zacatek_kurzu, konec_kurzu):
    #     self.nazev=nazev
    #     self.misto=misto
    #     self.vedouci=vedouci
    #     self.voj_oznaceni=voj_oznaceni
    #     self.zacatek_kurzu=zacatek_kurzu
    #     self.konec_kurzu=konec_kurzu


    def __repr__(self):
        return f"nazev: {self.nazev} misto: {self.misto} voj_oznaceni: {self.voj_oznaceni} zacatek_kurzu: {self.zacatek_kurzu} konec_kurzu: {self.konec_kurzu}"