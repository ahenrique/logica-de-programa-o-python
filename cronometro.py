from time import sleep

def cronometro():
   
   contador = 0

   while True:
      minutos, segundos = divmod(contador, 60)
      print(f'{minutos:02}:{segundos:02}', end='\r', flush=True)
      sleep(.99)
      contador+=1

cronometro()
