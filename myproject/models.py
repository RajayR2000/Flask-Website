from myproject import db

class Puppy(db.Model):

    __tablename__='puppies'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    owner=db.Column(db.Text)

    def __init__(self,name,owner):
        self.name=name
        self.owner=owner

    def __repr__(self):
        if self.owner:
            return f"My name is {self.name} and my owner is {self.owner}"
        else:
            return f"My name is {self.name} and i don't have an owner yet"
