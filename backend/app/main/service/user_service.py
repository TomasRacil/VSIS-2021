import uuid
#import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.role import Role


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            # registered_on=datetime.datetime.utcnow()

        )

        user_role = Role.query.filter_by(name="user").first()
        if user_role:
            new_user.roles.append(user_role)

        save_changes(new_user)
        # response_object = {
        #    'status': 'success',
        #    'message': 'Successfully registered.'
        # }
        # return response_object, 201
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def update_user(user, data):
    #user = User.query.filter_by(public_id=public_id).first()
    if user.check_password(data.pop("current_password", False)):
        user.update(data)
        save_changes(user)
        return user
    else:
        response_object = {
            'status': 'fail',
            'message': 'Passwords does not match',
        }
        return response_object, 401


def delete_user(user, data):
    # if user.check_password(data.pop("current_password", False)):
    if True:
        remove_object(user)
        return user
    else:
        response_object = {
            'status': 'fail',
            'message': 'Passwords does not match',
        }
        return response_object, 401


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def remove_object(data):
    db.session.delete(data)
    db.session.commit()


def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token  # .decode()
        }
        return response_object, 201
    except Exception as e:
        print(e)
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
