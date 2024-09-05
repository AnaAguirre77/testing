import aritmetica

def test_sumar():
    assert aritmetica.sumar(2, 3) == 5.00
    assert aritmetica.sumar(0, 0) == 0.00
    assert aritmetica.sumar(-1, 1) == 0.00


def test_restar():
    assert aritmetica.restar(6, 3) == 3.00
    assert aritmetica.restar(0, 5) == -5.00
    assert aritmetica.restar(-1, -1) == 0.00

def test_dividir():
    assert aritmetica.dividir(8, 4) == 2.00
    assert aritmetica.dividir(0, 1) == 0.00
    assert aritmetica.dividir(9, 3) == 3.00

    assert aritmetica.dividir(1, 0) == "Error: División por cero no permitida."

def test_multiplicar():
    assert aritmetica.multiplicar(1, 3) == 3.00
    assert aritmetica.multiplicar(-1, 1) == -1.00
    assert aritmetica.multiplicar(0, 100) == 0.00

def test_sumar_n():
    assert aritmetica.sumar_n(2, 2, 2) == 6.00
    assert aritmetica.sumar_n(-1, 1, 1) == 1.00
    assert aritmetica.sumar_n(0, 0, 0) == 0.00

def test_promedio_n():
    assert aritmetica.promedio_n(2, 2, 2) == 2.00
    assert aritmetica.promedio_n(0, 0, 0) == 0.00
    assert aritmetica.promedio_n(-1, 1, 1) == 0.33

if __name__ == "__main__":
    test_sumar()
    test_restar()
    test_dividir()
    test_multiplicar()
    test_sumar_n()
    test_promedio_n()
    print("Todas las pruebas pasaron exitosamente.")