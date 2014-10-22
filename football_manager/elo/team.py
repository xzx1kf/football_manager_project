class Team(object):
    """
    Representation of a team.
    """
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def set_team_name(self, name):
        """
        Set a team name.
        """
        self.name = name

    def set_team_rating(self, rating):
        """
        Set a team rating.
        """
        self.rating = rating
