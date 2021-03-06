[![Stories in Ready](https://badge.waffle.io/ariveralee/PiInTheSky.png?label=ready&title=Ready)](https://waffle.io/ariveralee/PiInTheSky)
# PiInTheSky

PiInTheSky is a security camera built using OpenCV and Raspberry Pi. The idea is to have a tracking algorithm that once is triggered by a PIR 
(motion) sensor, notifies the user of entry into their space VIA text and/or phone call.

---

## Broad Overview of what you'll need:

To implement this, you will need the following software and hardware:

### Software:
- Python | [Python Site](https://www.python.org/downloads/) - I'd say go with Python 2 instead of 3 as there's still more support for Python 2 regarding packages..

### Packages:
- Tons, I'll add them as I go along. Just a few to name off the start:
    - Pip
    - Numpy
    - Gpiozero - For the motion sensor
    - Picamera - For the camera module


### Libraries:
- OpenCV | [OpenCV Site](http://opencv.org/) - We will touch base on how to get this running on the Pi later.

### Hardware:
- **Raspberry Pi 3 Model B** | [Link Model B ](https://www.amazon.com/gp/product/B01CD5VC92/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1)

- **Raspberry Pi Camera Module V2** | [Camera Module](https://www.amazon.com/gp/product/B01ER2SKFS/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1)

- **Raspberry Pi case** | [Official Case](https://www.amazon.com/gp/product/B01F1PSFY6/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1)

- **PIR (motion) sensor** | [Link Adafruit](https://www.adafruit.com/products/189)

- **Micro SD card** | (preferably with the adapter) [Samsung EVO MicroSD](https://www.amazon.com/gp/product/B00IVPU786/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1)

- **CanaKit 5V 2.5 Raspberry Pi 3 Power Supply** | [Power Supply](https://www.amazon.com/gp/product/B00MARDJZ4/ref=oh_aui_detailpage_o03_s01?ie=UTF8&psc=1)

####Optional Hardware
- **Raspberry Pi Heatsink** | [Heatsinks](https://www.amazon.com/gp/product/B00HPQGTI4/ref=oh_aui_detailpage_o03_s01?ie=UTF8&psc=1) - Heatsinks are ~~not needed~~ are **HIGHLY** suggested to help dissipate the heat. As a matter of fact, I found that when I was installing OpenCV on the Pi, it would get hot to the point that it stopped the installation. 

- **USB Flash Memory Card Reader** | [Sabrent Card Reader](https://www.amazon.com/Sabrent-SuperSpeed-Windows-Certain-Android/dp/B00OJ5WBUE/ref=sr_1_4?s=pc&ie=UTF8&qid=1475681982&sr=1-4&keywords=sd%2Bcard%2Breader&th=1) - Get this if you don't have a card reader built-in to your pc or laptop.

- **HDMI Cable** | [Amazon HDMI Cable](https://www.amazon.com/AmazonBasics-High-Speed-HDMI-Cable-Standard/dp/B014I8SSD0/ref=sr_1_3?ie=UTF8&qid=1476410577&sr=8-3&keywords=hdmi%2Bcable&th=1) - This can be used in conjunction with a monitor (if it takes HDMI input) or a TV for when you're installing NOOBS and using the Pi.

- **Keyboard** | [Amazon Basics Keyboard](https://www.amazon.com/AmazonBasics-KU-0833-Wired-Keyboard/dp/B005EOWBHC/ref=sr_1_3?ie=UTF8&qid=1476410680&sr=8-3&keywords=keyboard) - Used to.. you guessed it! Type.

- **Mouse** | [Amazon Basics Mouse](https://www.amazon.com/AmazonBasics-3-Button-Wired-Mouse-Black/dp/B005EJH6RW/ref=sr_1_2?ie=UTF8&qid=1476410734&sr=8-2&keywords=mouse) - Used to.. point and click!

---

### Component Breakdown:
- **Raspberry Pi 3 Model B** - This is the latest model, comes with a built-in Bluetooth and Wi-Fi module. Due to this, I suggest looking to get this model.

- **Raspberry Pi Camera Module V2** - This module is capable of providing 1080P video at 30FPS or 720P video at 60FPS (Frame Per Second). This module is also capable of taking still frames. I suggest this module because in regards to performance, it's a lot faster and cheaper than a standard USB camera.

- **Raspberry Pi case** - This offical case is the best on the market right now. There's some issues with connecting external components, but this is definitely the go to!

- **PIR (motion) sensor** - This is an essential part of the project. The PIR sensor uses infrared detection to sense movement in a room. We will use this sensor to wake the camera to see our intruder.

- **Micro SD card** - Simply used for the installion of our operating system NOOBS (New Out Of the Box Software).

- **Raspberry Pi Heatsink** - Used to dissipate heat. Being as we are going to have a few components hooked up, we want to reduce the operating temperature as much as possible.

- **CanaKit 5V 2.5 Raspberry Pi 3 Power Supply** - Used to power the Raspberry Pi. For our implementation, USB power will most likely not be enough.

---

### Notes:


- You don't have to connect any peripheral devices to the PI or use a monitor to install. You could SSH in and do what is known as a "silent install" but for this tutorial, we will use a TV/Keyobard/Mouse combo.
- This has not been tested on any other Raspberry Pi hardware but this does not mean that it will not work

---

##Instructions

---
### Initial Setup:

1. Download the NOOBS zip (New Out Of the Box Software)
    - [NOOBS Link](https://www.raspberrypi.org/downloads/noobs/)


2. Format the SD card in the MS-DOS (FAT) format.


3. RaspberryPi.org has provided a good tutorial on how to setup NOOBS, definitely watch the video! 
    - [NOOBS Setup](https://www.raspberrypi.org/help/videos/)


4. Grab the Raspberry Pi and the Raspberry Pi Case. Lets disassemble the case so we can place the pi in:
    - Grab the edge of the top of the Pi case and hold the bottom with the other hand. You should be able to pull the top off as shown below:

        ![alt text](https://github.com/ariveralee/PiInTheSky/blob/master/images/topoff.JPG "Taking the top off")


    - Next, you need to pull the side pieces off, try to edge underneath and pull it out as shown below:

        ![alt text](https://github.com/ariveralee/PiInTheSky/blob/master/images/sidepiece.JPG "Taking the side off")


    - Once you're done, one of the sides will have an arrow as shown below. If you press on this and pull on the top of the case, it will come off fairly easily:

        ![alt text](https://github.com/ariveralee/PiInTheSky/blob/master/images/thearrow.JPG "separating the pieces")


    - Now take the Pi and insert the bottom first on an angle where the SD slot is as and press down as shown below:

        ![alt text](https://github.com/ariveralee/PiInTheSky/blob/master/images/insertpi.JPG "Placing the pi")


    - At this point, now is the perfect time to put the heatsinks on. Remove the adhesive from the bottom and attach them in the places shown below:

        ![alt text](https://github.com/ariveralee/PiInTheSky/blob/master/images/heatsink.JPG "Placing heat sinks")

    
    - Cool, now we can move to getting the rest of the case back on. Press the top of the case back on and the side pieces. At this point, lets leave the top cover off because we want the heat to vent while installing everything:

        ![alt text](https://github.com/ariveralee/PiInTheSky/blob/master/images/assembled.JPG "Pi assembled")


5. Now, if you followed the NOOBs installation properly, you should have your files on the SD card. Put the micro SD into the slot on the Raspberry pi.


6. Grab that Keyboard, Mouse, HDMI cable, Power cable for the Pi and a TV that no one is using in the house.
    - Plug the HDMI cable into a HDMI slot on the TV and the Raspberry Pi.

    - Plug in the Keyboard and Mouse into the USB slots on the Pi.

    - Plug in the power supply to an outlet and then into the Pi.

    - Viola! the Pi should be powering on. You should see an option to install Pixel. Select it and you should see a screen like the one below:

        ![alt text](https://github.com/ariveralee/PiInTheSky/blob/master/images/install.JPG "Installing Raspbian")


7. Grab a beer while you wait.

8. You should be lead to your desktop now. First things first, we need WIFI, so setup your WIFI.

9. Great, we are connected to the world! Time for some updates:
    - Open terminal (should be top right corner)
    
    - We are on a form of debian so we will be using apt-get for our upgrades and installations.
    
    - Let's start by upgrading installed packages:
    
    ```bash
    sudo apt-get update
    sudo apt-get upgrade
    sudo rpi-update
    ```

    - Now lets install the required developer tools and packages

    ```bash
    sudo apt-get install build-essential cmake pkg-config
    ```

    - Now we need some image I/O packages for our processing of images

    ```bash
    sudo apt-get install libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev
    ```

    - Time to install our GTK development library. This is used for building GUI's (Graphical User Interfaces) and is required to use OpenCV to view images on our screen.

    ```bash
    sudo apt-get install libgtk2.0-dev
    ```

    - We need to add on the necessay video I/O packages to load video files using OpenCV

    ```bash
    sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv41-dev
    ```

    - Cool, now we need some other libraries for optimizing operations within OpenCV

    ```bash
    sudo apt-get install libatlas-base-dev gfortran
    ```

10. Lets install pip
   
    ```bash
    wget https://bootstrap.pypa.io/get-pip.py
    sudo python get-pip.py
    ```

11. Next up, We want to install virtualenv and virtualenvwrapper:
    
    ```bash
    sudo pip install virtualenv virtualenvwrapper
    sudo rm -rf ~/.cache/pip
    ```
12. We must now update our `~/.profile` file to include the following:
    
    ```bash
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
    ```

13. Add this to your `.bashrc` / `.bash_profile` / `.zshrc` :
    
    ```bash
    # load virtualenvwrapper for python (after custom PATHs)
    venvwrap="virtualenvwrapper.sh"
    /usr/bin/which -a $venvwrap
    if [ $? -eq 0 ]; then
    venvwrap=`/usr/bin/which $venvwrap`
    source $venvwrap
    fi
    ```

14. Lets source our files to get our changes in:

    ```bash
    source ~/.profile
    source ~/.bashrc  # or .bash_profile / .zshrc
    ```

15. Create our OpenCV virtual environment:

    ```bash
    mkvirtualenv cv
    ```

16. Awesome! Now we can install Python 2.7

    ```bash
    sudo apt-get install python2.7-dev
    ```

    We also need Numpy because OpenCV Python represents images as multi-dimension Numpy arrays:

    ```bash
    pip install numpy
    ```

17. Now the most important part, OpenCV:

    ```bash
    wget -O opencv-3.1.0.zip https://sourceforge.net/projects/opencvlibrary/files/latest/download?source=directory
    unzip opencv-3.1.0.zip
    cd opencv-3.1.0
    ```

    Setup the build

    ```bash
    mkdir build
    cd build
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_NEW_PYTHON_SUPPORT=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON  -D BUILD_EXAMPLES=ON ..
    ```

    We compile OpenCV (**Note that this could take up to 3 hours on the Pi!**):

    ```bash
    make
    ```

    Last but not least, We install OpenCV:

    ```bash
    sudo make install
    sudo ldconfig
    ```

18. OpenCV should be installed in:

    ```bash
    /usr/local/lib/python2.7/site-packages
    ```

    In order for us to use OpenCV in our Virtual Environment (cv), we need to link it:

    ```bash
    cd ~/.virtualenvs/cv/lib/python2.7/site-packages/
    ln -s /usr/local/lib/python2.7/site-packages/cv2.so cv2.so
    ln -s /usr/local/lib/python2.7/site-packages/cv.py cv.py
    ```

19. Lets see if it works!:

    ```bash
    workon cv
    python
    ```

    ```python
    import cv2
    cv2.__version__
    '3.1.0'
    ```
    

If Python and OpenCV is successfully installed on our PI. the above should work with no problems.

___

### Attaching Components to the Pi


TBA ;-)









