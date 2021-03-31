from app.main import db
from app.main.model.osoba import Osoba
from app.main.model.hodnost import Hodnost
from app.main.model.utvar import Utvar

def save_new_osoba(data):
    osoba = Osoba.query.filter_by(osobni_cislo=data['osobni_cislo']).first()
    if not osoba:
        new_osoba = Osoba(
            jmeno=data['jmeno'],
            prijmeni=data['prijmeni'],
            osobni_cislo=data['osobni_cislo'],
            hodnost=Hodnost.query.filter_by(nazev=data['hodnost']).first(),
            utvar=Utvar.query.filter_by(cislo_vu=data['utvar']).first() 
        )

        
        save_changes(new_osoba)
        response_object = {
            'status': 'success',
            'message': 'Osoba added.'
        }
        return response_object, 200
        #return generate_token(new_user)

def get_all_osoba():
    return Osoba.query.join(Hodnost).with_entities(Osoba.jmeno, Osoba.prijmeni, Osoba.osobni_cislo, Hodnost.nazev.label("hodnost"), Utvar.cislo_vu.label("utvar")).all()

def save_changes(data):
    db.session.add(data)
    db.session.commit()