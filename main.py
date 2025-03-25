import keyboard
import gpio as GPIO
import time

def stop():
    GPIO.output(FLW1, GPIO.LOW)
    GPIO.output(FLW2, GPIO.LOW)
    GPIO.output(FRW1, GPIO.LOW)
    GPIO.output(FRW2, GPIO.LOW)
    GPIO.output(BLW1, GPIO.LOW)
    GPIO.output(BLW2, GPIO.LOW)
    GPIO.output(BRW1, GPIO.LOW)
    GPIO.output(BRW2, GPIO.LOW)

    global isMoving

    isMoving = False

    time.sleep(1)


def turn_right():
    global isMoving

    if isMoving:
        stop()

    # left wheels move forward
    GPIO.output(BLW2, GPIO.HIGH)
    GPIO.output(FLW2, GPIO.HIGH)

    # right wheels move back
    GPIO.output(FRW1, GPIO.HIGH)
    GPIO.output(BRW1, GPIO.HIGH)

    isMoving = True


def turn_left():
    global isMoving

    if isMoving:
        stop()

    # left wheels move back
    GPIO.output(BLW1, GPIO.HIGH)
    GPIO.output(FLW1, GPIO.HIGH)

    # right wheels move forward
    GPIO.output(FRW2, GPIO.HIGH)
    GPIO.output(BRW2, GPIO.HIGH)

    isMoving = True


def move_forward():
    global isMoving

    if isMoving:
        stop()

    GPIO.output(FLW2, GPIO.HIGH)
    GPIO.output(FRW2, GPIO.HIGH)
    GPIO.output(BLW2, GPIO.HIGH)
    GPIO.output(BRW2, GPIO.HIGH)

    isMoving = True


def move_backward():
    global isMoving

    if isMoving:
        stop()

    GPIO.output(FLW1, GPIO.HIGH)
    GPIO.output(FRW1, GPIO.HIGH)
    GPIO.output(BLW1, GPIO.HIGH)
    GPIO.output(BRW1, GPIO.HIGH)

    isMoving = True

# TODO: change to real values
FLW1 = 0
FLW2 = 1

FRW1 = 2
FRW2 = 3

BLW1 = 4
BLW2 = 5

BRW1 = 6
BRW2 = 7

# 0 for none
# 1 for clockwise
# -1 for anticlockwise
turning: int = 0

shouldRotate: bool = False

isMoving: bool = False

def main():
    # TODO: setup gpio here
    ...

    while True:
        # 0 for none
        # 1 for forward
        # -1 for backward
        movement = 0

        # 0 for none
        # 1 for turning right
        # -1 for turning left
        turning = 0

        if keyboard.is_pressed('esc'):
            print('stopping...')
            break

        if keyboard.is_pressed('w'):
            movement += 1

        if keyboard.is_pressed('s'):
            movement -= 1

        if keyboard.is_pressed('d'):
            turning += 1

        if keyboard.is_pressed('a'):
            turning -= 1

        if turning != 0:
            match turning:
                case 1:
                    print("turning right")
                    turn_right()
                case -1:
                    print("turning left")
                    turn_left()

        else:
            match movement:
                case 1:
                    print("moving forward")
                    move_forward()
                case -1:
                    print("moving backward")
                    move_backward()
                case 0:
                    print("stopping")
                    stop()

    stop()

    # end of program
    print('bye')

if __name__ == '__main__':
    main()


