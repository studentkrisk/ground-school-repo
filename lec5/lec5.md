# MavLink
- "drone language" for commands and telemetry
- not a physical protocol, just a data structure
- over radio for telemetry, to ground station

# DDS
- communication protocol used by flight controller
- very fast

# Wireless Communication with Drone
- ground station: communicates with onboard computer over UDP, same protocol for streaming services

## UDP
- User Datagram Protocol
- throw as much data as possible
- packets will not necessarily come in right order
- no reliability, packet data loss, but very fast and lightweight

## TCP
- Transmission Control Protocol
- uses acknowledgement between communication parties
- much slower, but more reliable


## RC Transmitters and Receivers
- RC Transmitter (TX)
	- handheld device
	- reads stick inputs, sends them over
	- 2.4 GHz radio
- RC Receiver (RX)


# Onboard Computer
- used like the somatic nervous system
- handles high-level tasks
- runs ROS nodes, SLAM, object detection, mission logic
- sends commands to FC and recieves telemetry for decision-making
- connects via serial, ethernet, or usb depending on setup

## Jetson Nano
- USB-C port for data transfer
- ethernet port
	- great for gimbal camera
- display port
	- good for seeing whats in the jetson
- 40 extra pins
- sd card and wifi, +more
- can run headless (via changing things on pins)
- 4/8GB ram
- AI accelerator
- runs linux!!!
	- can ssh into it
	- ROS runs on linux
- computer vision
	- runs ROS2 nodes for SLAM, path planning, control
	- real-time object detection, tracking
	- capable of running most computer vision things


# Communication Protocol Differences

## WiFi
- pros
	- high bandwidth
	- common in most computers
	- works well for short-range comms
- cons
	- limited range (a few hundred meters at most)
	- interference in commonly used bands
	- line of sight required

## Radio
- pros
	- long range
	- reliable, low-latency
	- works without cellular/WiFi
- cons
	- lower bandwidth (lower frequency!), so less data can be sent
	- requires dedicated hardware
	- regulation on allowed frequencies

## LTE
- cons
	- very wide coverage, reliable nowadays
	- high bandwidth, datarate (video!)
	- line of sight to GS not necessary
	- currently used on skydio drones (t-mobile)
- cons
	- latency higher than wifi radio (goes through cell towers)
	- requires SIM card/data plan
	- dead zones possible if far from cities


# SSH
- stands for secure shell
- TCP connection to a machine
- runs commands on other machines
- the output is sent back to you
- a way to run computers headless