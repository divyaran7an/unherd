from .. naive  import tscore
# from .. interface  import nodeEngine

import json
import sys
import requests
import unittest
import time

class BasicUnitTests(unittest.TestCase):

    def setUp(self):
        self.raw_sample = 'engine/resource/sample8.txt'
        self.api_batch_sample = 'engine/resource/earth.txt'
        self.api_sample = 'engine/resource/earth_batch.txt'
        self.startTime = time.time()
    
    def tearDown(self):
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)
    
    def testRaw(self):
        model = tscore.ScoreModel()
        f = open(self.raw_sample, 'r')

        for line in f.readlines():
            tweetJSON = json.loads(line)
            model.score(line), tweetJSON['text']

        f.close()


    # def testBatchCallToAPI(self):
    #     """
    #         Testing the node interface for batch tweet processing.
    #     """
    #     tweetJSONArr = []
        
    #     f = open(self.api_batch_sample, 'r')
        
    #     for line in f.readlines():
    #         tweetJSONArr.append(line)
    #     f.close()

    def testAPI(self):
        """
            Fire post request to the API.
        """
        

        url = "http://localhost:5000/unherd/api/v0.1/tweet"
        
        f = open(self.api_sample, 'r')
        dataArr = []
        for i in range(20):
            line = f.readline()
            line = line.replace("\n", "")
            # This works as well
            # But was just testing for the stringify issue in node
            # dataArr.append(line)		
            dataArr.append(json.dumps(json.loads(line)))		

        f.close();

        data = {'tweetJSON' : dataArr}

        headers = {'Content-type': 'application/json', 
                    'Accept': 'text/plain'}
        
        wts = {'featureWeights' : [10, 1, 1 ,1]}

        urlUpdate = "http://localhost:5000/unherd/api/v0.1/model/update"
        
        # r = requests.post(urlUpdate, data = json.dumps(wts), headers = headers)
        # print r.text

        r = requests.post(url, data = json.dumps(data), headers = headers)
        # print r.text


if __name__ == '__main__':
    unittest.main()
