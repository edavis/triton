import random
import logging
import threading

class Source(object):
    def __init__(self, url, channel):
        self.url = url
        self.channel = channel

        interval = random.randint(0, 60)
        logging.debug('starting check schedule in %s seconds for %s', interval, self.url)
        updater = threading.Timer(interval, self.update)
        updater.daemon = True
        updater.start()

    def update(self):
        self.process()

        interval = 2*60
        logging.debug('checking again in %s seconds for %s', interval, self.url)
        updater = threading.Timer(interval, self.update)
        updater.daemon = True
        updater.start()

class RSS(Source):
    def process(self):
        pass
