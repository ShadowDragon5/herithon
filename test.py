import matplotlib.pyplot as plt
import numpy as np
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

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
    pl = plt.scatter(xcord,ycord,s=color,alpha=0.7)
    plt.title('The graph for scatter map')
    return pl

x, y = skaitymas()
plot = plotas(x,y, 97*3)
plt.show()
