from classes.subscription import Subscription


class Magazine:

    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self.title
    
    @title.setter
    def title(self, title):
        if type(title) == str and not hasattr(self, "title"):
            self._title = title
        else:
            raise Exception
