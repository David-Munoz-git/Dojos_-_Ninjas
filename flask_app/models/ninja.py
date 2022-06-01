# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo


#==========================================================
#MODEL FILE
#==========================================================


# model the class after the friend table from our database
class Ninja:
  db = 'dojo_and_ninjas_schema' #variable connected to schema
  def __init__( self , data ):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.age = data['age']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.dojo_id = data['dojo_id']



  # Now we use class methods to query our database

  @classmethod
  def add_new_ninja(cls, data):
    query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojos_id) VALUES(%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojos_id)s)"
    results = connectToMySQL(cls.db).query_db(query, data)
    return results

#use f" {variable} to pass variable in the redirect"