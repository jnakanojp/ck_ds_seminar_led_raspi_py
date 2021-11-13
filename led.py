import subprocess
import codecs
import RPi.GPIO as GPIO
import requests
import json
import time

BCM_PINS = [2,3,4,14,15,
17,18,27,22,23,
24,10,9,25,11,
8,7,0,1,5,
6,12,13,19,16,
26,20,21]

# LEDS_URL = 'https://azkokugakuin1.japaneast.cloudapp.azure.com/leds.php'
LEDS_URL = 'http://192.168.0.85:10080/leds.php'

hostname = codecs.decode(subprocess.run('hostname', capture_output=True).stdout)
print(hostname)
host_num = int(hostname.split('-')[-1][2:])
print('host_num: %d' %  host_num)
user_offset = (host_num - 1) * len(BCM_PINS)

def main():
    GPIO.setmode(GPIO.BCM)
    for pin in BCM_PINS:
        GPIO.setup(pin, GPIO.OUT)
    
    gpio_out = [0] * len(BCM_PINS)

    while True:
        try:
            json_obj = json.loads(requests.get(LEDS_URL).text)
            led_dict = {}
            for id_switch_dict in json_obj:
                led_dict[id_switch_dict['led_id']] = id_switch_dict['switch_on']
            print(led_dict)

            for uid, out in led_dict.items():
                uid_0origin = uid - 1
                if user_offset <= uid_0origin < user_offset + len(BCM_PINS):
                    gpio_out[uid_0origin - user_offset] = out
            
            print([*zip(BCM_PINS, gpio_out)])

            for pin, out in zip(BCM_PINS, gpio_out):
                GPIO.output(pin, True if out > 0 else False)

            time.sleep(0.01)
        except KeyboardInterrupt:
            exit()
        except:
            pass

if __name__ == '__main__':
    main()
