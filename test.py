import matplotlib.pyplot as plt
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sklearn.cluster import KMeans
from pandas import DataFrame
from collections import Counter

def skaitymas():
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
                                                'herithon_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('photo data herithon').sheet1
    X = [int(x.value) for x in (sheet.range('D4:D100') + sheet.range('K4:K100')
                                + sheet.range('R4:R100'))]
    Y = [int(x.value) for x in (sheet.range('E4:E100') + sheet.range('L4:L100')
                                + sheet.range('S4:S100'))]
    return X, Y


def plotas(xcord, ycord, count):
    color = np.random.choice(500, size=count)

    heatmap, xedges, yedges = np.histogram2d(xcord, ycord, bins=10)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

    plt.clf()
    plt.imshow(heatmap.T, extent=extent, origin='lower', interpolation="sinc",
                                                                cmap="Greys")

    plt.title('Photo distribution')
    plt.xticks([])
    plt.yticks([])


def kMeansClustering(clusterCount, X, Y):
    Data = {'x': X, 'y': Y}
    df = DataFrame(Data, columns=['x','y'])
    kMeans = KMeans(n_clusters=clusterCount).fit(df)
    centroids = kMeans.cluster_centers_
    x = centroids[:, 0]
    y = centroids[:,1]
    z = list(x**2 for x in Counter(kMeans.labels_).values())

    #plt.scatter(X, Y, c=kMeans.labels_.astype(float))
    plt.scatter(x, y, c='red', s=z, alpha=.5)

x, y = skaitymas()
plotas(x,y, 97*3)
#kMeansClustering(5, x,y)
plt.tight_layout()
plt.savefig("phDist_final.png", dpi=500, quality=100)
