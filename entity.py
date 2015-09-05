

class Entity:
    def __init__(self, description, verbose_description):
        self.description = description
        self.verbose_description = verbose_description

    def get_description(self):
        return self.description

    def get_description_verbose(self):
        return self.verbose_description
