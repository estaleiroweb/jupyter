import signal
import time

def signal_handler(sig, frame):
    print("\nInterrupt Ctrl+C pressed!")
    quit()
    import sys
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


while True:
    print('waiting...')
    time.sleep(10)