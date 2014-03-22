

class RowProxy(object):
    def __init__(self, *args, **kwargs):
        self.row = ()
        for key in kwargs:
            setattr(self, key, kwargs[key])
            setattr(self, key.lower(), kwargs[key])
            setattr(self, key.upper(), kwargs[key])
        #Add each val in kwargs to self.row tuple
        for key,val in kwargs.items():
            self.row = self.row + (val,)

    def __repr__(self):
        return str(self.row)

    def __str__(self):
        return str(self.row)
