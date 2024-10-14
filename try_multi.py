# IMPORTS
# =======
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait


# CONSTANTS for Robot Operation Parameters
# ========================================
STRAIGHT_SPEED = 900
STRAIGHT_ACC = 300
TURN_RATE = 80
TURN_ACC = 85


# VARIABLES Representing Robot Electronics
# ========================================

# Hub
hub = InventorHub()

# Driving Motors & Drivebase
left_motor = Motor(port=Port.D, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(port=Port.C)
drivebase = DriveBase(left_motor, right_motor, 51, 104)

# Attachment Motors
left_attachment_motor = Motor(port=Port.E)
right_attachment_motor = Motor(port=Port.F)
# Sensors
right_color_sensor = ColorSensor(Port.A)
left_color_sensor = ColorSensor(Port.B)


# FUNCTIONS Representing Robot Behaviors
# ======================================

def try_multi_steps():
    drivebase.settings(straight_speed=900,
                       straight_acceleration=300,
                       turn_rate=100,
                       turn_acceleration=85)

    # Forward
    drivebase.straight(distance=-65, then=Stop.HOLD, wait=True)
   
    drivebase.turn(angle=44, then=Stop.HOLD, wait=True)

   
    drivebase.settings(straight_speed=300,
                       straight_acceleration=300,
                       turn_rate=100,
                       turn_acceleration=85)

    
    drivebase.straight(distance=-430, then=Stop.HOLD, wait=True)
    
    drivebase.straight(distance=150, then=Stop.HOLD, wait=True)

    # Change drivebase speed
    drivebase.settings(straight_speed=900,
                       straight_acceleration=300,
                       turn_rate=100,
                       turn_acceleration=85)

    # Turn
    drivebase.turn(angle=-140, then=Stop.HOLD, wait=True)
    
    drivebase.straight(distance=230, then=Stop.HOLD, wait=True)
    
    drivebase.turn(angle=-45, then=Stop.HOLD, wait=True)
    
    drivebase.straight(distance=635, then=Stop.HOLD, wait=True)
    
    right_attachment_motor.run_angle(speed=500, rotation_angle=100,
                                     then=Stop.HOLD, wait=True)
    # Turn
    drivebase.turn(-30)
    # Back up
    drivebase.straight(distance=-135, then=Stop.HOLD, wait=True)
    
    drivebase.turn(angle=40, then=Stop.HOLD, wait=True)
    
    drivebase.straight(distance=175, then=Stop.HOLD, wait=True)
    
    drivebase.turn(angle=44, then=Stop.HOLD, wait=True)

    # Change drivebase speed
    drivebase.settings(straight_speed=900,
                       straight_acceleration=900,
                       turn_rate=100,
                       turn_acceleration=85)

    
    drivebase.straight(distance=95, then=Stop.HOLD, wait=True)


# Return to the other base
def go_to_other_base():
    # Go to the other base
    drivebase.drive(speed=400, turn_rate=20)
    wait(4000)
    drivebase.stop()


# MAIN PROGRAM
# ============
try_multi_steps()
go_to_other_base()
