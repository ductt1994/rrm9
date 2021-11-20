#This file is used to set the capturing and displaying parameters of the IMX219 camera

#Supported capturing resolution and fps combinations for IMX219 and Webcam
res_fps_dict = {"8MP" : {"width" : 3264, "height" : 2464, "fps" : 21},
                "6MP" : {"width" : 3264, "height" : 1848, "fps" : 28},
                "2MP_a" : {"width" : 1920, "height" : 1080, "fps" : 30},
                "2MP_b" : {"width" : 1640, "height" : 1232, "fps" : 30},
                "1MP_a" : {"width" : 1280, "height" : 720, "fps" : 60},
                "1MP_b" : {"width" : 1280, "height" : 720, "fps" : 120},
                "WebcamH" : {"width" : 1280, "height" : 720, "fps" : 10},
                "WebcamL" : {"width" : 640, "height" : 480, "fps" : 30}}

#Select a capturing mode
mode = "8MP"
capture_width = res_fps_dict[mode]["width"]
capture_height = res_fps_dict[mode]["height"]
capture_fps = res_fps_dict[mode]["fps"]

#Displaying parameters
display_width = 1280
display_height = 720

if capture_width < display_width and capture_height < display_height:
    display_width = capture_width
    display_height = capture_height

display_fps = res_fps_dict[mode]["fps"]
