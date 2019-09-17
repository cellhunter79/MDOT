# Python code for measure reacation time in human subject
# with computer monitor and keyboard

import matplotlib.pyplot as plt #pip install matplotlib; pip install pyQt5
import numpy as np 
import time # No need for installation
from matplotlib.widgets import Button
from PIL import Image #pip install Pillow
import glob

# import picture to randomize and set dimentions 
# set globle variables
time_display=0
time_interval = []
t_press = 0
delay = 1
reaction_time=0


###################################### Sara Editing
image_raw  = np.array(Image.open("road2.png"))  # choose pictures and directions.
x_res = image_raw.shape[0] 
y_res = image_raw.shape[1]
image_linearized = image_raw.reshape(x_res*y_res,3) #linearize image

stim_x_size=150 ## size of your final noise stimulation
stim_y_size=150

chance = 3 # chance of displaying the bar

signal_x_size = 50 #size of the bar
signal_y_size = 50
################################################3
x_res = image_raw.shape[0] 
y_res = image_raw.shape[1]



def main():
    #1. Randomize image and produce image and image_shuffle
    image_shuffle = randomize_image(image_linearized, stim_x_size, stim_y_size)

    #2. Plot the image and note the initiation time point
    line1, im = plotimage(image_shuffle)
    time_display = time.time()    
    fig.canvas.mpl_connect('button_press_event', on_press)

    #3. display new image
    make_new_image(image_shuffle,line1,im,time_interval)
    #3. Make image with randomize pixels from a picture.
    

    #x Final report
    final_report()

'''def randomize_image():
    x_ram_loc = np.random.randint(0,high=x_res-stim_x_size)
    y_ram_loc = np.random.randint(0,high=y_res-stim_y_size)
    image_temp = image_raw.reshape(x_res*y_res,3)
    np.random.shuffle(image_temp)
    image_shuffle = image_temp.reshape((x_res,y_res,3))
    image = image_shuffle[x_ram_loc:(x_ram_loc+stim_x_size),y_ram_loc:(y_ram_loc+stim_y_size),:]
    return image, image_shuffle '''

def randomize_image(image_linearized_local, x, y):
    np.random.shuffle(image_linearized_local)
    #pixel_index = np.random.randint(0,high=x_res*y_res,size=(stim_x_size,stim_y_size))
    image_shuffle_linear = image_linearized_local[0:(x*y),:]
    image_shuffle = image_shuffle_linear.reshape((x,y,3))
    return image_shuffle 
    
def plotimage(image_shuffle):
    global fig
    fig, ax1 = plt.subplots(figsize = (10,10))
    plt.ion()
    plt.show(block=False)
    im = plt.imshow(image_shuffle)
    fig_result = plt.figure()
    ax_result = plt.subplot(111)
    line1, = ax_result.plot(np.arange(len(time_interval)),time_interval)
    ax_result.set_ylim([0,delay])
    ax_result.set_xlim([0,40])
    return line1, im

def on_press(event):
    global t_press
    print('you pressed', event.button, event.xdata, event.ydata)
    t_press = time.time()
    if t_press - time_display < delay:
        time_interval.append(t_press-time_display)
        print(t_press)
        print(time_display)
        print(time_display-t_press)
        print(time_interval)

def make_new_image(image_shuffle, line1, im,time_interval):
    global time_display
    for filename in sorted(glob.glob('patterns/*.npy')): 
        print(filename)
        image = np.load(filename)
        im.set_data(image)
        if filename[-12:] == "1_signal.npy":
                time_display = time.time()
                print("works")
        plt.pause(0.1)

        print(time_interval)
        print(np.average(time_interval))
        
        print(reaction_time)
        line1.set_xdata(np.arange(len(time_interval)))
        line1.set_ydata(time_interval)

        print(np.average(time_interval))

def final_report():
    reaction_time = "Reaction Time: " + str(np.average(time_interval))
    plt.text(0,-1,reaction_time,color = "red", fontsize = 18)
    plt.pause(10)

#This is necessary. It finally calls main function to run.
main()
