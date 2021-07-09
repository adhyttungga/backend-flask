from app import app
from flask import request

# import controller
from app.controller import postsController

@app.route('/')
def index():
    return "Hello World!"

@app.route('/article', methods=["POST"])
def articles():
    return postsController.create()

@app.route('/article/<limit>/<offset>', methods=["GET"])
def paginations(limit, offset):
    return postsController.paginate(limit, offset)

@app.route('/article/<id>', methods=["GET", "PUT", "DELETE"])
def postsByIDs(id):
    if request.method == "GET":
        return postsController.postsByID(id)
    elif request.method == "PUT":
        return postsController.update(id)
    elif request.method == "DELETE":
        return postsController.remove(id)