import requests
import urllib
import json
import time

# BASE_URL = "http://azkokugakuin1.japaneast.cloudapp.azure.com/"
BASE_URL = 'http://192.168.0.85:10080/'

def led_on(led_id):
  res = requests.get(BASE_URL + "led.php?led_id=%d&switch_on=1" % led_id)
  print("HTTP Response Code:", res.status_code, "\nJSON:", res.text)

def led_off(led_id):
  res = requests.get(BASE_URL + "led.php?led_id=%d&switch_on=0" % led_id)
  print("HTTP Response Code:", res.status_code, "\nJSON:", res.text)

while True:
    for i in range(70):
        try:
            led_id = i + 1
            led_on(led_id)
            time.sleep(0.25)
            led_off(led_id)
        except KeyboardInterrupt:
            exit()
        except:
            pass
    