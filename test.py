import matplotlib.pyplot as plt
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

def skaitymas():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('herithon_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('photo data herithon').sheet1
    X = [ int(x.value) for x in sheet.range('D4:D100')] + [int(x.value) for x in sheet.range('K4:K100')] + [ int(x.value) for x in sheet.range('R4:R100')]
    Y = [ int(x.value) for x in sheet.range('E4:E100')] + [ int(x.value) for x in sheet.range('L4:L100')] + [ int(x.value) for x in sheet.range('S4:S100')]
    #igX = [ x.value for x in sheet.range('D4:D100')]
    #igY = [ x.value for x in sheet.range('E4:E100')]
    #bX = [ x.value for x in sheet.range('K4:K100')]
    #fbY = [ x.value for x in sheet.range('L4:L100')]
    #twX = [ x.value for x in sheet.range('R4:R100')]
    #twY = [ x.value for x in sheet.range('S4:S100')]
    #X = igX + fbX + twX
    #Y = igY + fbY + twY
    return X, Y


def plotas(xcord, ycord, count):
    color = np.random.rand(count)
    pl = plt.scatter(xcord,ycord,s=20,c=color,alpha=0.7)
    plt.xticks(np.arange(0, 101, 20).sort())
    plt.yticks(np.arange(0, 101, 20).sort())
    plt.title('The graph for scatter map')
    return pl

x, y = skaitymas()
plot = plotas(x,y, 97*3)
plt.show()
