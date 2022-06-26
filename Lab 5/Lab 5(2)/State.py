from User import *


class State():
    def __init__(self, document):
        self.document = document

    def render(self, user):
        if user.isAdmin or self.document.author == user:
            print(self.document.text)
        else:
            print("você não pode renderizar este documento")

    def publish(self, user):
        pass

    def review(self, user, approved):
        pass

    def expire(self, user):
        pass

    def showState(self):
        print(f'este documento esta no estado {self.__class__.__name__}')

class Draft(State):
    def __init__(self, document):
        super().__init__(document)


    def publish(self, user):
        if user.isAdmin:
            print("Publicado pelo admin")
            self.document.changeState(Published(self.document))
        else:
            print("Publicado por um usuario comum")
            self.document.changeState(Moderation(self.document))


class Moderation(State):
    def __init__(self, document):
        super().__init__(document)

    def review(self, user, approved):
        if user.isAdmin & approved:
            print("Revisao aprovada")
            self.document.changeState(Published(self.document))
        elif user.isAdmin:
            print("Revisao negada")
            self.document.changeState(Draft(self.document))



class Published(State):
    def __init__(self, document):
        super().__init__(document)


    def expire(self,user):
        if user.isAdmin:
            print("O documento expirou")
            self.document.changeState(Draft(self.document))

