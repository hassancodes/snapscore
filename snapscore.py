# from ppadb.client import Client as AdbClient

# import time
# import subprocess
# import os
# import sys


# class SnapScore:  # cam image and screen image should be string
#     def __init__(self, device):
#         self.device = device
#         # self.cam_img = cam_img
#         # self.screen_img = screen_img

#     def click_camera(self):
#         self.device.shell(
#             f'input touchscreen tap {cam_points[0]} {cam_points[1]}')
#         time.sleep(1)

#     def take_picture(self):
#         self.device.shell(
#             f'input touchscreen tap {cam_click_points[0]} {cam_click_points[1]}')
#         time.sleep(1)

#     def send_image(self):
#         self.device.shell(
#             f'input touchscreen tap {send_cord[0]} {send_cord[1]}')
#         time.sleep(1)
    
#     # function for sending multiple snaps.
#     def exp_snaps(self):
#         count =0
#         main_cam_cords=(542,2290)
#         cam_click_img_cord =(535,2050)
#         next_cord = (925,2280)
#         # friends_grp_cord=(879,1100)
#         friends_grp_cord=(910,1225)
        
#         # use this one where are some best friends
#         # friends_grp_cord=(910,1951)

#         send_grp_cord =(992,2270)
#         # get the camera location in the middle
#         # take the image 
#         # select the group of people you want to send the image to 
#         # send the snap and repeat the cycle
#         while(count!=400):
#             count+=1
#             time.sleep(1)
#             self.device.shell(f'input touchscreen tap {main_cam_cords[0]} {main_cam_cords[1]}')
#             time.sleep(1)
#             self.device.shell(f'input touchscreen tap {cam_click_img_cord[0]} {cam_click_img_cord[1]}')
#             time.sleep(1)
#             self.device.shell(f'input touchscreen tap {next_cord[0]} {next_cord[1]}')
#             time.sleep(1)
#             self.device.shell(f'input touchscreen tap {friends_grp_cord[0]} {friends_grp_cord[1]}')
#             time.sleep(1)
#             self.device.shell(f'input touchscreen tap {send_grp_cord[0]} {send_grp_cord[1]}')
#             print(f"cyle: {count}")
        
     
        
        


# cam_points = (72, 1582)
# cam_click_points = (535, 2055)
# send_cord = (995, 2280)


# client = AdbClient(host="127.0.0.1", port=5037)
# devices = client.devices()
# if len(devices) == 0:
#     print("No devices attached")
#     quit()
# device = devices[1]


# # initialization


# snp = SnapScore(device)
# if __name__ == "__main__":
#     cam_points = (72, 1582)
#     cam_click_points = (535, 2055)
#     send_cord = (995, 2280)
#     client = AdbClient(host="127.0.0.1", port=5037)
#     devices = client.devices()
    
#     if len(devices) == 0:
#         print("No devices attached")
#         quit()
#     device = devices[1]

#     if sys.argv[1] == 'exp':
#         # write exponential code over here
#         snp.exp_snaps()
#     elif sys.argv[1] =='reg':
#         print([x.serial for x in devices])

#         snapsent = 0
#         while(snapsent !=1000):
#             print("lol")
#             snapsent += 1
#             print(f"total Number of snap sent are", snapsent)
#             snp.click_camera()
#             snp.take_picture()
#             snp.send_image()


from ppadb.client import Client as AdbClient
import time
import sys

# Constants
CAM_POINTS = (72, 1582)
CAM_CLICK_POINTS = (535, 2055)
SEND_CORD = (995, 2280)

MAIN_CAM_CORDS = (542, 2290)
CAM_CLICK_IMG_CORD = (535, 2050)
NEXT_CORD = (925, 2280)
FRIENDS_GRP_CORD = (910, 1225)
SEND_GRP_CORD = (992, 2270)

class SnapScore:
    def __init__(self, device):
        self.device = device

    def click_camera(self):
        self.device.shell(f'input touchscreen tap {CAM_POINTS[0]} {CAM_POINTS[1]}')
        time.sleep(1)

    def take_picture(self):
        self.device.shell(f'input touchscreen tap {CAM_CLICK_POINTS[0]} {CAM_CLICK_POINTS[1]}')
        time.sleep(1)

    def send_image(self):
        self.device.shell(f'input touchscreen tap {SEND_CORD[0]} {SEND_CORD[1]}')
        time.sleep(1)

    def exp_snaps(self):
        count = 0
        while count != 400:
            count += 1
            time.sleep(1)
            self.device.shell(f'input touchscreen tap {MAIN_CAM_CORDS[0]} {MAIN_CAM_CORDS[1]}')
            time.sleep(1)
            self.device.shell(f'input touchscreen tap {CAM_CLICK_IMG_CORD[0]} {CAM_CLICK_IMG_CORD[1]}')
            time.sleep(1)
            self.device.shell(f'input touchscreen tap {NEXT_CORD[0]} {NEXT_CORD[1]}')
            time.sleep(1)
            self.device.shell(f'input touchscreen tap {FRIENDS_GRP_CORD[0]} {FRIENDS_GRP_CORD[1]}')
            time.sleep(1)
            self.device.shell(f'input touchscreen tap {SEND_GRP_CORD[0]} {SEND_GRP_CORD[1]}')
            print(f"Cycle: {count}")

def select_device():
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()

    if not devices:
        print("No devices attached.")
        sys.exit(1)

    print("Connected devices:")
    for idx, device in enumerate(devices):
        print(f"{idx}: {device.serial}")

    # Default to first device if only one
    selected_index = 0 if len(devices) == 1 else int(input("Select device index: "))
    return devices[selected_index]

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py [exp | reg]")
        sys.exit(1)

    device = select_device()
    snp = SnapScore(device)

    if sys.argv[1] == 'exp':
        snp.exp_snaps()
    elif sys.argv[1] == 'reg':
        snaps_sent = 0
        while snaps_sent != 1000:
            print(f"Sending snap #{snaps_sent + 1}")
            snp.click_camera()
            snp.take_picture()
            snp.send_image()
            snaps_sent += 1
        print(f"Total snaps sent: {snaps_sent}")
    else:
        print("Invalid argument. Use 'exp' or 'reg'.")

if __name__ == "__main__":
    main()
