from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):

  def get(self):

    data = {"1":"goodbye world"}
    data["2"] = "qualquer coisa"
    return data

api.add_resource(HelloWorld,'/')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
