# -*- coding: utf-8 -*-
from download import DataDownloader
#from keras_test02 import NeuralNetwork
from neural_network_2 import NeuralNetwork

from sendMail import send_email

downloader = DataDownloader(2017)
downloader.download_data()

nn = NeuralNetwork()
prediction = nn.run()

print(prediction)



send_email("safesfabio@gmail.com", "Hallo!", "Deine Nummer  diese Woche lauten: " +
           str(prediction))
