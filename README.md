# elevator
A simulation of an elevator

Challenge:
1. Provide code that simulates an elevator.
2. Please upload your code to github for a discussion.
3. Additionally, document all assumptions and features that weren't implemented
4. Please be prepared to discuss the assumptions and features that were not implemented during your interview

This program consists of 4 files:
- config.py: Contains constants for number of floors and max occupant number
- main.py: Initializes the elevator manager and starts up the threads to run
- manager.py: The elevator manager class. Holds properties for managing the elevator and the methods for populating requests and running elevator
- elevator.py: The elevator class. Contains methods and properties for basic elevator functionality.

Overview
The program consists to two threads running in parallel:
- Thread to generate requests for the elevator to process
- Thread to operate the elevator
The elevator operates with the following priorities:
1. Process the requests coming from inside the elevator
2. Pick up outside requests if they are going in same direction as current request and on same floor as elevator
3. If elevator is empty, go to oldest request next (FIFO)
4. If elevator is empty and no requests. Remain idle on current floor.

Assumptions:
- There is only one elevator in the building
- The building starts at Floor level 0 and has no basement

Improvements:
- Use event loops to allow the elevator to responsively react to new elevator requests
- Improve scalability of the program (adjustable frequencies for traffic, no hardcoded values, adjustable sleep times between actions)
- Create GUI to display the elevator moving across the floors
- Implement multiple elevators in the building all working at same time
- Implement a weight sensor system for the elevator
- Research and implement more optimized algorithms for the movement of the elevator
- Implement unit testing to validate the elevator's functionality
- Use real data to simulate the incoming requests (presumably more traffic on first floor, etc.)
- Implement a metric tool to analyze and visualize the performance of the elevator
- Add several states for the elevator (idle, out of order, etc.)
- Add 'emergency stop' button in case of emergency
- Add elevator music :)

How to run:
- Adjust values in config.py
- Run `python3 main.py` in ./elevator