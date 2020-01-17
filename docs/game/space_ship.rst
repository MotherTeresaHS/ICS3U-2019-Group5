.. _space_ship:

Clown
==========

For our main character we created a simple 16x16 clown sprite which we than just placed at the center of the screen when the user presses start from the menu screen. We spawned our sprite using a simple statement and placing its coordinates.

.. code-block:: python
  :linenos:
  
    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("sprites.bmp")
    
    clown = stage.Sprite(image_bank_2, 2, 74, 56)
    sprites.insert(0, clown)  # insert at the top of sprite list
