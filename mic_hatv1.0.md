---
title: MIC HAT v1.0
category:
bzurl:
oldwikiname:
prodimagename:
surveyurl:
sku:
---

换一张封面图
![](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/mic_hatv1.0.png?raw=true)

ReSpeaker 2-Mics Pi HAT is a dual-microphone expansion board for Raspberry Pi designed for AI and voice applications. This means that you can build a more powerful and flexible voice product that integrates Amazon Alexa Voice Service, Google Assistant, and so on.


The board is developed based on WM8960, a low power stereo codec. There are 2 microphones on both sides of the board for collecting sounds and it also provides 3 APA102 RGB LEDs, 1 User Button and 2 on-board Grove interfaces for expanding your applications. What is more, 3.5mm Audio Jack or JST 2.0 Speaker Out are both available for audio output.

## Features

* Raspberry Pi compatible(Support Raspberry Pi Zero, Raspberry Pi 1 B+, Raspberry Pi 2 B and Raspberry Pi 3 B)
* 2 Microphones
* 2 Grove Interfaces
* 1 User Button
* 3.5mm Audio Jack
* JST2.0 Speaker Out

## Application Ideas

* Voice Interaction Application
* AI Assistant

## Hardware Overview

![](https://github.com/SeeedDocument/MIC_HATv1.0_for_raspberrypi/blob/master/img/mic_hatv1.0.png?raw=true)

- BUTTON: a User Button, connected to GPIO17
- MIC_L & MIC_R: 2 Microphones on both sides of the board
- RGB LED: 3 APA102 RGB LEDs, connected to SPI interface
- WM8960: a low power stereo codec
- Raspberry Pi 40-Pin Headers: support Raspberry Pi Zero, Raspberry Pi 1 B+, Raspberry Pi 2 B and Raspberry Pi 3 B
- POWER: Micro USB port for powering the ReSpeaker 2-Mics Pi HAT, please power the board for providing enough current when using the speaker.
- I2C: Grove I2C port, connected to I2C-1
- GPIO12: Grove digital port, connected to GPIO12 & GPIO13
- JST 2.0 SPEAKER OUT: for connecting speaker with JST 2.0 connector
- 3.5mm AUDIO JACK: for connecting headphone or speaker with 3.5mm Audio Plug

## Usage

### Connect ReSpeaker 2-Mics Pi HAT to Raspberry Pi

Mount ReSpeaker 2-Mics Pi HAT on your Raspberry Pi, make sure that the pins are properly aligned when stacking the ReSpeaker 2-Mics Pi HAT.

补图片
![connection picture1]()
![connection picture2]()

### Setup the driver on Raspberry Pi

While the upstream wm8960 codec is not currently supported by current Pi kernel builds, upstream wm8960 has some bugs, we had fixed it. we must build it manually. Or you could download and use our 补链接[raspbian image(click for guidance)](), in which the driver is pre-installed.

Get the seeed voice card source code.
```
git clone --depth=1 http://git.oschina.net/seeed-se/seeed-voicecard
cd seeed-voicecard
sudo ./install.sh
reboot
```

Check that the sound card name matches the source code seeed-voicecard.

```
pi@raspberrypi:~ $ aplay -l
**** List of PLAYBACK Hardware Devices ****
card 0: seeedvoicecard [seeed-voicecard], device 0: bcm2835-i2s-wm8960-hifi wm8960-hifi-0 []
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```
Next apply the alsa controls setting
```
sudo alsactl --file=asound.state restore
```
If you want to change the alsa settings, You can use `sudo alsactl --file=asound.state store` to save it.

Test, you will hear what you say to the microphones(don't forget to plug in an earphone or a speaker):
```
arecord -f cd -Dhw:0 | aplay -Dhw:0
```
Enjoy!

### Configure sound settings and adjust the volume with **alsamixer**

介绍alsamixerhttps://en.wikipedia.org/wiki/Alsamixer
命令行一句
截图一张
测试音量大小

### Getting started with **Google Assistant**

There are 2 ways to get started with Google Assistant([what is  Google Assistant](https://assistant.google.com/)): the first is that you could integrate the Google Assistant Library into your raspberry pi system. Here is the link to [Google official guidance](https://developers.google.com/assistant/sdk/prototype/getting-started-pi-python/run-sample). And the other way is that you could download the [raspbian image](https://s3-us-west-2.amazonaws.com/wiki.seeed.cc/001share/seeed-raspbian-jessie-20170523.7z) we built, in which the Google Assistant Library and  example are pre-installed. The following guide will show you how to get started with Google Assistant.

1. Configure a Developer Project and get JSON file

    Follow step 1. 2. 3. 4. in the  [guide](https://developers.google.com/assistant/sdk/prototype/getting-started-pi-python/config-dev-project-and-account#config-dev-project) to configure a project on Google Cloud Platform and create an OAuth Client ID JSON file.

2. fff
    Authorize the Google Assistant SDK sample to make Google Assistant queries for the given Google Account. Reference the JSON file you copied over to the device in a previous step.

3. Start the Google Assistant demo
    ```
    pi@raspberrypi:~ $ alsamixer    // To config
    pi@raspberrypi:~ $ source env/bin/activate
    (env) pi@raspberrypi:~ $ env/bin/google-assistant-demo
    ```
    ![alsamixer_pic]()
    ![run demo]()



### How to use APA102 LEDs

介绍APA102 led灯及如何使用该库（example）

APA102 LEDs are addressed with SPI,

- Activate SPI: sudo raspi-config; Go to "Interfacing Options"; Go to "SPI"; Enable SPI; Exit the tool and reboot
-
- Get the APA102 Library and sample light programs:
- You might want to set the number of LEDs to match your strip: cd APA102_Pi && nano runcolorcycle.py; Update the number, Ctrl-X and "Yes" to save.
- Run the sample lightshow: python3 runcolorcycle.py

### How to use Button

如何使用button

### About our raspbian image

介绍如何使用这个image

## Resources
[raspbian image](https://s3-us-west-2.amazonaws.com/wiki.seeed.cc/001share/seeed-raspbian-jessie-20170523.7z)
[原理图]
[google assistant link]
