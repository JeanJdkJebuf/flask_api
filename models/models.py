from app import db

class Food(db.Model):
    __tablename__ = 'foodlist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    count = db.Column(db.String())

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'count': self.count,
        }
