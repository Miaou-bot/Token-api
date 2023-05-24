from flask import Flask
from flask_restful import Api, Resource, reqparse
from os import environ

app = Flask(__name__)
api = Api(app)
token = environ['bot_token']
tokans = environ['tokens'].split("||")
def check_token(token):
  return token in tokans

arguments = reqparse.RequestParser()
arguments.add_argument('token', type=str, help="Nous avons de besoin de l'authorisation", required=True)

class main(Resource):
  def get(self):
    args = arguments.parse_args()
    if check_token(args['token']) is False: return {"help: "'Invalid token'}, 400
    return {"token": token}, 200

api.add_resource(main, "/token")
@app.route('/')
def home():
  return "Closed api."

app.run(host='0.0.0.0', port=81)
