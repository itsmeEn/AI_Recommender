from mongoengine import Document, StringField, FloatField, ObjectIdField
from mongoengine import Document, StringField, FloatField, ObjectIdField, ListField # Import ListField

class Product(Document):
     _id = ObjectIdField()
     name = StringField(required=True, max_length=100)
     description = StringField()
     price = FloatField(required=True)
     category = StringField(max_length=50)
     tags = ListField(StringField(max_length=50)) # Change this to accept a list of strings

     meta = {'collection': 'products'}

