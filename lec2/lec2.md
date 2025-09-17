# Imagery Techniques
nadir = straight down
	opposite of zenith -> straight up
oblique = from an angle
RGB-D = RGB-depth
	uses ultrasonic for a depth value
	using two cameras allows for stereoscopic

# Types of cameras
gimbal cameras = can swivel
old one = optical zoom
new one = digital zoom
	worse for zooming
	however, new one is 5x lighter
	this year, we're trying to  optimize for weight so this is important

# OpenCV
all in python
free and open source
c++ apis for speed
general-purpose computer vision
features:
	3d reconstruction
	motion analysis
	optical flow
	feature detection
	deblurring
	video editing/reading/writing
abstraction!
	we don't have to write this stuff!!!
	we don't have to optimize this stuff!!

# SIFT
detects corners
can be used to detect similar features between two different images
no ai!!!

# Premade Alternatives to OpenCV
OpenDroneMap!
you need to give geotagged data!!
gives meshes and colours triangulation
has nice API and even web application
you can avoid coding (so sad!!)
gives interesting data (like the 3d model)

# This Year
either use OpenDroneMap or use OpenCV realtime

# Other Projects
SLAM
Optical Flow
Structure from Motion (getting terrain map)
Applying drone imagery (with Oksana)