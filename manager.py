import time
import random
from elevator import Elevator

class Manager:
  # Constructor initializes the queue for outside elevator requests, the elevator, and the number of floors of the building
  def __init__(self, max_occupancy, num_floors):
    self.outside_queue = []
    self.elevator = Elevator(max_occupancy, num_floors)
    self.num_floors = num_floors

  # Generates a random elevator request to add to the queue
  def generate_request(self):
    #Generates a random floor the request is coming from
    floor = random.randrange(0, self.num_floors)

    # Generates a random direction the requester wants to go
    direction = ''
    if floor == 0:
      direction = 'up'
    elif floor == self.num_floors - 1:
      direction = 'down'
    else:
      direction = random.choice(['up', 'down'])

    # Returns the request object
    return {
      'direction': direction,
      'floor': floor
    }

  # Continually generates requests for the elevator. One of the two major threads.
  def generate_traffic(self):
    while True:
      # Create a request
      request = self.generate_request()

      # Print request to console
      print('Passenger pressed ' + request['direction'] + ' button on floor ' + str(request['floor']))

      # Add to outside queue and wait
      self.outside_queue.append(request)
      time.sleep(random.randrange(2, 5))
      
  # Main loop for elevator to run. Processes requests inside elevator then outside the elevator. One of the two major threads.
  def run_elevator(self):
    while True:
      # If no one in elevator, go to the floor that requested first
      if len(self.elevator.queue) == 0:

        # Elevator is idle
        if len(self.outside_queue) == 0:
          print("No occupants or requests. Now idle...")
          time.sleep(5)
          continue

        # Figure out whether to go up or down to pick up new passenger
        if self.outside_queue[0]['floor'] > self.elevator.floor_level:
          self.elevator.direction = 'up'
        elif self.outside_queue[0]['floor'] < self.elevator.floor_level:
          self.elevator.direction = 'down'

        # Move to the floor with the new passenger
        for i in range(abs(self.elevator.floor_level - self.outside_queue[0]['floor'])):
          self.elevator.move()
          time.sleep(1)

        # Set elevator to go in direction occupant needs
        self.elevator.direction = self.outside_queue[0]['direction']

      # Remove occupants on current floor if necessary
      i = 0
      elevator_queue_size = len(self.elevator.queue)
      while i < elevator_queue_size:
        if self.elevator.queue[i] == self.elevator.floor_level:
          self.elevator.open_doors()
          self.elevator.remove_occupant(i)
          i -= 1
          elevator_queue_size -= 1
        i += 1
      
      # Load occupants on current floor if necessary
      i = 0
      queue_size = len(self.outside_queue)
      while i < queue_size:
        if self.outside_queue[i]['floor'] == self.elevator.floor_level and self.outside_queue[i]['direction'] == self.elevator.direction:
          if self.elevator.door_status == 'closed':
            self.elevator.open_doors()
          if self.elevator.add_occupant():
            self.outside_queue.pop(i)
            i -= 1
            queue_size -= 1
        i += 1

      # Close doors if necessary
      if self.elevator.door_status == 'open':
        self.elevator.close_doors()

      # Move elevator to adjacent floor
      time.sleep(1)
      if len(self.elevator.queue) > 0:
        self.elevator.move()
      time.sleep(1)