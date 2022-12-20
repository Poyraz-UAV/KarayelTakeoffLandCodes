#KALKIŞ KOD ÖRNEĞİ1
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

# Connect to the vehicle
vehicle = connect('/dev/serial0', baud=57600, wait_ready=True)

# Set the vehicle into guided mode
vehicle.mode = VehicleMode("GUIDED")

# Wait for the mode to be set
while not vehicle.mode.name == 'GUIDED':
    print("Waiting for guided mode...")
    time.sleep(1)

# Take off to an altitude of 10 meters
vehicle.simple_takeoff(10)

# Wait until the vehicle reaches the desired altitude
while True:
    print("Altitude: ", vehicle.location.global_relative_frame.alt)
    if vehicle.location.global_relative_frame.alt >= 10*0.95:
        print("Reached target altitude")
        break
    time.sleep(1)

# Disconnect from the vehicle
vehicle.close()



#İNİŞ KOD ÖRNEĞİ1

from dronekit import connect, VehicleMode

# Dronenun bağlantı noktasını belirtin (örneğin, /dev/ttyACM0)
vehicle = connect('/dev/ttyACM0', wait_ready=True)

# Dronenun uçuş modunu belirtin
vehicle.mode = VehicleMode("GUIDED")

# Dronenun "land" (iniş) işlemini yapması için "land" komutunu gönderin
vehicle.commands.land()

# Dronenun uçuş kontrol modülünü kapatın ve bağlantıyı kesin
vehicle.close()



#İNİŞ KOD ÖRNEĞİ2
from dronekit import connect, VehicleMode

# Connect to the drone
vehicle = connect("127.0.0.1:14550", wait_ready=True)

# Set the drone's mode to "LAND"
vehicle.mode = VehicleMode("LAND")

# Wait for the drone to land
while vehicle.location.global_relative_frame.alt > 0.1:
    time.sleep(1)

# Disarm the motors
vehicle.armed = False

# Close the connection to the drone
vehicle.close()

