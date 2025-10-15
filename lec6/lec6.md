# sim2real transfer
- can you convert from sitl to reality?
- a lot harder than it sounds
- simulated sensors work differently from real sensors
- reality is imprecise
- zeroshot: can you transfer to reality and have it work first try
- processing power

# ROS
- robot operating system
- open source framework for building robots
- not technically an operating system
- features
	- modularity: node-based
	- communication: topics, services, actions to pass messages between nodes
	- ecosystem: lots of ROS packages for existing sensors
	- simulation support:  works out of the box with gazebo/isaac sim
- new for this year!

## Vocabulary
- node: a process that performs a specific function
- topic: a named place where nodes can publish to and subscribe to (like a bus)
- message: data structure sent between nodes (e.g. velocity commands)
- service: a request/response communication directly between nodes (i.e. a function call)
- action: service but supports long-running tasks
- package: collection of POS code, nodes, config files
- launch file: script that starts/initializes nodes

## Problems with ROS
- the version of ROS you're using is really important
- there are a lot of version conflicts
- PX4 recommends humble