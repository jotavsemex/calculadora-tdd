import pytest
from calculadora import calcula_media, situacao

def test_media_simples():
    assert calcula_media(8.0, 7.0, 9.0) == 8.25

def test_aluno_aprovado():
    assert situacao(7.0) == "aprovado"
    assert situacao(8.5) == "aprovado"
    assert situacao(10.0) == "aprovado"

def test_aluno_em_recuperacao():
    assert situacao(4.0) == "recuperacao"
    assert situacao(6.9) == "recuperacao"

def test_aluno_reprovado():
    assert situacao(3.9) == "reprovado"
    assert situacao(0.0) == "reprovado"

def test_nota_acima_de_10_e_invalida():
    with pytest.raises(ValueError):
        calcula_media(11.0, 7.0, 8.0)

def test_nota_negativa_e_invalida():
    with pytest.raises(ValueError):
        calcula_media(7.0, -1.0, 8.0)