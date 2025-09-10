1. What software is on our current drone? (Summary of the next 5 weeks)
	- objection detection (week 3)
		- historically done with openCV
		- last year we switched to YOLO
			- you only need one photo, which saves time
		- considering switching back to openCV
	- aerial imagery/stitching (week 2)
		- a lot of theory surrounding it
		- very long history of stitching, as used for spying 
		- tried openCV
		- had better results with OpenDroneMap
		- might switch back to openCV
			- last year, OpenDroneMap took a long time on the computer, also required another operator, vs. openCV can run on the drone
	- flight controller
		- cube orange running ardupilot
		- keeps drone stable and flying
		- very little autonomy
		- takes commands from navlink
	- 
2. What kinds of challenges/projects can YOU work on as a Software team member?
	- many differing this!
		- improve flight controller?
			- learn some reinforcement learning
		- computer vision
			- revamp stitching code
			- design better object detection system
		- focus on applications only
			- do 3d mapping for environmental research (w/ Oksana)
		- research into random things?
			- talk about it with team
3. What’s the “industry standard” for drone software in 2025?

| flight software       | ardupilot/betaflight | ros 2, highly modular, px4                                                         |
| --------------------- | -------------------- | ---------------------------------------------------------------------------------- |
| real time autonomy    | basic (e.g. YOLO)    | advanced SLAM (simeltaneous localization and mapping), path planning, AI interface |
| compliance and saftey | RFID + B4UFLY        | automated risk assessments, airspace alerts                                        |
| data integration      | local storage        | cloud storage                                                                      |
- also a push towards BVLOS and multiple drones
- BVLOS = beyond visual line of sight
- multiple drones driven by one operator
- talk more in week six
4. How does one learn about drones effectively in 2025?
	- AI can help for conceptual questions
	- can be used for code if used correctly
	- not good for stuff that has not been written about
	- EXPERIENCE!!!!
		- why we are here
		- repetition is the mother of learning
- good workflow
	- talk back and forth with AI
	- set goals for yourself
	- do projects
	- find ways of tracking progress to stay encouraged
	- for individual details, use AI + fact checking on websites + personal experience
	- reach out to friends/team
	- also learn from other subteams


# technology on drone
- WiFi antenna
- GPS receiver (x2 for redundancy) + other sensors
	- for SUAS, GPS coordinates are given and the drone has to fly between them
- Cube (flight controller)
- NVIDIA jetson orin nano (onboard computer)
- 360 auto-stabilize gimbal camera