from flask_app import app
from flask import render_template, redirect, request, flash
from flask_app.models.dojo import Dojo

@app.route("/")
def dojos():
    dojo = Dojo.get_all_dojos()
    return render_template("dojos.html",all_dojos = dojo )

@app.route("/")
def createdojo():
    query_data = {
        "name" : request.form["name"],
    }
    Dojo.createdojo(query_data)
    return redirect("/")



@app.route("/dojosInfo/<int:id>")
def dojosinfo(id):
    query_data = {
        "id" : id
    }
    dojosinfo = Dojo.dojoinfo(query_data)
    return render_template("dojosInfo.html",  dojosinfo = dojosinfo)



