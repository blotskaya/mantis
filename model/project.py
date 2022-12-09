class Project:
    def __init__(self, name=None, description=None, status=None, viewstate=None):
        self.name = name
        self.description = description
        self.status = status
        self.viewstate = viewstate

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.name, self.status, self.viewstate, self.description)

    def __eq__(self, other):
        return (self.name == other.name and self.description == other.description and self.status == other.status
                and self.viewstate == other.viewstate)

