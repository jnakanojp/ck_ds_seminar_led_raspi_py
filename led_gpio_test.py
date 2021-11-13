import time
import RPi.GPIO as GPIO

BCM_PINS = [2,3,4,14,15,
17,18,27,22,23,
24,10,9,25,11,
8,7,0,1,5,
6,12,13,19,16,
26,20,21]


def main():
    GPIO.setmode(GPIO.BCM)
    for pin in BCM_PINS:
        GPIO.setup(pin, GPIO.OUT)
    
    gpio_out = [0] * len(BCM_PINS)

    led_id = 0
    while True:
        try:
            time.sleep(0.03)
            led_id2 = led_id % (len(BCM_PINS) * 2)
            if led_id2 > len(BCM_PINS):
              led_id2 = len(BCM_PINS) * 2 - (led_id2 + 1)

            print(led_id2)

            gpio_out[led_id2] = 1
            for pin, out in zip(BCM_PINS, gpio_out):
                GPIO.output(pin, True if out > 0 else False)
            gpio_out[led_id2] = 0
            if led_id % 1000 == 0:
              print(led_id)
        except KeyboardInterrupt:
            exit()
        except:
            pass
        led_id += 1

if __name__ == '__main__':
    main()
