# Created by: Teddy Sannan & Jack D'Angelo
# Created on: January 2020
# This file is the "Clown Town" game
#   for CircuitPython

import ugame
import stage
import board
import neopixel
import time
import random

import constants

sprites = []

def blank_white_reset_scene():
    # this function is the splash scene game loop

    # do house keeping to ensure everythng is setup

    # set up the NeoPixels
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 5, auto_write=False)
    pixels.deinit() # and turn them all off

    # reset sound to be off
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 160, 120)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1/2 seconds
        time.sleep(0.5)
        mt_splash_scene()

        # redraw sprite list

def mt_splash_scene():
    # this function is the MT splash scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    text = []

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    # get sound ready
    # follow this guide to convert your other sounds to something that will work
    #    https://learn.adafruit.com/microcontroller-compatible-audio-file-conversion
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1 seconds
        time.sleep(3.0)
        game_splash_scene()

        # redraw sprite list

def game_splash_scene():
    # this function is the MT splash scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("sprites.bmp")
    image_bank_3 = stage.Bank.from_bmp16("splash_screen.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    T = stage.Sprite(image_bank_3, 0, 65, 45)
    sprites.append(T)
    
    J = stage.Sprite(image_bank_3, 1, 81, 45)
    sprites.append(J)
    
    G = stage.Sprite(image_bank_3, 2, 40, 63)
    sprites.append(G)
    
    A = stage.Sprite(image_bank_3, 3, 56, 63)
    sprites.append(A)
    
    M = stage.Sprite(image_bank_3, 4, 72, 63)
    sprites.append(M)
    
    E = stage.Sprite(image_bank_3, 5, 88, 63)
    sprites.append(E)
    
    S = stage.Sprite(image_bank_3, 6, 104, 63)
    sprites.append(S)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()
    
    sprites.remove(T)
    sprites.remove(J)
    sprites.remove(G)
    sprites.remove(A)
    sprites.remove(M)
    sprites.remove(E)
    sprites.remove(S)

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 3 seconds
        time.sleep(3.0)
        main_menu_scene()

        # redraw sprite list

def main_menu_scene():
# this function is the MT splash scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("clown.bmp")
    image_bank_3 = stage.Bank.from_bmp16("sprites.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    text = []

    text1 = stage.Text(width=29, height=15, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(40, 10)
    text1.text("Clown Town")
    text.append(text1)

    clown1 = stage.Sprite(image_bank_2, 1, 70, 56)
    sprites.append(clown1)

    clown2 = stage.Sprite(image_bank_2, 2, 70, 72)
    sprites.append(clown2)

    clown3 = stage.Sprite(image_bank_2, 3, 54, 56)
    sprites.append(clown3)

    clown4 = stage.Sprite(image_bank_2, 4, 86, 56)
    sprites.append(clown4)

    clown5 = stage.Sprite(image_bank_2, 5, 54, 72)
    sprites.append(clown5)

    clown6 = stage.Sprite(image_bank_2, 6, 86, 72)
    sprites.append(clown6)

    clown7 = stage.Sprite(image_bank_2, 8, 70, 40)
    sprites.append(clown7)

    clown8 = stage.Sprite(image_bank_2, 0, 54, 40)
    sprites.append(clown8)

    clown9 = stage.Sprite(image_bank_2, 7, 86, 40)
    sprites.append(clown9)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(35, 110)
    text2.text("PRESS START")
    text.append(text2)

    horn_sound = open("horn.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(horn_sound)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = sprites + text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # removes menu clown
    sprites.remove(clown1)
    sprites.remove(clown2)
    sprites.remove(clown3)
    sprites.remove(clown4)
    sprites.remove(clown5)
    sprites.remove(clown6)
    sprites.remove(clown7)
    sprites.remove(clown8)
    sprites.remove(clown9)

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 3 seconds
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_START != 0:  # Start button
            game_scene()

        # redraw sprite list

def game_scene():
    # this function is the game scene
    score = 0

    text = []

    score_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))
    text.append(score_text)

    def show_tomato():
        # make an tomato show up on screen on the x-axis
        for tomato_number in range(len(tomatos)):
            if tomatos[tomato_number].x < 0:
                tomatos[tomato_number].move(random.randint
                                          (0 + constants.SPRITE_SIZE,
                                           constants.SCREEN_X -
                                           constants.SPRITE_SIZE),
                                          constants.OFF_TOP_SCREEN)
                break

    def show_pie():
        for pie_number in range(len(pies)):
            if pies[pie_number].x < 0:
                pies[pie_number].move(random.randint
                                          (0 + constants.SPRITE_SIZE,
                                           constants.SCREEN_X -
                                           constants.SPRITE_SIZE),
                                          constants.OFF_TOP_SCREEN)
                break

    def show_balloon():
        for balloon_number in range(len(balloons)):
            if balloons[balloon_number].x < 0:
                balloons[balloon_number].move(random.randint
                                          (0 + constants.SPRITE_SIZE,
                                           constants.SCREEN_X -
                                           constants.SPRITE_SIZE),
                                          constants.OFF_TOP_SCREEN)
                break

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("sprites.bmp")

    splat_sound = open("splat.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    tomatos = []
    pies = []
    balloons = []

    # drops tomatos 
    for tomato_number in range(constants.TOTAL_NUMBER_OF_TOMATOS):
        a_single_tomato = stage.Sprite(image_bank_2, 3,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        tomatos.append(a_single_tomato)

    show_tomato()
    
    # drops pie
    for pie_number in range(constants.TOTAL_NUMBER_OF_PIES):
        a_single_pie = stage.Sprite(image_bank_2, 4,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        pies.append(a_single_pie)

    show_pie()
    
    # drops balloon
    for balloon_number in range(constants.TOTAL_NUMBER_OF_BALLOONS):
        a_single_balloon = stage.Sprite(image_bank_2, 5,
                                      constants.OFF_SCREEN_X,
                                      constants.OFF_SCREEN_Y)
        balloons.append(a_single_balloon)

    show_balloon()

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    clown = stage.Sprite(image_bank_2, 2, 74, 56)
    sprites.insert(0, clown)  # insert at the top of sprite list

    # create a stage for the background to show up
    # setting the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # setting the layers to show them in order
    game.layers = text + sprites + pies + tomatos + balloons + [background]
    # rendering the background and the locations of the sprites
    game.render_block()

    # repeat forever game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_RIGHT != 0:
            if clown.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                clown.move(constants.SCREEN_X - constants.SPRITE_SIZE, clown.y)
            else:
              
                clown.move(clown.x + constants.CLOWN_SPEED, clown.y)

        if keys & ugame.K_LEFT != 0:
            if clown.x < 0:
                clown.move(0, clown.y)
            else:
              
                clown.move(clown.x - constants.CLOWN_SPEED, clown.y)

        if keys & ugame.K_UP != 0:
            if clown.y < 0:
                clown.move(clown.x, 0)
            else:
              
                clown.move(clown.x, clown.y - constants.CLOWN_SPEED)

        if keys & ugame.K_DOWN != 0:
            if clown.y > constants.SCREEN_Y - constants.SPRITE_SIZE:
                clown.move(clown.x, constants.SCREEN_Y - constants.SPRITE_SIZE)
            else:
              
                clown.move(clown.x, clown.y + constants.CLOWN_SPEED)

        # resets tomato    
        for tomato_number in range(len(tomatos)):
            if tomatos[tomato_number].x > 0:
                tomatos[tomato_number].move(tomatos[tomato_number].x,
                                          tomatos[tomato_number].y +
                                          constants.TOMATO_SPEED)
                if tomatos[tomato_number].y > constants.SCREEN_Y:
                    tomatos[tomato_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
                    score += 1
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))
                    game.render_block()
                    show_tomato()

        # resets pie
        for pie_number in range(len(pies)):
            if pies[pie_number].x > 0:
                pies[pie_number].move(pies[pie_number].x,
                                          pies[pie_number].y +
                                          constants.PIE_SPEED)
                if pies[pie_number].y > constants.SCREEN_Y:
                    pies[pie_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
                    show_pie()

        # resets pie
        for balloon_number in range(len(balloons)):
            if balloons[balloon_number].x > 0:
                balloons[balloon_number].move(balloons[balloon_number].x,
                                          balloons[balloon_number].y +
                                          constants.BALLOON_SPEED)
                if balloons[balloon_number].y > constants.SCREEN_Y:
                    balloons[balloon_number].move(constants.OFF_SCREEN_X,
                                              constants.OFF_SCREEN_Y)
                    show_balloon()

        # collision with tomato
        for tomato_number in range(len(tomatos)):
            if tomatos[tomato_number].x > 0:
                if stage.collide(tomatos[tomato_number].x + 1,
                                 tomatos[tomato_number].y,
                                 tomatos[tomato_number].x + 15,
                                 tomatos[tomato_number].y + 15,
                                 clown.x, clown.y, clown.x + 15, clown.y + 15):
                    sound.stop()
                    sound.play(splat_sound)
                    time.sleep(2.0)
                    sound.stop()
                    sprites.remove(clown)
                    game_over_scene(score)
                    
        # collision with pie
        for pie_number in range(len(pies)):
            if pies[pie_number].x > 0:
                if stage.collide(pies[pie_number].x + 1,
                                 pies[pie_number].y,
                                 pies[pie_number].x + 15,
                                 pies[pie_number].y + 15,
                                 clown.x, clown.y, clown.x + 15, clown.y + 15):
                    sound.stop()
                    sound.play(splat_sound)
                    time.sleep(2.0)
                    sound.stop()
                    sprites.remove(clown)
                    game_over_scene(score)
                    
        # collision with balloon
        for balloon_number in range(len(balloons)):
            if balloons[balloon_number].x > 0:
                if stage.collide(balloons[balloon_number].x + 1,
                                 balloons[balloon_number].y,
                                 balloons[balloon_number].x + 15,
                                 balloons[balloon_number].y + 15,
                                 clown.x, clown.y, clown.x + 15, clown.y + 15):
                    sound.stop()
                    sound.play(splat_sound)
                    time.sleep(2.0)
                    sound.stop()
                    sprites.remove(clown)
                    game_over_scene(score)

        # update game logic

        # redraw sprite list
        game.render_sprites(sprites + pies + tomatos + balloons)
        game.tick()  # wait until refresh rate finishes

def game_over_scene(final_score):
    # this function is the game over scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("sprites.bmp")
    
    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    text = []
    
    text1 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(22, 20)
    text1.text("Final Score: {:0>2d}".format(final_score))
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(43, 60)
    text2.text("GAME OVER")
    text.append(text2)

    text3 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text3.move(32, 110)
    text3.text("PRESS SELECT")
    text.append(text3)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
   
    # set the background layer
    game.layers = text + [background]
    
    # render the background
    # most likely you will only render background once per scene
    game.render_block()

    # Game loop
    while True:
        # Update game logic
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_SELECT != 0:
            keys = 0
            main_menu_scene()


if __name__ == "__main__":
    blank_white_reset_scene()
