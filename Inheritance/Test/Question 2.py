# Question 2 Inheritance testing
# Tissan Kugathas
# ICS4U0
# November 4 2019

# This class is called Stats and it generates the points of the teams
class Stats:

    # constructor which initializes overall variable to 0
    def __init__(self):
        self.overall = 0

    # This function calculates the overall points of the team
    def overallPoints(self,wins,losses,tieds):
        # wins are multiplied by 2 and tieds are multiplied by 1 and losses are multiplied by 0 to get the overall points
        self.overall = (wins*2) + (tieds*1) + (losses*0)
        return self.overall

    # This returns the overall points of the team
    def __repr__(self):
        return "This team's overall points are {}".format(self.overallPoints())

# This class is BaseballTeam and hold the wins, losts, tieds, and returns total points of the team
class BaseballTeam(Stats):

    # constructor which initializes the wins, losts, tieds, and the stats class
    def __init__(self,wins,losses,tieds):
        self.wins = wins
        self.losts = losses
        self.tieds = tieds
        super().__init__()

    # this sets the num of wins
    def setWins(self,num):
        self.wins = num

    # this sets the num of losses
    def setLosses(self,num):
        self.losts = num

    # this sets the num of tieds
    def setTieds(self,num):
        self.tieds = num

    # this calculates and returns the the total points the team has
    def totalPoints(self):
        return self.overallPoints(self.wins,self.losts,self.tieds)

    # this returns information about the team such as the num of wins, nums of losts, nums of tieds, and the overall points
    def __repr__(self):
        return "This team has won {} game(s), lost {} game(s) and tied {} game(s) and has {} point(s)".format(self.wins,self.losts,self.tieds,self.totalPoints())

# This test case shows a baseball team that has 2 wins, 5 losees and 1 tied game
raptors = BaseballTeam(2,5,1)

# prints the information about the baseball team raptors
print(raptors)

# sets the number of wins to 5 for the raptors
raptors.setWins(5)

# prints the information about the baseball team raptors
print(raptors)
