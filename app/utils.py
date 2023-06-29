from app.models import Like
from app import app, cache, Session


def send_notification(content_id):
    # Replace with your actual notification implementation
    print(f"Notification: Content with ID {content_id} has reached 100 likes!")

def get_total_likes(content_id):
    # Query the database to get the total likes for the content
    session = Session()
    total_likes = session.query(Like).filter_by(content_id=content_id).count()
    session.close()
    return total_likes