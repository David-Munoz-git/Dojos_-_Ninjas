# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

#==========================================================
#MODEL FILE
#==========================================================


# model the class after the friend table from our database
class Dojo:
  db = 'dojo_and_ninjas_schema' #variable connected to schema
  def __init__( self , data ):
    self.id = data['id']

    self.name = data['name']

    self.created_at = data['created_at']
    self.updated_at = data['updated_at']



  # Now we use class methods to query our database
  @classmethod
  def get_all_dojos(cls):
    query = "SELECT * FROM dojos;"
    # make sure to call the connectToMySQL function with the schema you are targeting.
    results = connectToMySQL(cls.db).query_db(query)
    # Create an empty list to append our instances of friends
    dojos = []
    # Iterate over the db results and create instances of friends with cls.
    for dojo in results:
      dojos.append( cls(dojo) )
    return dojos

  @classmethod
  def createdojo(cls,data):
    query = "INSERT INTO dojos (name, created_at, updated_at) VALUES(%(name)s, NOW(), NOW() )"
    results = connectToMySQL(cls.db).query_db(query, data)
    return results
  
  @classmethod
  def dojoinfo(cls,data):
    query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s;"
    results = connectToMySQL(cls.db).query_db(query, data)
    return results