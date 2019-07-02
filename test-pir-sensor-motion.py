from gpiozero import MotionSensor

pir = MotionSensor(4)

print('test-pir-sensor-motion.py has started ...')

while True:
    pir.wait_for_motion()
    print('Motion detected!')