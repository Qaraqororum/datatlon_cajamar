ts = []

for serie in ds['ID'].unique():
    if serie% 20 == 0 :print('reading serie:'+ str(serie))
    
    serie_samples = pd.Series(data=np.zeros(365),index=ds['SAMPLETIME'].unique())
    sample = ds.loc[ds['ID'] == serie, 'DELTA']
    sample.index = ds.loc[ds['ID'] == serie, 'SAMPLETIME']
    serie_samples.loc[ds.loc[(ds['ID'] == serie), 'SAMPLETIME']] = sample
    # serie_samples = ds.loc[(ds['ID'] == serie) &  (ds['SAMPLETIME'] == ds['SAMPLETIME'].unique()), 'DELTA']
    # print(len(serie_samples))
    # for moment in ds['SAMPLETIME'].unique():
    #     sample = serie_samples = ds.loc[(ds['ID'] == serie) &  (ds['SAMPLETIME'] == moment), 'DELTA']
    #     serie_samples.append(sample)
    ts.append(serie_samples)
ts = np.array(ts)


from tslearn.clustering import TimeSeriesKMeans
from tslearn.preprocessing import TimeSeriesScalerMeanVariance, TimeSeriesResampler
X_train = TimeSeriesScalerMeanVariance().fit_transform(ts[:300])
km = TimeSeriesKMeans(n_clusters=10, metric="dtw")
y_pred = km.fit_predict(X_train)



n = 10

for yi in range(n):
    plt.subplot(n/2, 2, yi+1)
    for xx in X_train[y_pred == yi]:
        plt.plot(xx.ravel(), "k-", alpha=.2)
    plt.plot(km.cluster_centers_[yi].ravel(), "r-")
    plt.xlim(0, 365)
    plt.text(0.55, 0.85,'Cluster %d' % (yi + 1),
             transform=plt.gca().transAxes)
    if yi == 1:
        plt.title("DBA $k$-means")
