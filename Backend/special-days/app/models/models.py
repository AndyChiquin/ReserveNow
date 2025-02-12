from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SpecialDay(db.Model):
    __tablename__ = 'special_days'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    event_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))

    def __repr__(self):
        return f"<SpecialDay {self.event_name} on {self.date}>"
