from models.user import User
from flask import Flask, request, jsonify
import jwt
from datetime import datetime, timedelta
from settings import SECRET_KEY, TEMPO_EXPIRACAO_SEGUNDOS

app = Flask(__name__)

users: list[User] = []

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    for user in users:
        if user.username == data['username']:
            return jsonify({'status': 'fail'}), 409
    user = User(data['username'], data['password'])
    users.append(user)
    expiracao = datetime.utcnow() + timedelta(seconds=TEMPO_EXPIRACAO_SEGUNDOS)
    token = jwt.encode({'username': user.username, "expiracao": expiracao.timestamp()}, SECRET_KEY, algorithm='HS256')
    return jsonify({'status': 'success', 'token': token})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    for user in users:
        if user.username == data['username'] and user.password == data['password']:
            expiracao = datetime.utcnow() + timedelta(seconds=TEMPO_EXPIRACAO_SEGUNDOS)
            token = jwt.encode({'username': user.username, "expiracao": expiracao.timestamp()}, SECRET_KEY, algorithm='HS256')
            return jsonify({'status': 'success', 'token': token})
    return jsonify({'status': 'fail'}), 401

@app.route('/verificar', methods=['POST'])
def verificar():
    token = request.get_json()['token']
    try:
        if datetime.fromtimestamp(jwt.decode(token, SECRET_KEY, algorithms=['HS256'])['expiracao']) < datetime.utcnow():
            return jsonify({'status': 'fail'}), 401
        return jsonify({'status': 'success'})
    except:
        return jsonify({'status': 'fail'}), 401
    
app.run()
