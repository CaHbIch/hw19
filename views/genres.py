from flask_restx import Resource, Namespace

from auth.helpers import auth_required
from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required  # Получать данные могут только авторизованные пользователи
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required  # Получать данные могут только авторизованные пользователи
    def get(self, rid):
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200
