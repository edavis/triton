#!/usr/bin/env python

import time
import arrow
import logging
import requests
import argparse
import threading

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',
)

class Source(object):
    def __init__(self, url):
        self.url = url
        self.updater = threading.Timer(2.0, self.update)
        self.updater.start()

class RSS(Source):
    def update(self):
        logging.debug('updating: %s', self.url)
        self.updater.run()

def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    r = RSS('http://til.ericdavis.org/feed.xml')

if __name__ == '__main__':
    main()
