#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: processes.py
Author: Me
Email: yourname@email.com
Github: https://github.com/yourname
Description:        
    sdsdf
                sdfs
"""
from multiprocessing import Process, Event
import os
from time import sleep


def work():
    print __name__
    print os.getpid()
    sleep(9)
new_p = Process(target=work)
new_p.start()
print os.getpid()
bro
print 'after bro'
sleep(4)

