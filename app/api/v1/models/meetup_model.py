import datetime

meetups = []
rsvp = []


class Meetups(object):
    """Meetup model """

    def __init__(self):
        self.data = meetups

    id = len(meetups)+1
    dateon = str(datetime.date.today())

    @classmethod
    def create_meetup(self, topic, location, images, dateon, tags):
        '''Create meetup dictionry'''
        meetup = {
            'id': self.id,
            'topic': self.topic,
            'location': self.location,
            'image': self.images,
            'dateon': self.dateon,
            'tags': self.tags
        }
        meetups.append(meetup)
        return meetups

    @classmethod
    def rsvp_meetup(self, user_id, meetup_id):
        '''models to RSVP a meetup'''
        rsvp_dict = {
            'user_id': self.user_id,
            'meetup_id': self.meetup_id,
            'scheduled': True
        }
        rsvp.append(rsvp_dict)
        return rsvp

    @classmethod
    def find_meetup(self, id):
        '''A function to find a meetup'''
        try:
            for meetup in meetups:
                if meetup['id'] == id:
                    return meetup
        except:
            return None
