# A simple realtime face recognition application using OpenCV 

## What is this magic?
It basically checks for one specific face based on a jpg file.

## How it works
<ol>
<li> it'll make a "sample" of the face. This can be obtained with the capture_face_dump.py script</li>
</li> 
<li>The "sample" of the face can be found in ./target_face.jpg</li>
<li>
The main.py script will use the device's camera to process each frame
</li>
<li>It'll do an analysis of the face dumped in target_face.jpg</li>
</ol>
Note that the speed of analyzing the face is determined by the hardware.

On my computer (Intel i5 4 cores & 8GB ram) it took **3 seconds**  to process every frame. That can be different between each computer.

## How to use
1.Install the required modules
```
python -m pip install -r requirements.txt # on Windows
python3 -m pip install -r requirements.txt # on linux and other distributions
```

2.Make a "sample" of of  the target's face

```
python capture_face_dump.py
```

<ul>
<li> Press space to make a picture  </li>
<li> Press Q to close the application </li>
</ul>


3. And finally, run the main script
```
python main.py
```
You'll see that in the console will be printed if it found the target's face or not

Press the ``q`` button while focused on the opencv created window to close the project

***Note that this project is not recommended to be used in real projects for production. Processing the image is slow and it's not optimized***