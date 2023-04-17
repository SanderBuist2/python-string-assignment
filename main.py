# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scoringPlayer1 = "Ruud Gullit"
scoringPlayer2 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = scoringPlayer1 + " " + str(goal_0) + ", " + scoringPlayer2 + " " + str(goal_1)

report = scoringPlayer1 + " scored in the " + str(goal_0) + "nd minute\n" + scoringPlayer2  + " scored in the " + str(goal_1) + "th minute"

player = scoringPlayer1

first_name = player[0:player.find(" ")]
last_name_len = len(player[player.find(" ")+1:])

name_short = first_name[0:1] + ". " + player[player.find(" ")+1:]

chant_temp = (first_name + "! ") * len(first_name)
chant = chant_temp[0:-1]

good_chant = chant[-1] != " "
