from ppadb.client import Client as AdbClient

import time
import subprocess
import os
import sys


class SnapScore:  # cam image and screen image should be string
    def __init__(self, device):
        self.device = device
        # self.cam_img = cam_img
        # self.screen_img = screen_img
    
    
    def click_camera(self):
        self.device.shell(f'input touchscreen tap {cam_points[0]} {cam_points[1]}')
        time.sleep(1)
        
    def take_picture(self):
        self.device.shell(f'input touchscreen tap {cam_click_points[0]} {cam_click_points[1]}')
        time.sleep(1)
    
    def send_image(self):
        self.device.shell(f'input touchscreen tap {send_cord[0]} {send_cord[1]}')
        time.sleep(1)
    



    
cam_points = (72,1582)
cam_click_points =(535,2055)
send_cord = (995,2280)


client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()
if len(devices) == 0:
    print("No devices attached")
    quit()
device = devices[0]

# initialization


snp = SnapScore(device)
if __name__ =="__main__":
    snapsent = 0
    
    while(snapsent!=1000):
        snapsent+=1
        print(f"total Number of snap sent are",snapsent)
        snp.click_camera()
        snp.take_picture()
        snp.send_image()    
        
