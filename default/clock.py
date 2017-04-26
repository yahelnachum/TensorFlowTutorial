'''
Created on Apr 25, 2017

@author: yahel
'''

import time


class Clock(object):
    '''
    classdocs
    '''

    timeBefore = 0.0;

    def __init__(self):
        '''
        Constructor
        '''
        self.timeBefore = time.time()*1000;
    
    def split(self):
        return time.time()*1000 - self.timeBefore
    
    def delta(self):
        timeAfter = time.time()*1000
        delta = timeAfter - self.timeBefore
        self.timeBefore = timeAfter
        return delta