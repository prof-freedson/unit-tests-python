# 1) Importar a classe
# "Calculadora"
from calculadora import Calculadora

# 2) Importar o pacote de
# testes unitários chamado "unittest"
import unittest

# 3) Criando a classe de
# testes unitários
class TestCalculadora(unittest.TestCase):
    
    # 4) Criando o objeto
    # que herdará a classe
    # "Calculadora"
    
    # OBS: é necessário usar
    # o método chamado "setUp()"
    def setUp(self):
        self.calc = Calculadora()
        
    # 5) Criar o método de teste
    # do método "soma()"
    def test_soma(self):
        self.assertEqual(self.calc.soma(2,3), 5, "Deve somar dois números")
        self.assertEqual(self.calc.soma(10,20), 30, "Deve resultar no valor 30")
        self.assertEqual(self.calc.soma(135,20123), 20258, "Deve resultar no valor 20258")
        
    # 5) Criar o método de teste
    # do método "subtracao()"
    def test_subtracao(self):
        self.assertEqual(self.calc.subtracao(10,2), 8, "Deve subtrair dois números")
        self.assertEqual(self.calc.subtracao(10,30), -20, "Deve resultar em um valor negativo")
    
    # 5) Criar o método de teste
    # do método "multiplicacao()"
    def test_multiplicacao(self):
        self.assertEqual(self.calc.multiplicacao(2,3), 6, "Deve multiplicar dois números")
    
    # 6) Criar o método de teste
    # do método "divisao()"
    def test_divisao(self):
        self.assertEqual(self.calc.divisao(10,2), 5, "Deve dividir dois números")
        
    # 7) Criar o método de teste
    # para uma divisão por zero
    def test_divisao_por_zero(self):
        self.assertEqual(self.calc.divisao(1,0), "Divisão inválida")
        
# Executar a classe de
# testes unitários
if __name__ == '__main__':
    unittest.main()


        
    