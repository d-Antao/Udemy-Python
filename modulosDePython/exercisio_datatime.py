# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime

from dateutil.relativedelta import relativedelta

total_value = 1_000_000
date_loan = datetime(2020,12,20)
delta_years = relativedelta(years=5)
final_date = date_loan + delta_years

date_instalments = []
date_instalment = date_loan
while date_instalment < final_date:
    date_instalments.append(date_instalment)
    date_instalment += relativedelta(months=+1)

value_instalments = total_value / len(date_instalments) 
  
for date in date_instalments:
    print(date.strftime('%d/%m/%Y'),f'E${value_instalments:,.2f}')
    
print('----------------------------------------------------')

print(
    f'The loan was {total_value} to pay'
    f' in {delta_years.year} years'
    f'({len(date_instalments)} months) in instalments of {value_instalments:,.2f} E$)'
)
    



