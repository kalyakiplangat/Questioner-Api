import

meetup = []

class Meetups(object):
    def __init__(self):
        self.data = meetup

    def create_meetup(self, created0n, createdby, location, tags):
        self.createdon = created0n
        self.createdby = createdby
        self.location = location
        self.tags = tags

    