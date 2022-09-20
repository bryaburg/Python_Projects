import threading

class BuckyMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_Thread().getName())

x = BuckyMessenger(name = "Send out messags")
y = BuckyMessenger(name = "Receve messages")
x.start()
y.start()
