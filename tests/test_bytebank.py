from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_27_11_2001_deve_retornar_21(self):
        entrada = '27/11/2001' # Given-Contexto
        esperado = 21

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_sobrenome_recebe_Felipe_Rodrigues_deve_retornar_Rodrigues(self):
        entrada = ' Felipe Rodrigues ' # Given
        esperado = 'Rodrigues'

        felipe = Funcionario(entrada, '27/11/2001', 1111)
        resultado = felipe.sobrenome() # When

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 #given
        entrada_nome = 'Felipe Rodrigues'
        esperado = 90000

        funconario_teste = Funcionario(entrada_nome, '27/11/2001', entrada_salario)
        funconario_teste.decrescimo_salario() # when
        resultado = funconario_teste.salario

        assert resultado == esperado  # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # given
        esperado = 100

        funconario_teste = Funcionario('teste', '27/11/2001', entrada)
        resultado = funconario_teste.calcular_bonus() # when

        assert resultado == esperado  # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000000  # given

            funconario_teste = Funcionario('teste', '27/11/2001', entrada)
            resultado = funconario_teste.calcular_bonus()  # when

            assert resultado  # then
