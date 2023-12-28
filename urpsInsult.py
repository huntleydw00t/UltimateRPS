
from random import randint

#Insult function creation
#This will implemented but there will be a further menu choice also added to play in clean mode or fucked up mode
#There will two things here there will be computer player insulting user and judge insulting the user (for this version only when
#player loses more will be added for winning in version 0.0.3)

def judge_insult():

    jInsult = ["Really that's the best you can fucking do? It's gunna be a long game.", 
               "Son of a bitch why am I judging a loser.", 
               "Dang that chick is hot. Oh you lost again big fucking suprise.",
               "Loser! Your mother was a hamster, and your father smelt of elderberries!",
               "I once saw my dog eat his own shit.  Watching you play is way worse then that.",
               "If I had a face like yours, I'd sue my parents.",
               "Your birth certificate is an apology letter from the condom factory.",
               "Hey you did your best but, well you suck",
               "I am jealous of people that don't know you!",
               "Brains aren't everything. In your case they're nothing.",
               "I don't know what makes you so stupid, but it really works."]
    return jInsult[randint(0,10)]
