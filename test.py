import matplotlib.pyplot as plt
import numpy as np
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
from sklearn.cluster import KMeans
from pandas import DataFrame
from collections import Counter

def skaitymas():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('herithon_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('photo data herithon').sheet1
    X = [int(x.value) for x in (sheet.range('D4:D100') + sheet.range('K4:K100') + sheet.range('R4:R100'))]
    Y = [int(x.value) for x in (sheet.range('E4:E100') + sheet.range('L4:L100') + sheet.range('S4:S100'))]
    return X, Y


def plotas(xcord, ycord, count):
    color = np.random.choice(500, size=count)
    pl = plt.scatter(xcord,ycord,c=color,alpha=0.7)
    #plt.title('The graph for scatter map')
    #plt.ylabel('Y coord')
    #plt.xlabel('X coord')
    return pl

def kMeansClustering(clusterCount, X, Y):
    Data = {'x': X, 'y': Y}
    df = DataFrame(Data, columns=['x','y'])
    kMeans = KMeans(n_clusters=clusterCount).fit(df)
    centroids = kMeans.cluster_centers_
    vals = Counter(kMeans.labels_).values()
    fuk = list(vals)
    for x in range(len(fuk)):
        plotting = plt.scatter(centroids[x, 0], centroids[x,1], c='red', s=int(fuk[x]*12))

    plt.title('The graph for scatter map')
    plt.ylabel('Y coord')
    plt.xlabel('X coord')
    return plotting

x, y = skaitymas()
#plot = plotas(x,y, 97*3)
plotas = kMeansClustering(10, x,y)
plt.show()
