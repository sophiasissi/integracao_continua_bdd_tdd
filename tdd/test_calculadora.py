from calculadora import Calculadora

def test_media_num(): 
    calculadora = Calculadora()
    result = calculadora.media(2, 3)
    assert result == 2.5