# Python code for measure reacation time in human subject
# with computer monitor and keyboard

import matplotlib.pyplot as plt #pip install matplotlib; pip install pyQt5
import numpy as np 
import time # No need for installation
from matplotlib.widgets import Button
from PIL import Image #pip install Pillow

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

chance = 5 # chance of displaying the bar

signal_x_size = 20 #size of the bar
signal_y_size = 10

red_comp    = 0  # RGC color from 0 to 1
blue_comp   = 1
green_comp  = 0

total_frame_num = 3000
signal_frame_num = 10
blank_frame_num = signal_frame_num 
total_batch_num = int (total_frame_num / signal_frame_num) #i
################################################3
x_res = image_raw.shape[0] 
y_res = image_raw.shape[1]

def main():
    #1. Randomize image and produce image and image_shuffle
    image_shuffle = randomize_image(image_linearized, stim_x_size, stim_y_size)

    #2. Plot the image and note the initiation time point
    im = plotimage(image_shuffle)
    #time_display = time.time()    

    #3. display new image
    make_new_image(image_shuffle,im,time_interval)
    #3. Make image with randomize pixels from a picture.


def randomize_image(image_linearized_local, x, y):
    np.random.shuffle(image_linearized_local)
    #pixel_index = np.random.randint(0,high=x_res*y_res,size=(stim_x_size,stim_y_size))
    image_shuffle_linear = image_linearized_local[0:(x*y),:]
    image_shuffle = image_shuffle_linear.reshape((x,y,3))
    return image_shuffle 
    
def plotimage(image_shuffle):
    global fig
    fig = plt.plot(figsize = (10,10))
    plt.ion()
    plt.show(block=False)
    im = plt.imshow(image_shuffle)
    #fig_result = plt.figure()
    #ax_result = plt.subplot(111)
    return im

def make_new_image(image_shuffle, im,time_interval):
    global time_display
    rand_choice = round(np.random.random()*100)%chance
    for i in range(1,total_batch_num,1):
        m =0
        if rand_choice == 0:
            ## display a signal at random position
            start_p = np.random.choice(stim_x_size-signal_x_size)
            end_p = np.random.choice(stim_y_size-signal_y_size)
            Signal_start_point = (start_p,(stim_x_size-start_p))
            Signal_end_point = (end_p,(stim_y_size-end_p))

            row_pad = (start_p,(stim_x_size-start_p-signal_x_size))
            column_pad =(end_p,(stim_y_size-end_p-signal_y_size))

            time_display = time.time()
            for m in range(1,signal_frame_num,1):
                randomize_image(image_linearized, stim_x_size, stim_y_size)
                #Red = np.random.uniform(0,1,signal_x_size*signal_y_size)
                Red = np.full((signal_x_size*signal_y_size), red_comp)
                Green = np.full((signal_x_size*signal_y_size),green_comp)
                Blue = np.full((signal_x_size*signal_y_size), blue_comp)

                print(Signal_start_point,Signal_end_point)
                Z_signal = np.concatenate((Red,Green,Blue),axis=0)
                Z_signal = Z_signal.reshape((3,signal_x_size,signal_y_size))
                Z_signal = np.transpose(Z_signal, (2,1,0))
                Z_signal = np.pad(Z_signal,(column_pad,row_pad,(0,0)),'constant',constant_values=(0,0))
                Z_mask = np.zeros(signal_x_size*signal_y_size*3).reshape((3,signal_x_size,signal_y_size))
                Z_mask = np.transpose(Z_mask, (2,1,0))
                Z_mask = np.pad(Z_mask,(column_pad,row_pad,(0,0)),'constant',constant_values=(1,1))
                Z_new = image_shuffle*Z_mask + Z_signal*255
                Z_new = Z_new.astype(int)
                np.save(('patterns/test_'+str('%04d' % i)+'_'+str('%03d' % m)+'_signal'),np.array(Z_new))     
                image = np.load(('patterns/test_'+str('%04d' % i)+'_'+str('%03d' % m)+'_signal.npy'))
                print('patterns/test_'+str('%04d' % i)+'_'+str('%03d' % m)+'_signal.npy')
                im.set_data(image)
                plt.pause(0.1)

        else:
            for n in range(1,blank_frame_num,1):        
                image_shuffle = randomize_image(image_linearized, stim_x_size, stim_y_size)
                np.save(('patterns/test'+'_'+str('%04d' % i)+'_'+str('%03d' % n)+'_blank'),np.array(image_shuffle))
                image = np.load('patterns/test'+'_'+str('%04d' % i)+'_'+str('%03d' % n)+'_blank.npy')
                print(image.shape)
                im.set_data(image)
                plt.pause(0.1)
        rand_choice = round(np.random.random()*100)%chance
        print(np.average(time_interval))


    #plt.pause(30)

#This is necessary. It finally calls main function to run.
main()

