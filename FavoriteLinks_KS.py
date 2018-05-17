import pyautogui as pg
import webbrowser

youtubevideos = ["https://www.youtube.com/watch?v=_xTGsIHRIdA", "https://www.youtube.com/watch?v=EQ1HKCYJM5U"]

disneymovietrailers = ["https://www.youtube.com/watch?v=4sj1MT05lAA", "https://www.youtube.com/watch?v=eh_co0HcHpY"]

answer = pg.prompt(
"""
Which would you rather do?
a)Watch Youtube videos
b)Watch Disney trailers

"""
    )

if answer == "a":
    for i in youtubevideos:
        webbrowser.open(i)

elif answer == "b":
    for i in disneymovietrailers:
        webbrowser.open(i)
    
