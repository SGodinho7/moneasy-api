from app.app import db


class User(db.Model):
    __tablename__ = 'users'

    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    transaction = db.relationship('Transaction', backref='user')

    @property
    def serialize(self):
        return {
            'id_user': self.id_user,
            'name': self.name,
            'email': self.email,
            'password': self.password,
        }


class Transaction(db.Model):
    __tablename__ = 'transactions'

    id_transaction = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    date = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id_user'))
    id_category = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.id_transaction}, {self.value}, {self.date}, {self.desc}, {self.id_category}, {self.id_user};'

    @property
    def serialize(self):
        return {
            'id_transaction': self.id_transaction,
            'value': self.value,
            'date': self.date,
            'desc': self.desc,
            'id_category': self.id_category,
            'id_user': self.id_user,
        }
