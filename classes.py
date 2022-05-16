from globals import *


class WaterIndoorPlants():

    def __init__(self):
        self.title = 'Water Indoor Plants'
        self.description = 'Check if there is water under the vase'
        self.frequency = WEEKLY
        self.interval = 1
        self.on_days = FRIDAY


class WaterLechuza():

    def __init__(self):
        self.title = 'Water Lechuza'
        self.description = ''
        self.frequency = WEEKLY
        self.interval = 1
        self.on_days = FRIDAY


class WashTowels():

    def __init__(self):
        self.title = 'Wash Towels and Accappatoio'
        self.description = 'Program is Sintetico + Asciugatrice'
        self.frequency = WEEKLY
        self.interval = 4
        self.on_days = FRIDAY

class WashBedSheets():

    def __init__(self):
        self.title = 'Wash Bedsheets'
        self.description = 'Program is Sintetico + Asciugatrice'
        self.frequency = WEEKLY
        self.interval = 4
        self.on_days = SATURDAY

class GlassAndPlastic():

    def __init__(self):
        self.title = 'Throw away Glass and Plastic'
        self.description = 'Do this unless you have already done it during shopping day'
        self.frequency = WEEKLY
        self.interval = 1
        self.on_days = FRIDAY


