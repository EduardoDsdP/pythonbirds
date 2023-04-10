from unittest import TestCase

from OO.carro import Motor

class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor=Motor()
        self.assertEqual(0, motor.velocidade)  # asserEqual serve para teste, para que adicionar primeiro um valor esperado que é o 0 e depois o valor que efetivamente voce ira receber. No caso pegamos o valor de velocidade e testamos se ele é igual a zero.

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)


