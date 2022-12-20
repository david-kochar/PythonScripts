from datetime import datetime
from dateutil.relativedelta import relativedelta

fivetran_state = '202207'
dte = datetime.strptime(fivetran_state, '%Y%m').date()
# Calculate one months previous
fivetran_state = (dte + relativedelta(months=1)).strftime('%Y%m')

print(fivetran_state)


s = ''

if s is None or len(s) == 0:
    t = 'a'
else:
    t = 'b'
        
    
print(t)