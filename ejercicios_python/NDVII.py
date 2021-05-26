#Teledeteccion

def levantar_banda(carpeta, banda):
    '''Dada una carpeta y un número de banda, levanta la banda.'''
    
    import numpy as np
    import os
    
    directorio = os.path.join(carpeta)
    os.chdir(directorio)
    
    # Uso numpy para levantar cada una de las bandas 
    banda = np.load(banda)
    return banda

#%%

def crear_img_png(carpeta, banda):
    '''
    Dada una carpeta y un número de banda, muestra la
    imagen de dicha banda y la guarde en formato .png.
    '''
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    # Me va a servir para mas adelante, cuando necesite guardar la imagen
    nombre_imagen = 'IMG_' + banda[:-4] + '.png'
    
    banda = levantar_banda(carpeta, banda)
    
    # Puedo usar percentiles para fijar el rango
    q = 5 #Calculemos el qth percentil de la matriz banda
    vmin = np.percentile(banda.flatten(), q) 
    vmax = np.percentile(banda.flatten(), 100-q)
    
    # Visualizo la banda de la siguiente manera: 
    plt.imshow(banda, vmin = vmin, vmax = vmax)
    plt.colorbar()
    plt.savefig(nombre_imagen, transparent = True, bbox_inches = 'tight')


import os
os.path.join('c:\\', 'ejercicios_python', 'Nuevos', 'clip')
crear_img_png('c:\\ejercicios_python\\Nuevos\\clip', 'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band6_clip.npy')

#%%

def crear_hist_png(carpeta, banda, bins):
    '''
    Dada una carpeta, un número de banda y una
    cantidad de bins, muestre el histograma
    (con la cantidad de bins seleccionados) de los
    valores de dicha banda y la guarde en formato .png.
    '''
    import matplotlib.pyplot as plt    
    
    # Me va a servir para mas adelante, cuando necesite guardar la imagen
    nombre_hist = 'HIST_' + banda[:-4] + '.png'
    
    banda = levantar_banda(carpeta, banda)
    
    # En plt.imshow puedo  ajustar el rango de visualización de colores
    # usando los parámetros vmin y vmax. El siguiente histograma de los
    # valores en la matriz banda sirve para guiarme  en la búsqueda del
    # rango que tiene sentido usar como vmin y vmax.
    plt.hist(banda.flatten(),bins = bins)
    plt.savefig(nombre_hist, transparent = True, bbox_inches = 'tight')    

       
import os
os.path.join('c:\\', 'ejercicios_python', 'Nuevos', 'clip')
crear_hist_png('c:\\ejercicios_python\\Nuevos\\clip', 'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band4_clip.npy', 100)

#%%

def mascara_binaria(carpeta, banda):
    '''
    El histograma de la banda 4 parece ser bimodal. Es necesario 
    seleccionar un umbral que permita distinguir los dos tipos de
    píxels; y esto es lo que hace esta funcion.
    '''
    import matplotlib.pyplot as plt
    
    banda = levantar_banda(carpeta, banda)
    
    # Creo una matriz de booleanos con el condicional >= 1.20
    umbral_bool = (banda >= 1.20) 
    # Convierto la matriz de booleanos anterior en una matriz de 0s y 1s. 
    umbral_nums = 1 * umbral_bool
    # Grafico la imágen binaria obtenida de la matriz umbral_nums
    plt.imshow(umbral_nums)
    
    
import os
os.path.join('c:\\', 'ejercicios_python', 'Nuevos', 'clip')
mascara_binaria('c:\\ejercicios_python\\Nuevos\\clip', 'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band4_clip.npy')

#%%

def clasific_manual():
    '''nose todavia'''
    import numpy as np
    import matplotlib.pyplot as plt
    import os
    import matplotlib.colors
    import matplotlib.patches as mpatches
    
    # Levanto unicamente aquellas bandas pertenecientes
    # al Rojo y al infrarrojo cercano
    os.path.join('c:\\', 'ejercicios_python', 'Nuevos', 'clip')
    banda_roja = levantar_banda('c:\\ejercicios_python\\Nuevos\\clip',
                                'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band4_clip.npy')
    banda_IR_cerc = levantar_banda('c:\\ejercicios_python\\Nuevos\\clip',
                                'LC08_L1TP_225084_20180213_20180222_01_T1_sr_band5_clip.npy')
    # Calculo el NDVI en una nueva matriz
    NDVI = (banda_IR_cerc - banda_roja) / (banda_IR_cerc + banda_roja)
    
    # Categorizo los valores obtenidos en cada píxel de acuerdo
    # a clases que sean más útiles y fáciles de interpretar.
    clases_ndvi = NDVI.copy()
    for n_i, i in enumerate(clases_ndvi):
        for n_s,s in enumerate(i):
            if s < 0:
                clases_ndvi[n_i][n_s] = 0
            elif 0 <= s < 0.1:
                clases_ndvi[n_i][n_s] = 1
            elif 0.1 <= s < 0.25:
                clases_ndvi[n_i][n_s] = 2
            elif 0.25 <= s < 0.4:
                clases_ndvi[n_i][n_s] = 3
            elif s > 0.4:
                clases_ndvi[n_i][n_s] = 4
    
    # colorMap para asignarle a cada clase el color sugerido en la tabla.
    colors = ['black', 'y', 'yellowgreen', 'g', 'darkgreen']
    cmap = matplotlib.colors.ListedColormap(colors)    
    
    # Defino los limites de cada color
    limites = [0, 1, 2, 3, 4]
    norm = matplotlib.colors.BoundaryNorm(limites, cmap.N)
    
    # Gráfico con matplotlib mostrando las clases obtenidas.
    plt.imshow(clases_ndvi, cmap = cmap, norm = norm)
    
    texts = ['Sin vegetacion', 'Area desnuda', 'vegetacion baja', 'Vegetacion moderada']
    patches = [mpatches.Patch(color=colors[i], label=texts[i] ) for i in range(len(texts)) ]
    plt.legend(handles=patches, bbox_to_anchor=(1, 1), loc='upper left', ncol=1, fontsize = 'x-small' )
    
    
clasific_manual()    
    
    
    