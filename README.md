# MDOT Project Roadmap 
## Issues to solve
### White noise experiments
    1. Increase frame rate in white noise stimulation
      Requiments: > 15 fps for 100 x 100 stimulation.
      Possible solutions:
        Solution 1. Use psychopy3  
        Solution 2. Refactor code
        Solution 3. Use a new strategy: 
            Create a movie first
            Annotate the timing of stimulus in a separate file.
            Compare response time with the annotation

    2. Turn background to back and set fullscreen

    3. Test the code on desktop experiment computer
    
### Road video experiments
    Module 1 - Road video response time:
       1. Create a timestamps file for road video experiment with the timestamp at the moment when the car passes the light
       2. Write code to 
             1. Use a video and timestamps file to measure relative response time
             2. export test file name, timestamps and reaction time. 
    
    Module 2 - Recording system:
       1. Use USB-6001 as a digitizer for recording. 
       2. Python code to record and control equipment: 
            1. Sending out synchronization signal for equipment to start presenting signal and recording
            2. Display live response
            3. Export data. 
            
    Module 3 - Data analysis:
