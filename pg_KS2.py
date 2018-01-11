import pyautogui as pg
import time
pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('crome\n', .1)
time.sleep (.4)
pg.hotkey('winleft','up')

pg.typewrite('youtube.com\n', .1)
time.sleep (2.5)
pg.typewrite ('failarmy\n', .1)
time.sleep (2.5)
pg.moveTo (387, 517, .3)
pg.click ()
