entrada = float(input())
cem_int = entrada // 100
cem_rest = entrada % 100
cinq_int = cem_rest // 50
cinq_rest = cem_rest % 50
vinte_int = cinq_rest // 20
vinte_rest = cinq_rest % 20
dez_int = vinte_rest // 10
dez_rest = vinte_rest % 10
cinco_int = dez_rest // 5
cinco_rest = dez_rest % 5
dois_int = cinco_rest // 2
dois_rest = cinco_rest % 2
um_real_int = dois_rest // 1
um_real_rest = dois_rest % 1
cinq_cent_int = um_real_rest // 0.50
cinq_cent_rest = um_real_rest % 0.50
vinte_e_cinco_int = cinq_cent_rest // 0.25
vinte_e_cinco_rest = cinq_cent_rest % 0.25
dez_cent_int = vinte_e_cinco_rest // 0.10
dez_cent_rest = vinte_e_cinco_rest % 0.10
cinco_cent_int = dez_cent_rest // 0.05
cinco_cent_rest = dez_cent_rest % 0.05
um_cent_int = cinco_cent_rest // 0.01
um_cent_rest = cinco_cent_rest % 0.01
print('NOTAS:')
print('{:.0f} nota(s) de R$ 100.00'.format(cem_int))
print('{:.0f} nota(s) de R$ 50.00'.format(cinq_int))
print('{:.0f} nota(s) de R$ 20.00'.format(vinte_int))
print('{:.0f} nota(s) de R$ 10.00'.format(dez_int))
print('{:.0f} nota(s) de R$ 5.00'.format(cinco_int))
print('{:.0f} nota(s) de R$ 2.00'.format(dois_int))
print('MOEDAS:')
print('{:.0f} moeda(s) de R$ 1.00'.format(um_real_int))
print('{:.0f} moeda(s) de R$ 0.50'.format(cinq_cent_int))
print('{:.0f} moeda(s) de R$ 0.25'.format(vinte_e_cinco_int))
print('{:.0f} moeda(s) de R$ 0.10'.format(dez_cent_int))
print('{:.0f} moeda(s) de R$ 0.05'.format(cinco_cent_int))
print('{:.0f} moeda(s) de R$ 0.01'.format(um_cent_int))