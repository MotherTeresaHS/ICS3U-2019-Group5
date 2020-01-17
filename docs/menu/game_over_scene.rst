.. _game_over_scene:

Game Over Scene
===============

If you get hit by any of the objects the game makes a splat sound and takes you to the game over scene, where it gives you you final score and to press start if you wish to play again.

.. code-block:: python
  :linenos:
  
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
      game.layers = sprites + text + [background]
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
              
.. container:: twocol

  .. container:: leftside

    .. image:: ./images/gm.jpg
      :width: 320 px
      :height: 240 px
      :alt: PyBadge
      :align: left

  .. container:: rightside
