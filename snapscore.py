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
        self.device.shell(
            f'input touchscreen tap {cam_points[0]} {cam_points[1]}')
        time.sleep(1)

    def take_picture(self):
        self.device.shell(
            f'input touchscreen tap {cam_click_points[0]} {cam_click_points[1]}')
        time.sleep(1)

    def send_image(self):
        self.device.shell(
            f'input touchscreen tap {send_cord[0]} {send_cord[1]}')
        time.sleep(1)
    
    # function for sending multiple snaps.
    def exp_snaps(self):
        count =0
        main_cam_cords=(542,2290)
        cam_click_img_cord =(535,2050)
        next_cord = (925,2280)
        friends_grp_cord=(879,1510)
        send_grp_cord =(992,2270)
        # get the camera location in the middle
        # take the image 
        # select the group of people you want to send the image to 
        # send the snap and repeat the cycle
        while(count!=400):
            count+=1
            time.sleep(1)
            self.device.shell(f'input touchscreen tap {main_cam_cords[0]} {main_cam_cords[1]}')
            time.sleep(1)
            self.device.shell(f'input touchscreen tap {cam_click_img_cord[0]} {cam_click_img_cord[1]}')
            time.sleep(1)
            self.device.shell(f'input touchscreen tap {next_cord[0]} {next_cord[1]}')
            time.sleep(1)
            self.device.shell(f'input touchscreen tap {friends_grp_cord[0]} {friends_grp_cord[1]}')
            time.sleep(1)
            self.device.shell(f'input touchscreen tap {send_grp_cord[0]} {send_grp_cord[1]}')
        
        
        
        


cam_points = (72, 1582)
cam_click_points = (535, 2055)
send_cord = (995, 2280)


client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()
if len(devices) == 0:
    print("No devices attached")
    quit()
device = devices[0]

# initialization


snp = SnapScore(device)
if __name__ == "__main__":
    cam_points = (72, 1582)
    cam_click_points = (535, 2055)
    send_cord = (995, 2280)
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()
    
    if len(devices) == 0:
        print("No devices attached")
        quit()
    device = devices[0]

    if sys.argv[1] == 'exp':
        # write exponential code over here
        snp.exp_snaps()
    else:

        snapsent = 0
        while(snapsent !=1000):
            print("lol")
            snapsent += 1
            print(f"total Number of snap sent are", snapsent)
            snp.click_camera()
            snp.take_picture()
            snp.send_image()
