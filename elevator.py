import random

class Elevator:
  def __init__(self, max_occupancy, num_floors):
    self.direction = 'up'
    self.door_status = 'closed'
    self.floor_level = 0
    self.queue = []
    self.max_occupancy = max_occupancy
    self.num_floors = num_floors

  # Open the doors to the elevator
  def open_doors(self):
    self.door_status = 'open'
    print("Door is " + self.door_status)

  # Close the doors to the elevator
  def close_doors(self):
    self.door_status = 'closed'
    print("Door is " + self.door_status)

  # Add an occupant to the elevator and add floor occupant requests to queue
  def add_occupant(self):
    if len(self.queue) < self.max_occupancy:
      requested_floor = 0
      if self.direction == 'up':
        requested_floor = random.randrange(self.floor_level + 1, self.num_floors)
      else:
        requested_floor = random.randrange(self.floor_level)
      self.queue.append(requested_floor)
      print("Passenger is added. Now at " + str(len(self.queue)) + " occupants.")
      print("Passenger pressed Floor " + str(requested_floor))
      return True
    else:
      print("Elevator full. Passenger cannot be added.")
      return False

  # Remove an occupant from the elevator and queue
  def remove_occupant(self, index):
      self.queue.pop(index)
      print("Passenger is removed. Now at " + str(len(self.queue)) + " occupants.")

  # Move the elevator up or down one floor
  def move(self):
    if self.direction == 'up':
      self.floor_level += 1
    else:
      self.floor_level -= 1
    print("Elevator moved to floor " + str(self.floor_level))