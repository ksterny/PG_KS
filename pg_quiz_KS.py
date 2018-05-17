import pyautogui as pg
import time
import webbrowser 

points = 0

# Question

answer = pg.prompt(
"""
What trait do your friends describe you as?

a) Loyal
b) Playful
c) Clumsy
d) Always asleep

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4

# Question 2

answer = pg.prompt(
"""
What do you like to do?

a) Playing outside
b) Going on a walk
c) Hunting
d) Sleeping

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4

# Question 3

answer = pg.prompt(
"""
What do you want to eat?

a) Steak
b) Anything that is edible
c) Apples
d) Fancy foods

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4

# Question 4

answer = pg.prompt(
"""
What is your favorite toy?

a) Stuffed Animals
b) Toys with noises 
c) Light up ball 
d) None of these

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4

# Question 5

answer = pg.prompt(
"""
What is your favorite animal?

a) Dogs
b) Squirrels
c) Ducks
d) Mice

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4

# END OF SURVEY

pg.alert ("you are...")

# Golden Retriever
if points < 9:
    pg.alert("Golden Retriever")
    webbrowser.open("http://www.golfian.com/wp-content/uploads/2016/06/Cute-Golden-Retriever-Dog-Playing-With-Bubbles.jpg")
    
# English Springer Spaniel
elif points >= 9 and points < 13:
    pg.alert("English Springer Spaniel")
    webbrowser.open("https://t00.deviantart.net/Hc3dpO-enzspikMZURYofaAaJ_k=/fit-in/700x350/filters:fixed_height(100,100):origin()/pre00/c9bc/th/pre/i/2010/067/b/9/flying_dawwg_by_njt_rasta.jpg")

# Blood Hound
elif points >= 13 and points < 17:
    pg.alert("Blood Hound")
    webbrowser("http://www.dogbreedslist.info/uploads/allimg/dog-pictures/Bloodhound-3.jpg")

# Maine Coon
elif points >= 17 and points < 20:
    pg.alert("Maine Coon")
    webbrowser("https://orig00.deviantart.net/2954/f/2010/159/5/2/maine_coon_sleeping_by_talashira.jpg")
