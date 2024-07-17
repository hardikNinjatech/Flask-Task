# app/models.py
from .. import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(
        db.Integer, unique=True, nullable=False
    )  # Adjusted to external_id
    name = db.Column(db.String(255), nullable=False)  # Specify length for String
    description = db.Column(
        db.String(1000), nullable=True
    )  # Adjusted with a length limit
    starts_at = db.Column(db.DateTime, nullable=False)
    ends_at = db.Column(db.DateTime, nullable=False)
    sell_mode = db.Column(db.String(50), nullable=False)  # Specify length for String
    last_updated = db.Column(db.DateTime, nullable=False)
