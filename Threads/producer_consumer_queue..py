import threading
import queue
import random
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

BUF_SIZE = 10
q = queue.Queue(BUF_SIZE)

class ProdcuerThread(threading.Thread):
    def __init__(self, group = None, target = None,
                 name = None, args = (), kwargs = None,
                 verbose = None):
        super(ProdcuerThread, self).__init__()
        self.target = target
        self.name = name


    def run(self):
        while True:
            if not q.full():
                item = random.randint(1,10)
                q.put(item)
                logging.debug('Putting {} : {} items in queue'.format(item, q.qsize()))
                time.sleep(random.random())

        return


class ConsumerThread(threading.Thread):
    def __init__(self, group = None, target = None,
                 name = None, args = (), kwargs = None,
                 verbose = None):
        super(ConsumerThread, self).__init__()
        self.name = name
        self.target = target

    def run(self):
        while True:
            if not q.empty():
                item = q.get()
                logging.debug("Getting {} : {} items in queue".format(item, q.qsize()))
                time.sleep(random.random())

        return


if __name__ == '__main__':
    p = ProdcuerThread(name='Producer')
    c = ConsumerThread(name='Consumer')

    p.start()
    time.sleep(2)
    c.start()
    time.sleep(2)


