from pymodm import fields, MongoModel

class User(MongoModel):
    email = fields.EmailField(primary_key=True) # because primary_key is True, we will need to query this field using the label _id
    age = fields.IntegerField()
    heart_rate = fields.ListField(field=fields.IntegerField())
    heart_rate_times = fields.ListField(field=fields.DateTimeField())
