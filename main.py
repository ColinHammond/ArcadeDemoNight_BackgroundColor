import arcade
#use this to open the window, width 800, Height 600
my_window = arcade.open_window(800,600, "First Window Demo")
arcade.set_background_color(arcade.color.GOLD)

arcade.start_render()
#everthing else goes here
arcade.finish_render()

arcade.run()