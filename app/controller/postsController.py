from app.model.posts import Posts

from app import response, app, db
from flask import request, jsonify
import json
import math

def index():
  try: 
    posts = Posts.query.all()
    data = formatArray(posts)
    return response.success(data, "success")
  except Exception as e:
    print(e)
    
def formatArray(datas):
  array = []  
  for data in datas:
    array.append(singleObject(data))
  return array

def singleObject(data):
  data = {
    "id": data.id,
    "title": data.title,
    "content": data.content,
    "category": data.category,
    "status": data.status,    
  }
  return data

# create function create for /article POST method
def create():
  try:
    data = request.get_json(force = True)
    title = data['title']
    content = data['content']
    category = data['category']
    status = data['status']
    # title = request.form.get('title')
    # content = request.form.get('content')
    # category = request.form.get('category')
    # status = request.form.get('status')
    input = [{
      "title": title,
      "content": content,
      "category": category,
      "status": status,
    }]
    posts = Posts(
      title=title,
      content=content,
      category=category,
      status=status      
    )
    db.session.add(posts)
    db.session.commit()
    return response.success(input, 'Successfully added new posts')
  except AssertionError as e:
    return response.badRequest([], "{}".format(e))
    
# create function paginate for /article/<limit>/<offset> GET method
def paginate(limit, offset):
  try:
    limit = int(limit)
    offset = int(offset)
    return jsonify(paginateList(limit, offset))
  except Exception as e:
    print(e)

def paginateList(limit, offset):
  posts = Posts.query.all()
  data = formatArray(posts)
  count = len(data)
  
  obj = {}
  
  if (count < offset):
    obj["success"] = False
    obj["message"] = "The selected page (offset) exceeds the total data limit!"
    return obj
  
  else:
    # make response
    obj['success'] = True
    obj['start_page'] = offset
    obj['per_page'] = limit
    obj['total_data'] = count
    obj['total_page'] = math.ceil(count / limit)
    obj['results'] = data[(offset - 1):(offset - 1 + limit)]
    obj['all_results'] = data
    return obj
  return obj

# create function postsByID for /article/<id> GET method
def postsByID(id):
  try:
    posts = Posts.query.filter_by(id=id).first()
    if not posts:
      return response.badRequest([], "Posts not found")
    data = singlePosts(posts)
    return response.success(data, "success")
  except Exception as e:
    print(e)

def singlePosts(posts):
  data = {
    "id": posts.id,
    "title": posts.title,
    "content": posts.content,
    "category": posts.category,
    "status": posts.status
  }
  return data

# create function update for /article/<id> PUT method
def update(id):
  try:
    data = request.get_json(force = True)
    title = data['title']
    content = data['content']
    category = data['category']
    status = data['status']
    # title = request.form.get('title')
    # content = request.form.get('content')
    # category = request.form.get('category')
    # status = request.form.get('status')
    input = [{
      "title": title,
      "content": content,
      "category": category,
      "status": status,
    }]
    posts = Posts.query.filter_by(id=id).first()
    posts.title = title
    posts.content = content
    posts.category = category
    posts.status = status
    db.session.commit()
    return response.success(input, "Managed to change the posts")
  except AssertionError as e:
    return response.badRequest([], "{}".format(e))

# create function remove for /article/<id> DELETE method
def remove(id):
  try: 
    posts = Posts.query.filter_by(id=id).first()
    if not posts:
      return response.badRequest({}, "Posts not found")
    db.session.delete(posts)
    db.session.commit()
    return response.success("", "Successfully removed the posts")
  except Exception as e:
    print(e)
