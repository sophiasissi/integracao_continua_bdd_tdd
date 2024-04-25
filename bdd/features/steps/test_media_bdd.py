from behave import given, when, then

@given('eu tenho dois números: {num1:d} e {num2:d}')
def step_impl(context, num1, num2):
    context.num1 = num1
    context.num2 = num2

@when('eu divido por dois as soma dos números')
def step_impl(context):
    context.resultado = (context.num1 + context.num2) / 2

@then('o resultado deve ser 2.5')
def step_impl(context):
    assert context.resultado == 2.5, f"Resultado incorreto. Esperado: 2.5. Obtido: {context.resultado}"
