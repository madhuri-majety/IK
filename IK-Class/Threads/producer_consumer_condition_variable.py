import threading
import logging
import time

logging.basicConfig(level=logging.INFO,
                    format='(%(threadName)-9s %(message)s',)

def consumer(cv):
    logging.info("Consumer thread started ... ")
    with cv:
        logging.info("Consumer waiting ...")
        cv.wait()
        logging.info("Consumer consumed resource...")

def producer(cv):
    logging.info("Producer thread started ...")
    with cv:
        logging.info("Making resource available ...")
        logging.info("Notifying all consumers")
        cv.notifyAll()

if __name__ == '__main__':
    cv = threading.Condition()
    cs1 = threading.Thread(name='Consumer1', target=consumer, args=(cv,))
    cs2 = threading.Thread(name='Consumer2', target=consumer, args=(cv,))
    p = threading.Thread(name='Producer', target=producer, args=(cv,))

    cs1.start()
    time.sleep(2)
    cs2.start()
    time.sleep(2)
    p.start()

