# -*- coding: utf-8 -*-
from download import DataDownloader
#from keras_test02 import NeuralNetwork
from keras_test import NeuralNetwork
from database import DbManager
from sendMail import send_email

downloader = DataDownloader(2017)
downloader.download_data()

nn = NeuralNetwork()
prediction = nn.run()

print(prediction)

db = DbManager()
db.store_data((int(prediction[0][0]),int(prediction[0][1]),
                   int(prediction[0][2]),int(prediction[0][3]),int(prediction[0][4])))


send_email("safesfabio@gmail.com", "Hallo!", "Deine Nummer  diese Woche lauten: " +
           str(prediction))
