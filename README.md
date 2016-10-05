# PiInTheSky

PiInTheSky is a security camera built using OpenCV and Raspberry Pi. The idea is to have a tracking algorithm that once is triggered by a PIR 
(motion) sensor, notifies the user of entry into their space VIA text and/or phone call.

To implement this, you will need the following software and hardware:

### Libraries:
- OpenCV [OpenCV Site](http://opencv.org/)

### Hardware:
- Raspberry Pi 3 Model B | [Link Model B ](https://www.amazon.com/gp/product/B01CD5VC92/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1)
- Raspberry Pi Camera Module V2 | [Camera Module](https://www.amazon.com/gp/product/B01ER2SKFS/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1)
- Raspberry Pi case | [Official Case](https://www.amazon.com/gp/product/B01F1PSFY6/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1)
- PIR (motion) sensor | [Link Adafruit](https://www.adafruit.com/products/189)
- Micro SD card | (preferably with the adapter) [Samsung EVO MicroSD](https://www.amazon.com/gp/product/B00IVPU786/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1)
- Raspberry Pi Heatsink | [Heatsinks](https://www.amazon.com/gp/product/B00HPQGTI4/ref=oh_aui_detailpage_o03_s01?ie=UTF8&psc=1)
- CanaKit 5V 2.5 Raspberry Pi 3 Power Supply | [Power Supply](https://www.amazon.com/gp/product/B00MARDJZ4/ref=oh_aui_detailpage_o03_s01?ie=UTF8&psc=1)

### Component Breakdown:
- Raspberry Pi 3 Model B - This is the latest model, comes with a built-in Bluetooth and Wi-Fi module. Due to this, I suggest looking to get this model.
- Raspberry Pi Camera Module V2 - This module is capable of providing 1080P video at 30FPS or 720P video at 60FPS (Frame Per Second). This module is also capable of taking still frames. I suggest this module because in regards to performance, it's a lot faster and cheaper than a standard USB camera.
- Raspberry Pi case - This offical case is the best on the market right now. There's some issues with connecting external components, but this is definitely the go to!
- PIR (motion) sensor - This is an essential part of the project. The PIR sensor uses infrared detection to sense movement in a room. We will use this sensor to wake the camera to see our intruder.
- Micro SD card - Simply used for the installion of our operating system NOOBS (New Out Of the Box Software).
- Raspberry Pi Heatsink - Used to dissipate heat. Being as we are going to have a few components hooked up, we want to reduce the operating temperature as much as possible.
- CanaKit 5V 2.5 Raspberry Pi 3 Power Supply - Used to power the Raspberry Pi. For our implementation, USB power will most likely not be enough.

### Notes:
- This has not been tested on any other hardware but this does not mean that it will not work
- Heatsinks are not necessary but **highly suggested**; the Pi can get hot.
