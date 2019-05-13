import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',)


def worker(num):
    """ Thread worker function """
    logging.debug(f"worker {num}")
    time.sleep(5)
    logging.debug(threading.currentThread().name)
    return


def my_service(num):
    """ Thread service function """
    logging.debug(f"service {num}")
    time.sleep(1)
    logging.debug(threading.currentThread().name)
    return


threads = []

for i in range(5):
    w = threading.Thread(name="w thread-" + str(i), target=worker, args=(i,))
    threads.append(w)
    w.start()
    t = threading.Thread(name="t thread-" + str(i),
                         target=my_service, args=(i,))
    threads.append(t)
    t.start()
