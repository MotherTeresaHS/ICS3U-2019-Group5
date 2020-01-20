.. _game:

****
Game
****

This is where we started to make the actual game itself we first started by creating our background and placing our sprites, where we than procceded to make our sprite move accross the screen, as well as setting a border for it to not to escape the screen. We than procceded to spawn objects and make them fall down from the top of the screen. We later than used for loops and if statements to make objects respawn randomly at the top of the screen, and finally we added a scoring system that increases by one every time you complete a wave.

.. code-block:: python
  :linenos:
  
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
  
          # resets tomatos and adds score
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
  
          # resets pies
          for pie_number in range(len(pies)):
              if pies[pie_number].x > 0:
                  pies[pie_number].move(pies[pie_number].x,
                                            pies[pie_number].y +
                                            constants.PIE_SPEED)
                  if pies[pie_number].y > constants.SCREEN_Y:
                      pies[pie_number].move(constants.OFF_SCREEN_X,
                                                constants.OFF_SCREEN_Y)
                      show_pie()
  
          # resets balloons
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

.. toctree::
   :maxdepth: 1
   :glob:

   Background <background>
   Clown <space_ship>
