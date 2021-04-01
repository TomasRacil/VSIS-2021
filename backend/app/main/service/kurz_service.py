from app.main import db
from app.main.model.kurz import Kurz
from app.main.model.osoba import Osoba


def save_new_kurz(data):
    kurz = Kurz.query.filter_by(voj_oznaceni=data['voj_oznaceni']).first()
    if not kurz:
        new_kurz = Kurz(
            nazev=data['nazev'],
            misto=data['misto'],
            #vedouci=data['vedouci'],
            voj_oznaceni=data['voj_oznaceni'],
            zacatek_kurzu=data['zacatek_kurzu'],
            konec_kurzu=data['konec_kurzu']
        )
        
        save_changes(new_kurz)
        response_object = {
            'status': 'success',
            'message': 'Kurz added.'
        }
        return response_object, 200
        #return generate_token(new_user)

def get_all_kurz():
    return Kurz.query.with_entities(Kurz.nazev, Kurz.misto, Kurz.voj_oznaceni, Kurz.zacatek_kurzu, Kurz.konec_kurzu).all()  

def save_changes(data):
   db.session.add(data)
   db.session.commit()