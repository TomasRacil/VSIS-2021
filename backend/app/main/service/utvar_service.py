from app.main import db
from app.main.model.utvar import Utvar


def get_a_utvar(cislo_vu):
    return Utvar.query.filter_by(cislo_vu=cislo_vu).first()


def save_new_utvar(data):
    utvar = Utvar.query.filter_by(cislo_vu=data['cislo_vu']).first()
    if not utvar:
        new_utvar = Utvar(
            nazev_utvaru=data['nazev_utvaru'],
            lokace=data['lokace'],
            cislo_vu=data['cislo_vu']
        )

        save_changes(new_utvar)
        response_object = {
            'status': 'success',
            'message': 'Utvar added.'
        }
        return response_object, 200
        # return generate_token(new_user)


def get_all_utvar():
    return Utvar.query.with_entities(Utvar.cislo_vu, Utvar.lokace, Utvar.nazev_utvaru).all()


def remove_object(data):
    db.session.delete(data)
    db.session.commit()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
