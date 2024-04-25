from tdd.src.calculadora import Calculadora

def test_media_num(): 
    result = Calculadora.media(2, 3)
    assert result == 2.5