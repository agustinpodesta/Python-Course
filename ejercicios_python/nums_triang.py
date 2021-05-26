def sumar_traing(desde, hasta):
    '''Calcula recursivamente el n-ésimo número triangular'''
    res = (hasta*(hasta + 1))/2
    if hasta != desde:
        res = res  +  sumar_traing(desde, hasta -1)
    return res

sumar_traing(3, 6)


