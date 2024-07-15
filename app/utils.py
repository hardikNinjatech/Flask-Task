# app/utils.py
def serialize_event(event):
    return {
        "id": event.event_id,
        "name": event.name,
        "description": event.description,
        "starts_at": event.starts_at.isoformat(),
        "ends_at": event.ends_at.isoformat(),
        "sell_mode": event.sell_mode,
        "last_updated": event.last_updated.isoformat(),
    }
