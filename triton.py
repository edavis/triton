#!/usr/bin/env python

import time
import logging
import argparse
import threading

from source import RSS
from source_list import SourceList

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)s) %(message)s',
)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()

    channel = object()

    sources = SourceList(args.input)
    for source in sources:
        RSS(source, channel)

    while threading.active_count() > 0:
        try:
            time.sleep(0.1)
        except KeyboardInterrupt:
            print '\nQuitting...'
            raise SystemExit
            
if __name__ == '__main__':
    main()
