import hub
import time

wheel_left = hub.port.A.motor
wheel_right = hub.port.E.motor
wheels = wheel_left.pair(wheel_right)
arm_left = hub.port.B.motor
arm_right = hub.port.F.motor
sensor_color = hub.port.C.device
sensor_distance = hub.port.D.device

# wheels.run_for_degrees(180,-40,40)

# arm_left.run_for_degrees(360,50,50,0,100,100,False)
# arm_right.run_for_degrees(360,-50,50,0,100,100,False)
# while True:
#     time.sleep(0.2)
#     values_left = arm_left.get()
#     values_right = arm_right.get()
#     if values_left[0] == 0:
#         arm_left.float()
#     if values_right[0] == 0:
#         arm_right.float()
#     if values_left[0] == 0 and values_right[0] == 0:
#         break

# arm_left.run_for_degrees(-30)
# arm_right.run_for_degrees(50)
time.sleep(0.2)
arm_left.run_to_position(0)
arm_right.run_to_position(180)


# wheels.run_at_speed(-40,40)
# while True:
#     distance = sensor_distance.get()[0]
#     if distance and distance < 30:
#         wheels.float()
#         wheels.run_at_speed(40,40)
#         time.sleep(1)
#         wheels.float()
#         time.sleep(0.1)
#     else:
#         wheels.run_at_speed(-60,60)


