from flask import Blueprint, request, jsonify
from app.models.models import Event
from datetime import datetime

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/events", methods=["GET"])
def get_events():
    starts_at = request.args.get("starts_at")
    ends_at = request.args.get("ends_at")

    try:
        starts_at = datetime.fromtimestamp(int(starts_at))
        ends_at = datetime.fromtimestamp(int(ends_at))
    except ValueError:
        return (
            jsonify(
                {"error": "Invalid timestamp format. Use Unix timestamp in seconds"}
            ),
            400,
        )

    events = Event.query.filter(
        Event.starts_at >= starts_at,
        Event.ends_at <= ends_at,
        Event.sell_mode == "online",
    ).all()
    result = [
        {
            "id": event.external_id,
            "name": event.name,
            "description": event.description,
            "start_date": event.starts_at.timestamp(),
            "end_date": event.ends_at.timestamp(),
            "sell_mode": event.sell_mode,
        }
        for event in events
    ]

    return jsonify(result)
