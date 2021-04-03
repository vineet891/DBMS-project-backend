import psycopg2
import os
from flask_restful import Resource, reqparse
from models.match import MatchModel
from models.result import ResultModel
from flask_jwt_extended import jwt_required, get_jwt_identity

class ResultTeam(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('winner_id',
                        type=int,
                        required=True,
                        help="winner_id cant be blank"
                        )
    parser.add_argument('match_id',
                        type=int,
                        required=True,
                        help="match_id cant be blank"
                        )
    parser.add_argument('t1Score',
                        type=int,
                        required=True,
                        help="t1Score cant be blank"
                        )
    parser.add_argument('t2Score',
                        type=int,
                        required=True,
                        help="t2Score cant be blank"
                        )

    @jwt_required()
    def post(self):
        data = ResultTeam.parser.parse_args()
        res = ResultModel(data['winner_id'],data['match_id'])
        res.insertTeam(data['t1Score'],data['t2Score'])

class ResultNet(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('winner_id',
                        type=int,
                        required=True,
                        help="winner_id cant be blank"
                        )
    parser.add_argument('match_id',
                        type=int,
                        required=True,
                        help="match_id cant be blank"
                        )
    parser.add_argument('set1team1',
                        type=int,
                        required=True,
                        help="Score cant be blank"
                        )
    parser.add_argument('set1team2',
                        type=int,
                        required=True,
                        help="t2Score cant be blank"
                        )
    parser.add_argument('set2team1',
                        type=int,
                        required=True,
                        help="Score cant be blank"
                        )
    parser.add_argument('set2team2',
                        type=int,
                        required=True,
                        help="t2Score cant be blank"
                        )
    parser.add_argument('set3team1',
                        type=int,
                        required=False,
                        help="Score cant be blank"
                        )
    parser.add_argument('set3team2',
                        type=int,
                        required=False,
                        help="t2Score cant be blank"
                        )

    @jwt_required()
    def post(self):
        data = ResultNet.parser.parse_args()
        res = ResultModel(data['winner_id'],data['match_id'])
        if data['set3team1']:
            res.insertNet(data['set1team1'],data['set1team2'],data['set2team1'],data['set2team2'],data['set3team1'],data['set3team2'])
        else:
            res.insertNet(data['set1team1'],data['set1team2'],data['set2team1'],data['set2team2'])
        
        
