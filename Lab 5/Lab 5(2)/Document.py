from State import *
from User import *

class Document():
    def __init__(self, text, author):
        self.text = text
        self.state = Draft(self)
        self.author = author

    def render(self, user):
        self.state.render(user)

    def publish(self, user):
        self.state.publish(user)

    def review(self, user, approved):
        self.state.review(user, approved)

    def expire(self, user):
        self.state.expire(user)

    def showState(self):
        self.state.showState()

    def changeState(self, state):
        self.state = state