from app.main import db
from app.main.model.hodnost import Hodnost


def save_new_hodnost(data):
    # tohle nevím co znamená, asi nejspíš že pokud tam je? TODO
    hodnost = Hodnost.query.filter_by(nazev=data['nazev']).first()
    if not hodnost:
        new_hodnost = Hodnost(
            nazev=data['nazev'],
            hodnostni_sbor=data['hodnostni_sbor'],
        )

        # user_role=Role.query.filter_by(name="user").first()
        # if user_role:
        #    new_user.roles.append(user_role)

        save_changes(new_hodnost)
        response_object = {
            'status': 'success',
            'message': 'Hodnost added.'
        }
        return response_object, 200
        # return generate_token(new_user)


def get_all_hodnost():
    # , Hodnost.id).all()
    return Hodnost.query.with_entities(Hodnost.hodnostni_sbor, Hodnost.nazev).all()


def save_changes(data):
    db.session.add(data)
    db.session.commit()