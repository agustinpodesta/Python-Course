class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0

class TorreDeControl:
    '''Representa el trabajo de una torre de control de un aeropuerto con
    una pista de aterrizaje. Los aviones que están esperando para aterrizar
    tienen prioridad sobre los que están esperando para despegar.
    '''
    def __init__(self):
        '''Crea la 'cola' de espera de aviones'''
        self.items_arribo = []
        self.items_partida = []
        
    def nuevo_arribo(self, avion):
        '''Encola el avion que esta esperando aterrizar'''
        self.items_arribo.append(avion)
        
    def nueva_partida(self, avion):
        '''Encola el avion que esta esperando despegar'''
        self.items_partida.append(avion)
    
    def ver_estado(self):
        '''
        Devuelve el estado de espera de aqellos aviones que
        quieren aterrizar y aquellos que quieren partir
        '''
        print('Vuelos esperando para aterrizar:', ', '.join(self.items_arribo))
        print(f'Vuelos esperando para despegar:', ', '.join(self.items_partida))
   
    def asignar_pista(self):
        '''
        Elimina el primer elemento de la cola de aviones esperando aterrizar.
        Cuando no haya mas aviones esperando arribar, elimina el primer
        elemento de la cola de aviones esperando despegar.
        '''
        if not len(self.items_arribo) == 0:
            print(f'El vuelo {self.items_arribo.pop(0)} aterrizó con exito')
            return
        elif len(self.items_partida) == 0:
            print('No hay vuelos en espera.')
            return
        else:
            print(f'El vuelo {self.items_partida.pop(0)} despegó con exito')
            return
    
    