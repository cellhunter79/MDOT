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
road_im = Image.open("road2.png")  # choose pictures and directions.
image_raw = np.array(road_im)
stim_x_size=150 ## size of your final noise stimulation
stim_y_size=150

chance = 3 # chance of displaying the bar

signal_x_size = 50 #size of the bar
signal_y_size = 50
################################################3
x_res = road_im.size[0] 
y_res = road_im.size[1]



def main():
    #1. Randomize image and produce image and image_shuffle
    image,image_shuffle = randomize_image()

    #2. Plot the image and note the initiation time point
    line1, im = plotimage(image,image_shuffle)
    time_display = time.time()    
    fig.canvas.mpl_connect('button_press_event', on_press)

    #3. display new image
    make_new_image(image,image_shuffle,line1,im,time_interval)
    #3. Make image with randomize pixels from a picture.
    

    #x Final report
    final_report()

def randomize_image():
    x_ram_loc = np.random.randint(0,high=x_res-stim_x_size)
    y_ram_loc = np.random.randint(0,high=y_res-stim_y_size)
    image_temp = image_raw.reshape(x_res*y_res,3)
    np.random.shuffle(image_temp)
    image_shuffle = image_temp.reshape((x_res,y_res,3))
    image = image_shuffle[x_ram_loc:(x_ram_loc+stim_x_size),y_ram_loc:(y_ram_loc+stim_y_size),:]
    return image, image_shuffle
    
def plotimage(image,image_shuffle):
    global fig
    fig, ax1 = plt.subplots(figsize = (10,10))
    plt.ion()
    plt.show(block=False)
    im = plt.imshow(image)
    fig_result = plt.figure()
    ax_result = plt.subplot(111)
    line1, = ax_result.plot(np.arange(len(time_interval)),time_interval)
    ax_result.set_ylim([0,delay+0.5])
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

def make_new_image(image,image_shuffle, line1, im,time_interval):
    global time_display
    rand_choice = round(np.random.random()*100)%chance
    for i in range(1,300,1):
        m =0
        if rand_choice == 0:
            ## display a figure at random time
            start_p = np.random.choice(stim_x_size-signal_x_size)
            end_p = np.random.choice(stim_y_size-signal_y_size)
            Signal_start_point = (start_p,(stim_x_size-start_p))
            Signal_end_point = (end_p,(stim_y_size-end_p))

            row_pad = (start_p,(stim_x_size-start_p-signal_x_size))
            column_pad =(end_p,(stim_y_size-end_p-signal_y_size))

            x_ram_loc = np.random.randint(0,high=x_res-stim_x_size)
            y_ram_loc = np.random.randint(0,high=y_res-stim_y_size)
            
            image = image_shuffle[x_ram_loc:(x_ram_loc+stim_x_size),y_ram_loc:(y_ram_loc+stim_y_size),:]
            print(image.shape, image_shuffle.shape)
            time_display = time.time()
            for m in range(1,10,1):
                Red = np.random.uniform(0,1,signal_x_size*signal_y_size)
                Green = np.full((signal_x_size*signal_y_size),0)
                Blue = np.full((signal_x_size*signal_y_size),0)

                print(Signal_start_point,Signal_end_point)
                Z_signal = np.concatenate((Red,Green,Blue),axis=0)
                Z_signal = Z_signal.reshape((3,signal_x_size,signal_y_size))
                Z_signal = np.transpose(Z_signal, (2,1,0))
                Z_signal = np.pad(Z_signal,(column_pad,row_pad,(0,0)),'constant',constant_values=(0,0))
                Z_mask = np.zeros(signal_x_size*signal_y_size*3).reshape((3,signal_x_size,signal_y_size))
                Z_mask = np.transpose(Z_mask, (2,1,0))
                Z_mask = np.pad(Z_mask,(column_pad,row_pad,(0,0)),'constant',constant_values=(1,1))
                Z_new = image*Z_mask/255 + Z_signal
                np.save(('patterns/test'+str(i)+'_'+str(m)),np.array(Z_new))
                Z_new = np.load('patterns/test'+str(i)+'_'+str(m)+'.npy')
                im.set_data(Z_new)
                plt.pause(0.25)
                
                x_ram_loc = np.random.randint(0,high=x_res-stim_x_size)
                y_ram_loc = np.random.randint(0,high=y_res-stim_y_size)
                image = image_shuffle[x_ram_loc:(x_ram_loc+stim_x_size),y_ram_loc:(y_ram_loc+stim_y_size),:]
                
                np.save(('patterns/test'+str(i)+'_'+str(m)+'blank'),np.array(Z_new))     
                image = np.load(('patterns/test'+str(i)+'_'+str(m)+'blank.npy'))
                im.set_data(image)
                plt.pause(0.25)

            print(time_interval)
            print(np.average(time_interval))
            
            print(reaction_time)
            line1.set_xdata(np.arange(len(time_interval)))
            line1.set_ydata(time_interval)

        else:        
            plt.pause(0.25)
            x_ram_loc = np.random.randint(0,high=x_res-stim_x_size)
            y_ram_loc = np.random.randint(0,high=y_res-stim_y_size)
            image = image_shuffle[x_ram_loc:(x_ram_loc+stim_x_size),y_ram_loc:(y_ram_loc+stim_y_size),:]
            np.save(('patterns/test'+str(i)+'_0'),np.array(image))
            image = np.load('patterns/test'+str(i)+'_0.npy')
            print(image.shape)
            im.set_data(image)
            plt.pause(0.25)
        rand_choice = round(np.random.random()*100)%chance
        print(np.average(time_interval))

def final_report():
    reaction_time = "Reaction Time: " + str(np.average(time_interval))
    plt.text(0,-1,reaction_time,color = "red", fontsize = 18)
    plt.pause(30)

#This is necessary. It finally calls main function to run.
main()
