from sys import maxsize

class Project:

    def __init__(self, name=None, status=None, description=None, id=None):
        self.name = name
        self.status = status
        self.description = description
        self.id = id

    def __eq__(self, other):
        return self.name == other.name and self.status == other.status and self.description == other.description

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    #пишем правило (ключ для сравнения) если присвоено id, то берем его, если None, то maxsize
    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

