flight controller = autonomous nervous system
jetson nano = conscious nervous system

# sensors

- IMU (interial measurement unit)
	- combines accelorometer and gyroscopes to measure orientation
	- angular velocity and linear acceleration
	- essential for flight stabilization and altitude control
	- often fused with magnetometers for heading estimation
		- detects earth's magnetic field to determine heading
		- helps correct yaw drift and supports navigation in GPS-denied enviornemnts
		- usually built into IMU
		- annoying to calibrate
		- good to prevent accumulating integration error
	- can use kalman filter to piece these together
- barometer (pressure sensor)
	- measures atmosphere pressure to estimate altitude
	- used for altitude hold and smooth vertical control
- GPS module
	- has RTK (real time kinematics)
		- can get within 0.5 meter precision, so can use it for real-time position tracking
		- position + velocity
	- provides global position, velocity, and time data
	- enables waypoint navigation, return-to-home, and geofencing (keeping the drone from flying too far)
- cameras
	- standard rgb
	- sends optical data to FC and jetson
	- wide fov
	- high resolution and frame rate
	- digital zoom because lighter
- rc tranmitters and recievers
	- transmitter:
		- handheld device used to send commands
		- reads stick inputs and passes them on
		- uses pwm
	- reciever:
		- mounted on drone, recieves signals from transmitter
		- passes commands to flight controllre via serial bus

# communication protocols
- serial (UART)
	- direct, basic communication between two divices
	- used for flight controller, onboard computer, gps module, telemetry radios
	- simple 2-wire setup: TX, RX
	- each uart connection has its own set of wires
	- common for mavlink messages and debugging
- CAN (controller area network)
	- uses a bus
	- robust, multidevice protocol used in cars and high-end drones
	- used for smart escs, gimbals, and advanced sensor networks
	- has error checking to prevent miscommunication
- I2C / SPI (electronic-heavy protocol)
	- I2C (inter-integrated circuit)
		- used for low-speed communication with electronics
		- shares two wirse, sda (data) and scl (clock)
		- multiple devices can talk on the same bus, but only one speaks at a time
	- SPI (serial peripheral interfaces)
		- same as serial/UART for multiple devices listening to a master device
- mavlink: technically software not hardware
	- "drone language" for commands and telemetry
	- not physical protocol, but message format that runs over UART, UDP, or CAN
	- used to send commands (e.g. arm, takeoff) and recieve data (e.g. GPS, battery)
	- powers communication between flight controller and onboard computer or gronud station
	- DDS
		- communication protoc used by ROS2 and modern drone systems
		- has real time publish-subscribe messaging between modules (notable for later!)
		- powers direct connection between FCs and onboard computers
		- great for real-time performance unlike mavlink
		- also over UART connection

# Flight Controller Firmware
- low level software that runs on the FC and is not developed by us
- main 3 examples: ardupilot, betaflight, pix4
- firmware can be configured with hundreds of tiny settings to optimize
- we don't have to deal with this!
- PID
	- proportional, integral, derivative
	- if derivative is too high, not quick enough
	- if integral is too high, fluctuates too much
	- critical damping = montonically decreasing
	- 