from flask import Flask
from flask_restful import Resource, Api
import cx_Oracle

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):

  def get(self):
    connection = cx_Oracle.connect("ADMIN","GarciaDavila34","jumpstartdb_high")
    cursor = connection.cursor()
    query = 'select * from USER_TABLE'
    cursor.execute(query)
    data = []
    for row in cursor:
      data.append(row)
      print row
    cursor.close()
    connection.close()
    return data

api.add_resource(HelloWorld,'/')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
