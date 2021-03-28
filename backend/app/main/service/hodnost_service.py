from app.main import db
from app.main.model.hodnost import Hodnost

def save_new_hodnost(data):
    hodnost = Hodnost.query.filter_by(jmeno=data['jmeno']).first() #tohle nevím co znamená, asi nejspíš že pokud tam je? TODO
    if not hodnost:
        new_hodnost = Hodnost(
            jmeno=data['jmeno'],
            hodnostni_sbor=data['hodnostni_sbor'],
        )

        #user_role=Role.query.filter_by(name="user").first()
        #if user_role:
        #    new_user.roles.append(user_role)
        
        save_changes(new_hodnost)
        response_object = {
            'status': 'success',
            'message': 'Hodnost added.'
        }
        return response_object, 200
        #return generate_token(new_user)

def get_all_hodnost():
    return Hodnost.query.with_entities(Hodnost.hodnostni_sbor, Hodnost.jmeno, Hodnost.id).all()

def save_changes(data):
    db.session.add(data)
    db.session.commit()