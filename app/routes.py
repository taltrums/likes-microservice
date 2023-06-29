from flask import request, jsonify
from app import app, cache, Session
from app.models import Like
from app.utils import get_total_likes, send_notification

# Store Like event
@app.route('/likes', methods=['POST'])
def store_like():
    data = request.json
    user_id = data.get('user_id')
    content_id = data.get('content_id')

    # Save like event to the database
    session = Session()
    like = Like(user_id=user_id, content_id=content_id)
    session.add(like)
    session.commit()
    session.close()

    # Check if the number of likes for the content has reached 100
    total_likes = get_total_likes(content_id)
    if total_likes >= 100:
        send_notification(content_id)

    return jsonify({'message': 'Like event stored successfully'})


# Check if user has liked a particular content
@app.route('/likes/check', methods=['GET'])
def check_like():
    data = request.json
    user_id = data.get('user_id')
    content_id = data.get('content_id')

    # Query the database to check if the user has liked the content
    session = Session()
    like = session.query(Like).filter_by(user_id=user_id, content_id=content_id).first()
    session.close()

    print(like)

    if like:
        return jsonify({'liked': True})
    else:
        return jsonify({'liked': False})


# Total likes for a content
@app.route('/likes/total', methods=['GET'])
@cache.cached(timeout=60)  # Cache the response for 60 seconds
def total_likes():
    data = request.json
    content_id = data.get('content_id')

    # Query the database to get the total likes for the content
    session = Session()
    total_likes = session.query(Like).filter_by(content_id=content_id).count()
    session.close()

    return jsonify({'total_likes': total_likes})
