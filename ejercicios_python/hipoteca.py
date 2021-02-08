# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
pago_extra=1000
total_pagado = 0.0
mes=0
n=0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    mes=mes+1
    while mes>=60 and mes<=107:
        total_pagado = total_pagado + pago_mensual+pago_extra
        mes=mes+1
        saldo = saldo * (1+tasa/12) - pago_mensual-pago_extra
    total_pagado = total_pagado + pago_mensual
    print(mes,total_pagado,saldo)
    
a=f'El total pagado fueron ${round(total_pagado)} habiendo transcurrido {mes} meses'
print(a)
