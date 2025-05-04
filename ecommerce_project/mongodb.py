from mongoengine import connect, Document, StringField, IntField
from django.conf import settings

def connect_to_mongodb():
    """Connect to MongoDB using the settings from Django settings."""
    connect(
        db=settings.MONGODB_NAME,
        host=settings.MONGODB_URI
    )

class Product(Document):
    name = StringField(required=True)
    price = IntField(required=True)
    description = StringField() 