# A simple realtime face recognition application using OpenCV 

## How this works

It basically checks for one specific face based on a jpg file.

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