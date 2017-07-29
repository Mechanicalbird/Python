import threading


class BuckysMessenger(threading.Thread):
      def run(self):
          for _ in range(10):
              print(threading.currentThread().getName())
              print "/n"              

x = BuckysMessenger(name='send out messages')
y = BuckysMessenger(name='rescive messages')

x.start()
y.start()
