def get_ref_total(total):
    if total > 100:
        return print('total: ' + total + ' maior que 100')
    elif total < 100:
        return print('total: ' + total + ' é menor que 100')
    else:
        return print('total: ' + total + ' = 100')


get_ref_total(150)
get_ref_total(1)
get_ref_total(100)
get_ref_total(200)
get_ref_total(59)
get_ref_total(99)

