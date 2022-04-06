def p_decorate(func):
    def add_interjection(*args, **kwargs):
        '''adiciona a interjeição hmmmmmm... no início'''
        return "hmmmmmm...{0}".format(func(*args, **kwargs))
    return add_interjection


class Food(object):

    def __init__(self, food):
        self.name = food

    @p_decorate
    def compliment_food(self,*args, **kwargs) :
        '''fala sobre a comida'''
        statement = "this "+self.name+" is"
        for arg in args:
            statement = statement+" "+arg
        statement = "{0}\nQualities:".format(statement)
        for key in kwargs.keys():
            statement = statement+"\n"+key+":"+kwargs[key]
        return statement


my_lunch = Food("lunch")

print (my_lunch.compliment_food("very", "good", salt="right amount", temperature="hot", spicy="great"))