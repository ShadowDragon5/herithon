import matplotlib.pyplot as plt
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def skaitymas():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('herithon_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('photo data herithon').sheet1
    data = sheet.get_all_records()
    print(data)


def plotas(xcord, ycord, count):
    colors = np.random.rand()
    pl = plt.scatter(x,y,s=count,c=colors,alpha=0.7)
    return pl

skaitymas()
