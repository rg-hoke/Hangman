# Eigene Funktionen
import pygame as pg

def my_rectangles(screen, fill, border, color_back, color_border, posx, posy, width, height):
    if fill is True:
        pg.draw.rect(screen, color_back, [posx, posy, width, height], 0)  # ausgefüllt
    if border is True:
        pg.draw.rect(screen, color_border, [posx, posy, width, height], 1)  # Umrandung

def my_center_text(screen,centerX,centerY,font,fontsize,nachricht,antialias,color,bold,x,y,laenge,hoehe):
    myfont = pg.font.SysFont(font, fontsize,bold,False)
    mytext = myfont.render(nachricht, antialias, color)
    textKasten= mytext.get_rect()

    x2,y2 = textKasten.center
    x2 = x + (laenge / 2) if centerX else x + x2
    y2 = y + (hoehe / 2)  if centerY else y + y2
    textKasten.center = (x2, y2)

    screen.blit(mytext, textKasten)

def my_textausgabe(text,werte): #screen,center,antialias,color,backcolor,font,fontsize,bold,italic,x,y,laenge,hoehe):
    screen,centerX,centerY,antialias,color,backcolor,font,fontsize,bold,italic,x,y,laenge,hoehe = werte
    my_rectangles(screen,True,False,backcolor,(0, 0, 0),x,y,laenge,hoehe)

    my_center_text(screen,centerX,centerY,font,fontsize,text,antialias,color,bold,x,y,laenge,hoehe)

def draw_button(werte,aktiv=False):
    # (screen, bx, by, nachricht, font, fontsize,laenge, hoehe, farbe_normal, farbe_aktiv)
    screen, bx, by, nachricht, font, fontsize, laenge, hoehe, farbe_normal, farbe_aktiv = werte
    if aktiv:
        my_rectangles(screen, True, True, farbe_aktiv, (0,0,0), bx, by, laenge, hoehe)
    else:
        my_rectangles(screen, True, True, farbe_normal, (0,0,0), bx, by, laenge, hoehe)

    my_center_text(screen,True,True,font, fontsize, nachricht, True, (0,0,0),False, bx, by, laenge, hoehe)

def draw_slider(val,werte,inkrement=0):
    screen, x, y, w, h , border_color, back_color, wmin, wmax, step = werte
    val += step * inkrement
    if val < wmin: val = wmin
    if val > wmax: val = wmax

    pos = (val-wmin)*100/(wmax-wmin)
    #(screen, fill, border, color_back, color_border, posx, posy, width, height)
    my_rectangles(screen, True, True, back_color,  border_color,       x,    y, w,      h) # Umrahmung
    my_rectangles(screen, True, False,border_color,border_color,     x+5, y+14, w-13,   2) # Mittellinie
    my_rectangles(screen, True, False,border_color,border_color, x+5+pos,  y+5, 8,   h-10) # Slider
    return val