from app.main import db
from app.main.model.osoba import Osoba
from app.main.model.hodnost import Hodnost

def save_new_osoba(data):
    osoba = Osoba.query.filter_by(osobni_cislo=data['osobni_cislo']).first()
    if not osoba:
        new_osoba = Osoba(
            jmeno=data['jmeno'],
            prijmeni=data['prijmeni'],
            osobni_cislo=data['osobni_cislo'],
            hodnost=Hodnost.query.filter_by(jmeno=data['hodnost']).first()
        )

        #user_role=Role.query.filter_by(name="user").first()
        #if user_role:
        #    new_user.roles.append(user_role)
        
        save_changes(new_osoba)
        response_object = {
            'status': 'success',
            'message': 'Osoba přidána.'
        }
        return response_object, 200
        #return generate_token(new_user)

def save_changes(data):
    db.session.add(data)
    db.session.commit()