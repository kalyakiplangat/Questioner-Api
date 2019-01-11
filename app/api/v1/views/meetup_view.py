from flask import request, jsonify, make_response
from flask import Blueprint

#local imports 
from ..models.meetup_model import Meetups, meetups

meetupre = Blueprint('meetupre', __name__, url_prefix='/api/v1')

@meetupre.route('/meetup', methods=['POST'])
def post():
    if request.json:
        topic = request.json['topic']
        location = request.json['location']
        images = request.json['images']
        dateon = request.json['dateon']
        tags = request.json['tags']

        results = jsonify(Meetups.create_meetup(topic, location, images, dateon, tags))
        results.status_code = 201
        return results

    else:
        return make_reponse(jsonify({'message':'invalid request'}), 400 )

@meetupre.route('/meetup/upcoming', methods=['GET'])
def get():
    """Get upcoming meetups """
    get_upcoming = {
        'status': 200,
        'data': meetup
        }
    results = jsonify(get_upcoming)
    return results

@meetupre.route('/meetup/<int:id>', methods=['GET'])
def get_specific_meetup(id):
    '''Get a specific meetup'''
    specific_meetup = Meetups.find(id)
    if specific_meetup:
        meetup = {
            'status': 200,
            'data': [specific_meetup]
            }
        results = jsonify(meetup)
        results.status_code = 200
        return results
    else:
        return make_reponse(jsonify({'message':'Resource Not found'}), 404)

@meetupre.route('/meetup/<int:id>/rsvp', methods=['POST'])
def rsvp(id):
    '''RSVP a meetup'''
    if request.json:
        if Meetups.find(id):
            user_id = request.json['user_id']
            meetup = Meetups.rsvp_meetup(user_id, id)
            meetup_resp = {
                'status': 201,
                'data': [meetup]
            }
            results = jsonify(meetup_resp)
            results.status_code = 201
            return results
        else:
            return make_reponse(jsonify({'message':'Resource not found'}), 404)
    else:
        return make_reponse(jsonify({'message':'Invalid request type'}), 400)


