"""This module is related to actor objects."""

class Actor(object):
    """The Actor class contains information about actors."""

    def __init__(self, first_name, last_name):
        """Creates the displayed name by combining the first and last names.
        This could be better, but this class is only intended to be an example
        of creating a class, so it's fine."""

        self.set_name(first_name, last_name)

    def get_name(self):
        """Get the name of the actor."""
        return self.name

    def set_name(self, first_name, last_name):
        """"Set the name of the actor."""
        self.name = first_name + " " + last_name
