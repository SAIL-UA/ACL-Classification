# ACL-Classification
To start with the areas where the data changes from walking to jogging and for jogging to running have to be identified for each of the participants. In order to do so the data needs to be displayed and observed to see instances where the graph makes a clear change. If no change is evident, a general guess can be made based off the length of time each patient did the activity for. In the instance where the patient did not do an excercise (usually running), it is ignored and only the other parts are gathered. The code for file display is already added under Data_Graphing. The picture below is the output from running the code for a patient. 

<img width="650" alt="428_ACLR_273_All_Data" src="https://github.com/SAIL-UA/ACL-Classification/assets/149837589/d242babc-0aea-4f50-aa1e-8466d89ea97d">

There are two clear instances where the data makes a drastic change due to the height and position of the bars. The two instances are somewhere between the 15000th and 20000th index and 25000th and 31000th index after downsampling, respectively. However, the exact instances can be hard to see so the window can be changed to view the graph in more detail. In this case, 17000 and 19000 were chosen to view the first change which would be walking to jogging as they occur first. The image is added below. 

<img width="674" alt="image" src="https://github.com/SAIL-UA/ACL-Classification/assets/149837589/269f6de2-f251-4fee-bac0-ed7ded6c1602">

In this image, the change can be viewed much clearer and the indices are more precise. Now the change is noted down and this proceeds for the second instance. Next up the data needs to be sliced into 1 second intervals (600 window size) and then sorted into files. To create the files the code in File Creator is used, it generates 2 layers of files with the first layer being 5 files each with the patient's name and then the sensor and another one with the patient's name and slices where everything is put eventually. The second for each of the five has the patient name, sensor, and the action (walking, jogging, and running) as the title where later each of the files are stored. An image of the first layer generated is below.

<img width="518" alt="image" src="https://github.com/SAIL-UA/ACL-Classification/assets/149837589/747a0952-9f0b-4a4c-aaad-1962d3b7fd25">

Finally, the data needs to be sliced using the code in File Creator. The code slices all the data inbetween a set of specified indices into 600 index length CSV files. The code reads all the paths for each of the files and cuts from 0 to the first specified index for walking. Then, from the first specified index to the second specified index and then finally from the second specified index to the end. After, the data is saved into each of the earlier made files. The files are saved with the patient's name, the sensor whose data was used, the action being sliced (walking, jogging, running) and the start index. An example from one of the patient's data is below along with a screenshot of the finished data.

<img width="536" alt="image" src="https://github.com/SAIL-UA/ACL-Classification/assets/149837589/52d51873-737b-4cb6-94f4-39f372a72873">

<img width="631" alt="image" src="https://github.com/SAIL-UA/ACL-Classification/assets/149837589/76ffd868-b631-4796-b440-63d20699d5a4">

This process occurs for every patient in the data used. 
