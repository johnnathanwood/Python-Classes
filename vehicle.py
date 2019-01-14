class Vehicle:

    def __init__(self, v_type="vehicle"):
        self.name = "Vehicle"
        self.v_type = v_type
        self.is_transformed = False

    def add_wheels(self, wheel_num):
        self.wheels = wheel_num

    def add_rocket(self, rocket_num):
        self.rocket = rocket_num

    def transformerize(self, bot_name, rocket_num):
        self.add_rocket(rocket_num)
        self.wheels = 0
        self.is_transformed = True
        self.bot_name = bot_name


    def __str__(self):
        return f'This vehicle\'s name is {self.name}'

    def add_colorscheme(self, colorsObj):
        self.colorscheme = colorsObj
