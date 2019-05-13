import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-15s) %(message)s',)


def daemon():
    """daemon process will automatically get cancelled when all other non-daemon process is completed"""
    logging.debug("start daemon")
    time.sleep(5)
    logging.debug("end daemon")


d = threading.Thread(target=daemon)
d.setDaemon(True)


def nondaemon():
    logging.debug("start non-daemon")
    logging.debug("end non-daemon")


nd = threading.Thread(target=nondaemon)

d.start()
nd.start()

d.join(2)  # explicit wait before cancelling
