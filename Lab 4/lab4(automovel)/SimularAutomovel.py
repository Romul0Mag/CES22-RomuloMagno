from Automovel import *

class SimularAutomovel():

    def acelerar(self,automovel):
        automovel.mostrarVelocidade()
        automovel.velocidade = min(automovel.velocidade + automovel.motor.forca_gerada/automovel.massa, automovel.velocidade_maxima)
        print('acelerei')
        automovel.mostrarVelocidade()

    def freiar(self, automovel):
        automovel.mostrarVelocidade()
        automovel.velocidade = max(automovel.velocidade - automovel.aceleracao_freio, 0)
        print('freei')
        automovel.mostrarVelocidade()

    def fazerCurva(self, automovel, graus):
        automovel.mostrarDirecao()
        automovel.direcao = (automovel.direcao + graus)%360
        print(f'fiz uma curva de {graus} graus')
        automovel.mostrarDirecao()

    def createAutomovelCombustao(self):
        pass

    def createAutomovelHibrido(self):
        pass

    def createAutomovelEletrico(self):
        pass


class SimularCarro(SimularAutomovel):

    def createAutomovelCombustao(self):
        carro = Carro()
        comb = MotorCombustao()
        carro.motor = comb
        return carro

    def createAutomovelHibrido(self):
        carro = Carro()
        hib = MotorHibrido()
        carro.motor = hib
        return carro

    def createAutomovelEletrico(self):
        carro = Carro()
        ele = MotorEletrico()
        carro.motor = ele
        return carro


class SimularCaminhao(SimularAutomovel):

    def createAutomovelCombustao(self):
        caminhao = Caminhao()
        comb = MotorCombustao()
        caminhao.motor = comb
        return caminhao

    def createAutomovelHibrido(self):
        caminhao = Caminhao()
        hib = MotorHibrido()
        caminhao.motor = hib
        return caminhao

    def createAutomovelEletrico(self):
        caminhao = Caminhao()
        ele = MotorEletrico()
        caminhao.motor = ele
        return caminhao


class SimularMoto(SimularAutomovel):

    def createAutomovelCombustao(self):
        moto = Moto()
        comb = MotorCombustao()
        moto.motor = comb
        return moto

    def createAutomovelHibrido(self):
        moto = Moto()
        hib = MotorHibrido()
        moto.motor = hib
        return moto

    def createAutomovelEletrico(self):
        moto = Moto()
        ele = MotorEletrico()
        moto.motor = ele
        return moto

