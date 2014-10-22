from team import Team
from elo import Result, EloFootballRating

team_a = Team("Team A", 630)
team_b = Team("Team B", 500)

rating_system = EloFootballRating(20)
p = rating_system.calculate(team_a.rating, team_b.rating, 2, Result.WIN)

print "Original Rating %f" % team_a.rating
print "Points gained: %f" % p
print "New rating is: %f" % (team_a.rating + p)
