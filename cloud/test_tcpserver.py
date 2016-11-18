import threading
from poap.tcpserve import ThreadedTCPServer
from poap.strategy import FixedSampleStrategy


strategy = FixedSampleStrategy([1, 2, 3, 4, 5])
server = ThreadedTCPServer(sockname=('0.0.0.0', 0) , strategy=strategy)
name = server.sockname 
print(name)
cthread = threading.Thread(target=server.run)
cthread.start()
cthread.join()
result = server.controller.best_point()
print("Final: {0:.3e} @ {1}".format(result.value, result.params))