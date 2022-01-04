
import operator
import collections

def calculate_score(f, team_points):

    
    with open("sample_input.txt", 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
        for line in lines:
            teams = line.strip('\n').split(',')
            first_team = teams[0][:teams[0].rfind(' ')].lstrip()
            first_team_score = teams[0][teams[0].rfind(' '):].lstrip()
            second_team = teams[1][:teams[1].rfind(' ')].lstrip()
            second_team_score = teams[1][teams[1].rfind(' '):].lstrip()

            # Draw case: score worth 1 point
            if first_team_score == second_team_score:
                first_team_points = second_team_points = 1
            # Win case: winning team score is worth 3 points  losing team score is worth 0 ponits
            elif first_team_score > second_team_score:
                first_team_points = 3
                second_team_points = 0
            elif first_team_score < second_team_score:
                first_team_points = 0
                second_team_points = 3
                
            team_points[first_team] = int(team_points.get(first_team, 0)) + first_team_points # Making use of Python Dictionary get() Method to get the value of first_team
            team_points[second_team] = int(team_points.get(second_team, 0)) + second_team_points# Making use of Python Dictionary get() Method to get the value of second_team
    return team_points

def rank_score(data_file=None):
    team_points = {} # creates dictionary
    team_points = calculate_score([data_file], team_points) #calls the calculate_score function

    team_points = collections.OrderedDict(sorted(team_points.items())) #Dictionary that remebers the order of the keys so that it can print teams out in alphabetical order should some teams have the same score
    team_points = sorted(team_points.items(), key=operator.itemgetter(1), reverse=True)
    score = None
    ranking = None
    counter = 0
    for i, item in enumerate(team_points, start=1):
        i -= counter
        if score == item[1]:
            i = ranking
            counter += 1
        else:
            score = item[1]
        ranking = i
        print(i, item[0], item[1], "pts" if item[1] != 1 else "pt" )

rank_score()
