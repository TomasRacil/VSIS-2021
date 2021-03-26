from .. import db


osoba_kurz = db.Table('osoba_kurz',
    db.Column('osoba_id', db.Integer, db.ForeignKey('osoba.id'), primary_key=True),
    db.Column('kurz_id', db.Integer, db.ForeignKey('kurz.id'), primary_key=True)
)

class Kurz(db.Model):
    """
    Model pro ukládání jenotlivých kurzů.
    """
    __tablename__="kurz"


    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nazev = db.Column(db.String(20), unique=True, nullable=False)
    misto = db.Column(db.String(20), nullable=False)
    vedouci = db.Column(db.String(32), nullable=False)
    voj_oznaceni = db.Column(db.String(20), nullable=False)
    zacatek_kurzu = db.Column(db.DateTime, nullable=False)
    konec_kurzu = db.Column(db.DateTime, nullable=False)

    osoby = db.relationship('Osoba', secondary=osoba_kurz, lazy='dynamic',backref=db.backref('kurzy', lazy='dynamic'))

    # def __init__ (self, nazev, misto, vedouci, voj_oznaceni, zacatek_kurzu, konec_kurzu):
    #     self.nazev=nazev
    #     self.misto=misto
    #     self.vedouci=vedouci
    #     self.voj_oznaceni=voj_oznaceni
    #     self.zacatek_kurzu=zacatek_kurzu
    #     self.konec_kurzu=konec_kurzu


    def __repr__(self):
        return f"nazev: {self.nazev} misto: {self.misto} vedouci: {self.vedouci} voj_oznaceni: {self.voj_oznaceni} zacatek_kurzu: {self.zacatek_kurzu} konec_kurzu: {self.konec_kurzu}"