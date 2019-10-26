clave = ''
numeros = []

def mensaje_principal():
  print('-----------------------------------------------------------------------------------------------------------')
  print('| Encontrar el promedio de los numeros que ingresas, cuando quieras terminar solo escribe la palabra done |')
  print('|                              Nota: ingresa numeros entre 0 y 10                                         |')
  print('-----------------------------------------------------------------------------------------------------------')

def pedir_valor(clave):
#por que la variable "numeros" no me causa error
  while clave != "done":
    clave = input('ingresa un valor: ')
    try:
      if clave == 'done':
        clave = 'done'
      elif float(clave) >=0 and float(clave) <=10:
        numeros.append(float(clave))
        print(numeros)
      else:
        print('ingresa un numero entre 0 y 10 o la palabra done')
    except:
      print('ingresa un numero o la palabra done')

def promedio(numeros):
  try:
    promedio = (sum(numeros)/len(numeros))
    print('el promedio es',promedio)
  except:
    print('WARNING no existe un valor en el arreglo')

mensaje_principal()
pedir_valor(clave)
promedio(numeros)