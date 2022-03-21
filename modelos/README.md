Estos son los modelos entrenados, cada uno se aplica a un cluster, pero los clusters podrían formarse en un orden diferente.  
Para reconocerlo podemos recurrir al número de elementos por cluster, estos tamaños son (en orden, modelo_1,2,3,4):  [77, 1125,  685,  860].  


Hay un cluster que corresponde a todo ceros, esto luego hay que post-procesarlo para que los valores menores a x (por ejemplo 0.01), ponerlo a 0, lo que pasa es que el modelo tiene ruido.


