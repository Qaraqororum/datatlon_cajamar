# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 22:34:16 2022

@author: morte
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import silhouette_samples, silhouette_score
from pylab import *

def draw_silhouette(X_,cluster_labels):
    #Función que dibuja el silouette plot y devuelve los valores medios por cluster en orden.
    #Tambíen dibuja el valor medio con una línea discontínua.
    #
    #X_:- Matriz de datos que ha sido usada para clusterizar [muestras, características]
    #cluster_labels:-Etiquetas resultantes de la clusterización (vector)
    #
    #return, shiluete medio de cada cluster
    
    avg_sil_list = list()
    n_clusters = np.max(cluster_labels)
    X_ = X_.reshape([100,361])
    
    samples = silhouette_samples(X_,cluster_labels)
    y_lower = 10
    
    fig,ax=plt.subplots()
    silhouette_avg = silhouette_score(X_, cluster_labels)#silouette medio de todos los clústers
    
    #Dibujamos los diferenes clústers
    for i in range(n_clusters+1):
        it_sample = samples[cluster_labels == i]
        it_sample.sort()
        
        size_it_sample = it_sample.shape[0]
        y_upper = y_lower + size_it_sample
        
        color = cm.nipy_spectral(float(i) / n_clusters)
        ax.fill_betweenx(
            np.arange(y_lower, y_upper),
            0,
            it_sample,
            facecolor=color,
            edgecolor=color,
            alpha=0.7,)
    
        ax.text(-0.05, y_lower + 0.5 * size_it_sample, str(i))
        
        y_lower = y_upper+10
        print("cluster "+str(i)+" = "+str(np.mean(it_sample)))
        
        avg_sil_list.append(np.mean(it_sample))
    
    #Establecemos los retoques para que el gráfico sea legible
    ax.set_title("The silhouette plot for the various clusters.")
    ax.set_xlabel("The silhouette coefficient values")
    ax.set_ylabel("Cluster label")
    ax.axvline(x=silhouette_avg, color="red", linestyle="--")   
    ax.set_yticks([])  # Clear the yaxis labels / ticks
    ax.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])   
    
    return(avg_sil_list)