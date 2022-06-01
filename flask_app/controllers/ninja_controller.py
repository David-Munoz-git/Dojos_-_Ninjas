from flask_app import app
from flask import render_template, redirect, request, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/newNinja")
def newninjas():
  dojo = Dojo.get_all_dojos()
  return render_template("addingNinjas.html", all_dojos = dojo)






@app.route("/addNinja", methods=["POST"])
def addninja():
  query_data = {
          "first_name" : request.form["first_name"],
          "last_name" : request.form["last_name"],
          "age" : request.form["age"],
          "dojos_id" : request.form["dojos"]
      }
  Ninja.add_new_ninja(query_data)
  return redirect("/")








