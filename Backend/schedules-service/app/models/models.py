from app.config.settings import db
from sqlalchemy import Column, Integer, String, Time, ForeignKey
from sqlalchemy.orm import relationship

class Schedule(db.Model):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, autoincrement=True)
    day_of_week = Column(String(20), nullable=False)
    opening_time = Column(Time, nullable=False)
    closing_time = Column(Time, nullable=False)
    special_day_id = Column(Integer, ForeignKey("special_days.id"), nullable=True)

    # Relación con SpecialDays
    special_day = relationship("SpecialDay", back_populates="schedules")

    def __init__(self, day_of_week, opening_time, closing_time, special_day_id=None):
        self.day_of_week = day_of_week
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.special_day_id = special_day_id
