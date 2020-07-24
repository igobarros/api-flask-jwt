import datetime

from flask_restful import Resource, marshal
from flask import current_app
import jwt

from app.models import User
from app.schemas import user_field
from app import request, db


class Login(Resource):
    
    def post(self):
        payload = request.only(['username', 'password'])
        
        username = payload['username']
        password = payload['password']
        
        user = User.query.filter_by(username=username).first()
        
        if not user and not user.compare_password(password):
            return {'message': 'Usuário não encontrado ou senha incorreta!'}, 404
        
        data = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        
        token = jwt.encode(data, current_app.config['SECRET_KEY'])
        
        return {'access_token': token.decode('utf-8')}


class Register(Resource):
    
    def post(self):
        payload = request.only(['username', 'password'])
        
        username = payload['username']
        password = payload['password']
        
        user = User(username, password)
        
        db.session.add(user)
        db.session.commit()
        
        return marshal(user, user_field, 'user')