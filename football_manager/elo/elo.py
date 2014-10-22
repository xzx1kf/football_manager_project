class Result(object):
    """
    A Result can either be a win, lose or draw. A numerical value is
    assigned to the result.
    """
    WIN, LOSE, DRAW = 1, 0, 0.5


class EloFootballRating(object):
    """
    A rating system based on the Elo rating system but modified to take
    various football specific variables into account.
    """
    def __init__(self, k_factor):
        self.k_factor = k_factor

    @staticmethod
    def get_goal_difference_index(goal_difference):
        """
        The number of goals is taken into account by use of
        a goal difference index (g).

        g = 1 if the game is a draw or is won by one goal.
        g = 1.5 if the game is won by two goals.
        g = (11 + n) / 8 if the game is won by three or more goals.
        Where n is the goal difference.
        """
        if goal_difference <= 1:
            return 1
        elif goal_difference == 2:
            return 1.5
        else:
            return (11.0 + goal_difference) / 8.0

    @staticmethod
    def get_expected_result(home_rating, away_rating):
        """
        Calculate the expected result based on the current ratings
        of the home team and away team.
        """
        rating_diff = away_rating - home_rating
        rating_diff = 10 ** (rating_diff / 400.0)
        return 1 / (rating_diff + 1)

    def calculate(
            self,
            home_rating,
            away_rating,
            goal_difference,
            result):
        """
        Calculates a new elo rating based off the result of the match
        between a home team and away team.
        """
        goal_difference_index = self.get_goal_difference_index(goal_difference)
        expected_home_result = self.get_expected_result(
            home_rating,
            away_rating)
        chance = result - expected_home_result

        return goal_difference_index * self.k_factor * chance
