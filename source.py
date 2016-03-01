import random
import logging
import hashlib
import requests
import threading

class Source(object):
    def __init__(self, url, channel):
        self.url = url
        self.channel = channel
        self.running = False

        threading.Thread(name=self.thread_name(), target=self.update).start()

    def update(self):
        logging.debug('checking %s', self.url)
        self.process()

        interval = None
        if not self.running:
            interval = random.randint(0, 60*60)
            logging.debug('[first check] checking again in %s seconds for %s', interval, self.url)
            self.running = True
        else:
            interval = 60*60
            logging.debug('[running] checking again in %s seconds for %s', interval, self.url)

        next_check = threading.Timer(interval, self.update)
        next_check.name = self.thread_name()
        next_check.daemon = True
        next_check.start()

    def thread_name(self, digits=7):
        return 'Thread-%s' % hashlib.sha256(self.url).hexdigest()[:digits]

class RSS(Source):
    def process(self):
        resp = requests.get(self.url)
        resp.raise_for_status()
        logging.debug('%s', resp)
        
