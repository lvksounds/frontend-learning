def valorPagamento():
    contador_tarifas = 0
    valor_tarifa = float(input('Valor da tarifa (0 encerra o programa): '))
    while valor_tarifa != 0:
        contador_tarifas += 1
        dias_atraso = int(input('Dias de atraso: '))
        if dias_atraso > 0:
            multa = (3/100)*valor_tarifa
            juros = (0.1/100)*dias_atraso
            valor_final = valor_tarifa + multa + juros
            print(f'Valor final a ser pago: {valor_final}')
            print(f'Quantidade de tarifas pagas: {contador_tarifas}')
        valor_tarifa = float(input('Valor da tarifa (0 encerra o programa): '))
    return


valorPagamento()
