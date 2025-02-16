from flask import request
from flask_restx import Resource, Namespace

from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route("/")
class AuthView(Resource):
    def post(self):
        """Авторизация пользователя"""
        req_json = request.json
        username = req_json.get('username')
        password = req_json.get('password')
        if None in [username, password]:
            return "Нужно имя и пароль", 400
        tokens = auth_service.generate_tokens(username, password)
        if tokens != False:
            return tokens, 201
        else:
            return "Ошибка в запросе", 400

    def put(self):
        """Обновления авторизации пользователя."""
        req_json = request.json
        ref_token = req_json.get('refresh_token')
        if not ref_token:
            return "Не задан токен", 400

        tokens = auth_service.approve_refresf_token(ref_token)
        if tokens:
            return tokens
        else:
            return "Ошибка в запросе"
