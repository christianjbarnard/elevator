from manager import Manager
from threading import Thread
import config

# Initialize manager and threads for traffic generation and elevator operations
manager = Manager(config.MAX_OCCUPANCY, config.NUM_FLOORS)
t1 = Thread(target=manager.generate_traffic)
t2 = Thread(target=manager.run_elevator)

# Start threads
t1.start()
t2.start()