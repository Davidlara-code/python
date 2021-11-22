import pandas as pd



csv = pd.read_csv('cotizacion.csv', delimiter=';', thousands='.', decimal=',',index_col=0)

print(csv)


print("Estos son los valores minimos de cada columna:")
minFinal = min(csv['Final'])
minMaximo = min(csv['Máximo'])
minMinimo = min(csv['Mínimo'])
minVolumen = min(csv['Volumen'])
minEfectivo = min(csv['Efectivo'])
print("minFinal: ",minFinal)
print("minMaximo: ",minMaximo)
print("minVolumen: ",minVolumen)
print("minEfectivo: ",minEfectivo)
print( )
print("Estos son los valores máximos de cada columna:")
maxFinal = max(csv['Final'])
maxMaximo = max(csv['Máximo'])
maxMinimo = max(csv['Mínimo'])
maxVolumen = max(csv['Volumen'])
maxEfectivo = max(csv['Efectivo'])
print("maxFinal:",maxFinal)
print("maxMaximo:",maxMaximo)
print("maxVolumen:",maxVolumen)
print("maxEfectivo:",maxEfectivo)
print( )
print("Estos son los valores medios de cada columna:")
mediaFinal = csv['Final'].mean()
mediaMaximo = csv['Máximo'].mean()
mediaMinimo = csv['Mínimo'].mean()
mediaVolumen = csv['Volumen'].mean()
mediaEfectivo = csv['Efectivo'].mean()
print("mediaFinal:",round(mediaFinal,2))
print("mediaMaximo:",round(mediaMaximo,2))
print("mediaVolumen:",round(mediaVolumen,2))
print("mediaEfectivo:",round(mediaEfectivo,2))

