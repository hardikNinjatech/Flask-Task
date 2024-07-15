from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime
import atexit
from flask import current_app
from app.services import fetch_events


def start_scheduler(app):
    scheduler = BackgroundScheduler()
    scheduler.start()

    @scheduler.scheduled_job(
        IntervalTrigger(minutes=5, seconds=5),
        id="fetch_events_job",
        name="Fetch events every 5 minutes and 5 seconds",
    )
    def scheduled_job():
        with app.app_context():
            fetch_events()
            current_app.logger.info("Fetched events at: %s", datetime.now())

    atexit.register(lambda: scheduler.shutdown())
