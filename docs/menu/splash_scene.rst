.. _splash_scene:

Splash Scene
============

In the splash scene we start with the MT Game Studio splash scene which transciosns to the TJ Game splash scene after 3 seconds.

```
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

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    text = []

    text1 = stage.Text(width=29, height=15, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(50, 60)
    text1.text("TJ Games")
    text.append(text1)

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
```

.. container:: twocol

  .. container:: leftside

    .. image:: ./images/mt.jpg
      :width: 320 px
      :height: 240 px
      :alt: PyBadge
      :align: left

  .. container:: rightside

|
|
|
|
|
|
|

.. container:: twocol

  .. container:: leftside

    .. image:: ./images/tj.jpg
      :width: 320 px
      :height: 240 px
      :alt: USB Cable
      :align: left

  .. container:: rightside
