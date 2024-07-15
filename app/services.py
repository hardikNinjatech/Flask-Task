# app/services.py
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
from app.models import Event
from app import db


def fetch_events():
    url = "https://provider.code-challenge.feverup.com/api/events"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            root = ET.fromstring(response.content)

            for base_event_xml in root.findall(".//base_event"):
                external_id = int(base_event_xml.attrib["base_event_id"])
                name = base_event_xml.attrib.get("title", "")  # Adjusted to use 'title'

                event_xml = base_event_xml.find(".//event")
                description = event_xml.attrib.get(
                    "description", ""
                )  # Adjusted to use 'description'

                # Parsing start_date and end_date with robust error handling
                start_date_str = event_xml.attrib["event_start_date"]
                end_date_str = event_xml.attrib["event_end_date"]

                try:
                    start_date = datetime.strptime(
                        start_date_str[:19], "%Y-%m-%dT%H:%M:%S"
                    )  # Truncate microseconds
                    end_date = datetime.strptime(
                        end_date_str[:19], "%Y-%m-%dT%H:%M:%S"
                    )  # Truncate microseconds
                except ValueError as e:
                    print(f"Error parsing date: {e}. Skipping event.")
                    continue  # Skip this event if date parsing fails

                sell_mode = base_event_xml.attrib["sell_mode"]
                last_updated = datetime.now()

                # Check if event already exists in the database
                event = Event.query.filter_by(external_id=external_id).first()
                if event:
                    # Update existing event
                    event.name = name
                    event.description = description
                    event.starts_at = start_date  # Adjusted to starts_at
                    event.ends_at = end_date  # Adjusted to ends_at
                    event.sell_mode = sell_mode
                    event.last_updated = last_updated
                else:
                    # Create new event
                    event = Event(
                        external_id=external_id,
                        name=name,
                        description=description,
                        starts_at=start_date,  # Adjusted to starts_at
                        ends_at=end_date,  # Adjusted to ends_at
                        sell_mode=sell_mode,
                        last_updated=last_updated,
                    )
                    db.session.add(event)

            db.session.commit()
            print("Events fetched and saved successfully.")
        else:
            print(f"Failed to fetch events. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching or saving events: {str(e)}")
