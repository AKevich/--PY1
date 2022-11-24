from pprint import pprint
spisok = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(16)]
pprint(spisok)