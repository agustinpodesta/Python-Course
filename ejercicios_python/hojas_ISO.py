# Hojas ISO y recursión

def Hojas_ISO(N):
    '''
    Precondicion: N debe ser > 0
    Pos: devuelve el ancho y el largo de la hoja A(N) de manera mas prolija
    '''
    def hojas(N):
        '''
        Precondicion: N debe ser > 0
        Pos: devuelve el ancho y el largo de la hoja A(N) 
        '''
        if N == 0:
            ancho, alto = 1189, 841
        else:
            ancho, alto = hojas(N-1)
            if ancho > alto:
               ancho, alto = hojas(N-1)[0]//2, hojas(N-1)[1]
            else:
               ancho, alto = hojas(N-1)[0], hojas(N-1)[1]//2
        return ancho, alto
    
    ancho, alto = hojas(N)
    if ancho > alto:
        print(f'Las medidas de la hoja A{N} son: {alto} x {ancho} mm')
    else:
        print(f'Las medidas de la hoja A{N} son: {ancho} x {alto} mm')
    return


