import pygame as pg
import random as rnd

pg.init()
import myFunctions as myF

clock   = pg.time.Clock()
fps     = 20
size    = [620,620]

statuswert = ["Neustart", "Neu Easy", "Run", "Aufgegeben", "Verloren", "Gewonnen"]
status     = statuswert[0]
gameende   = False
buchstaben = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Picture = []
maxversuche = 11
versuche = 0

aktiv   = False
cnt     = 0

# genutzte Farbe
ORANGE    = (255,140,  0)
RED       = (255,  0,  0)
BLUE      = (  0,  0,255)
LIGTHBLUE1= (  3,200,255)
LIGTHBLUE2= (  3,150,255)
GREEN     = (  0,255,  0)
YELLOW    = (200,200, 50)
BLACK     = (  0,  0,  0)
WHITE     = (255,255,255)
GRAY      = (128,128,128)
LIGHTGRAY = (240,240,240)

screen = pg.display.set_mode(size)
pg.display.set_caption("Hangman")
screen.fill(YELLOW)

#Picture = pg.transform.scale(pg.image.load("image/myHangman0.png"), (620,470))
def ladeBild(dateiname):
  return pg.transform.scale(pg.image.load(dateiname), (620, 470))

for n in range(11):
    Picture.append(ladeBild(f'image/myHangman{n}.png'))

textfeld = [#screen,centerX,CenterY,antialias,color,backcolor,font,fontsize,bold,italic,x,y,laenge,hoehe
    [screen,True,True,True,BLACK,WHITE, 'Consolas',18,False,False,  0,470,620,35],
    [screen,True,True,True,BLACK,YELLOW,'Consolas',15,False,False,  0,510,200,25],
    [screen,True,True,True,BLACK,YELLOW,'Consolas',15,False,False,205,510,415,25],
]

button = [#screen, bx, by,  nachricht, font, fontsize,laenge, hoehe, farbe_normal, farbe_aktiv
    [screen, 470, 540, "Neustart", 'Consolas', 12, 70, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 550, 540, "Neu Easy", 'Consolas', 12, 60, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 470, 575, "Aufgabe",  'Consolas', 12, 70, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 550, 575, "Beenden",  'Consolas', 12, 60, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen,  10, 540, "A", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen,  45, 540, "B", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen,  80, 540, "C", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 115, 540, "D", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 150, 540, "E", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 185, 540, "F", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 220, 540, "G", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 255, 540, "H", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 290, 540, "I", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 325, 540, "J", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 360, 540, "K", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 395, 540, "L", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 430, 540, "M", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen,  10, 575, "N", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen,  45, 575, "O", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen,  80, 575, "P", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 115, 575, "Q", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 150, 575, "R", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 185, 575, "S", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 220, 575, "T", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 255, 575, "U", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 290, 575, "V", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 325, 575, "W", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 360, 575, "X", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 395, 575, "Y", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
    [screen, 430, 575, "Z", 'Consolas', 15, 30, 30, LIGTHBLUE2,LIGTHBLUE1],
]
           #screen, x, y, with, hight, border_color, back_color,valmin,valmax,step
#slider = [screen,635,350,120,30,BLACK,YELLOW,0,100,10]
#myF.draw_slider(cnt,slider)

def start(maxversuche):
    with open("Woerter.txt") as f:
        wort = rnd.choice([w.strip().upper() for w in f])
    versuche, gesucht, geraten = maxversuche, set(b for b in wort), set()
    return wort, versuche, gesucht, geraten

#Hauptschleife zum Bildschirmzeichnen und zur Auswertung der Ereignisse
while status != "quitt":
    if status == "Neustart" or status == "Neu Easy":
        if status=="Neustart":
            maxversuche = 7
            versuchoffset = 3
        if status=="Neu Easy":
            maxversuche = 10
            versuchoffset = 0
        wort, versuche, gesucht, geraten = start(maxversuche)
        status = "Run"
        gameende = False

    # Spielfeld/figuren zeichnen
    if status == "Aufgegeben":
        screen.blit(Picture[10], (0,0))
    else:
        screen.blit(Picture[maxversuche - versuche + versuchoffset], (0,0))

    # Events auswerten
    for event in pg.event.get():
        # wenn Fenster geschlossen wird
        if event.type == pg.QUIT: status = "quitt"
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE: status = "quitt"

        x,y = pg.mouse.get_pos()
        klick = pg.mouse.get_pressed()
        for i in button:
            # bx = i[1], by = i[2], laenge = i[6], hoehe  = i[7]
            if x > i[1] and x <i[1] + i[6] and y > i[2] and y < i[2] + i[7]:
                myF.draw_button(i,True)
                if klick[0] == 1 and aktiv == False:
                    aktiv = True
                    if i[3]   == "Neustart": status = "Neustart"
                    if i[3]   == "Neu Easy": status = "Neu Easy"
                    elif i[3] == "Aufgabe" and status == "Run":
                        status = "Aufgegeben"
                        gameende = True
                        break
                    elif i[3] == "Beenden": status = "quitt"
                    if not gameende and status == "Run":
                        for char in buchstaben:
                            if i[3]==char:
                                geraten.add(char)
                                if char not in gesucht: versuche -= 1
                                if gesucht.issubset(geraten) or versuche == 0:
                                    gameende = True
                                    break
                if klick[0] == 0:
                    aktiv = False
            else:
                myF.draw_button(i,False)

    if gameende and status == "Run":
        if versuche > 0:
            text = f"GEWONNEN! Das gesuchte Wort war: {wort}"
            status = "Gewonnen"
        else:
            text = f"VERLOREN! Das gesuchte Wort war: {wort}"
            status = "Verloren"
    elif gameende and status == "Aufgegeben":
        text = f"Aufgegeben! Das gesuchte Wort war: {wort}"
        gameende = True
    elif not gameende:
        text = 'Wort: ' + ' '.join([f"{b if b in geraten else '_'}" for b in wort])

    #myF.my_textausgabe(f"Status: {status:>10s}", textfeld[0])
    myF.my_textausgabe(text, textfeld[0])
    myF.my_textausgabe(f"Du hast noch {versuche} Versuche", textfeld[1])
    myF.my_textausgabe(f"Verwendete Buchstaben: {''.join(geraten)}", textfeld[2])

    pg.display.flip()
    clock.tick(fps)
pg.quit()
