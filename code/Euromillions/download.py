import urllib.request
import pandas as pd


class DataDownloader(object):
    
    def __init__(self, data):
        self.data = data
        
        
    def download_data(self):
        # Download the file from `url`, save it in a temporary directory and get the
        # path to it (e.g. '/tmp/tmpb48zma.txt') in the `file_name` variable:
        url = 'http://www.lottology.com/europe/euromillions/?do=past-draws-archive&tab=&as=TXT&year=' + str(self.data) + '&group_num_selector=selected&numbers_selector_mode=add&numbers_selected='    
        file_name, headers = urllib.request.urlretrieve(url, '../euromillions-past-draws-archive/euromillions-past-draws-archive' + str(self.data) + '.txt')
                
        print(file_name)        
        
        draws = pd.read_csv(file_name, skiprows=2, usecols=[1,2,3,4,5,6,7],  names=['1','2','3','4','5','6','7'], sep = '\t')
        return draws
    
downloader = DataDownloader(2017)
downloader.download_data()