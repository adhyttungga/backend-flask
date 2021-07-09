from app import db
from datetime import datetime
from sqlalchemy.orm import validates

class Posts(db.Model):
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  title = db.Column(db.String(200))
  content = db.Column(db.Text)
  category = db.Column(db.String(100))
  created_date = db.Column(db.DateTime, default=datetime.utcnow)
  updated_date = db.Column(db.DateTime, default=datetime.utcnow)
  status = db.Column(db.Enum('Publish', 'Draft', 'Thrash', name='postsStatus'), default='Draft')
  
  def __repr__(self):
    return '<Posts {}>'.format(self.name)
  
  @validates("title")
  def validate_title(self, key, title):
    if not title: 
      raise AssertionError("Title is required")
    if len(title) < 20:
      raise AssertionError("Title must be at least 20 character")
    return title
  
  @validates("content")
  def validate_content(self, key, content):
    if not content: 
      raise AssertionError("Content is required")
    if len(content) < 200:
      raise AssertionError("Content must be at least 200 character")
    return content
  
  @validates("category")
  def validate_category(self, key, category):
    if not category: 
      raise AssertionError("Category is required")
    if len(category) < 3:
      raise AssertionError("Category must be at least 3 character")
    return category
  
  @validates("status")
  def validate_status(self, key, status):
    if not status: 
      raise AssertionError("Status is required")
    elif status not in ['Publish', 'Draft', 'Thrash']:
      raise AssertionError("{} is not supported status".format(status))
    return status
