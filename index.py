from car import Car 
from color_picker import ColorPicker

bumblebee = Car(34, 3, "steel wool")
bumblebee.transformerize("dude",5)
print("bumblebee name=", bumblebee.v_type) 

bumblebee_colors = ColorPicker("yellow", interior="black", pinstripe="turquoise")
print(bumblebee_colors.get_colors())

bumblebee.add_colorscheme(bumblebee_colors)
print(bumblebee.colorscheme.get_colors)