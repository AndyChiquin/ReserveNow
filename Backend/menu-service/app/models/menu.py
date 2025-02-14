from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Notification(db.Model):
    __tablename__ = 'Notifications' 

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False) 
    message = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)

   
    user = db.relationship('User', backref=db.backref('notifications', lazy=True))

    def __init__(self, user_id, message, date, status):
        self.user_id = user_id
        self.message = message
        self.date = date
        self.status = status

    def __repr__(self):
        return f'<Notification {self.id} for User {self.user_id}>'
