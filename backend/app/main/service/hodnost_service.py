from app.main import db
from app.main.model.hodnost import Hodnost


def save_new_hodnost(data):
    hodnost = Hodnost.query.filter_by(nazev=data['nazev']).first()
    if not hodnost:
        new_hodnost = Hodnost(
            nazev=data['nazev'],
            hodnostni_sbor=data['hodnostni_sbor'],
        )

        save_changes(new_hodnost)
        response_object = {
            'status': 'success',
            'message': 'Hodnost added.'
        }
        return response_object, 200
        # return generate_token(new_user)


def get_all_hodnost():
    # , Hodnost.id).all()
    return Hodnost.query.with_entities(Hodnost.id, Hodnost.hodnostni_sbor, Hodnost.nazev).all()

def get_a_hodnost(id):
    return Hodnost.query.filter_by(id=id).first()

def remove_object(data):
    db.session.delete(data)
    db.session.commit()

def save_changes(data):
    db.session.add(data)
    db.session.commit()
