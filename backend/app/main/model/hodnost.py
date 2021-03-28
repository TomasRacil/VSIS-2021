from .. import db

class Hodnost(db.Model):
    """
    Model pro ukládání jenotlivých hodností a hodnostních sborů.
    """
    __tablename__="hodnost"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    jmeno = db.Column(db.String(20), unique=True, nullable=False) #spise nazev ale nevím kde všude změnit TODO
    hodnostni_sbor = db.Column(db.String(20), nullable=False)

    #def __init__ (self, hodnost, hodnostni_sbor):
     #   self.hodnost=hodnost
      #  self.hodnostni_sbor=hodnostni_sbor

    def __repr__(self):
        return f"hodnost: {self.hodnost} hodnostni_sbor: {self.hodnostni_sbor}"