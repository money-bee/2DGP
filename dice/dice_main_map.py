from pico2d import *

import All_Class

import random


def handle_events():
    global running
    global turn
    global dice_count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if(550<event.x<650 and 390<event.y<460):
               dice_count +=1

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False





open_canvas(1200,680)

map1= All_Class.Map_board()
dice_L = All_Class.Dice_L()
dice_R = All_Class.Dice_R()
dice_back = All_Class.Dice_Back1()
dice_back2 = All_Class.Dice_Back2()
dice_count = 1


turn = False
running = True


while running:
    handle_events()
    clear_canvas()
    if( dice_count %2 ==0):
        dice_L.update()
        dice_R.update()

    map1.draw()
    if(dice_count%2 ==1):
         dice_back.draw()
    else:
        dice_back2.draw()
    dice_L.draw()
    dice_R.draw()

    update_canvas()

    delay(0.05)





close_canvas()


