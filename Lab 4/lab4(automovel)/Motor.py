

class Motor():
    def __init__(self):
        self.forca_gerada = None

    def poluir(self):
        pass


class MotorEletrico(Motor):
    def __init__(self):
        super().__init__()
        self.forca_gerada = 3000

    def poluir(self):
        print('eu poluo pouco')


class MotorHibrido(Motor):
    def __init__(self):
        super().__init__()
        self.forca_gerada = 4000

    def poluir(self):
        print('eu poluo medio')


class MotorCombustao(Motor):
    def __init__(self):
        super().__init__()
        self.forca_gerada = 5000

    def poluir(self):
        print('eu poluo muito')
