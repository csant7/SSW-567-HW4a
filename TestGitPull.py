'''
Created on Sep 18, 2019

@author: Connor Santiago
'''

import unittest
from GitPull import gitHubAPI


class Object(object):
    def __init__(self, content):
        self.content = content

class testGitPull(unittest.TestCase):
    @patch('requests.get')
    
    def testInput(self, json):
        jsonObj = json.loads(json)
        m.json.return_value = jsonObj
        gitResults = []

        
        gitResults.append(json.loads('[{"name" : "SSW-567-HelloWorld"}. {"name": "SSW-567-HW2a"}, {"name": "SSW-567-HW4a"}, {"name": "Triangle-Classification"}]'))
        gitResults.append(json.loads('[ { "commit" : "1" }, { "commit" : "9" }, { "commit" : "2" }, { "commit" : "1" } ]'))

if __name__ == '__main__':
    unittest.main(exit = False)