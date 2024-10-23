


To use your Android phone’s camera as a PC webcam on Linux, you can utilize the DroidCam app. Here’s a step-by-step guide:

1. **Install DroidCam on your Android phone**: Download and install the DroidCam app from the Google Play Store.
2. **Install the DroidCam Linux client**: Follow the instructions to install the DroidCam Linux client on your Ubuntu or Linux Mint system. You can download the client from the official DroidCam website.
4. **Configure DroidCam**: Launch the DroidCam app on your phone and set it to use the camera and microphone. You can choose the video quality and other settings as desired.
5. **Start the DroidCam server**: On your Linux PC, run the command `sudo ./install-client` (assuming you extracted the DroidCam client archive to a directory) to start the DroidCam server.



1. **Enable USB debugging on your Android phone**: Enable developer mode and USB debugging on your phone to allow it to connect to your Linux PC via USB.
2. **Install ADB on your Linux PC**: Install Android Debug Bridge (ADB) on your Linux PC using the command `sudo apt install adb`.
3. **Connect your phone to your Linux PC**: Use a USB cable to connect your phone to your Linux PC. Run the command `adb devices` to verify the connection.


6. **Configure your Linux system to recognize the phone camera**: Run the command `sudo modprobe v4l2loopback` to load the v4l2loopback kernel module, which allows your Linux system to recognize the phone camera as a virtual webcam device.
7. **Test the phone camera as a PC webcam**: Use a video conferencing application like Skype, Zoom, or Google Meet to test the phone camera as a PC webcam. You should see your phone’s camera feed on your Linux PC.



v4l2loopback-dkms


sudo pacman -S v4l2loopback-dkms linux-headers v4l-utils v4l2loopback-utils
sudo modprobe v4l2loopback


sudo pacman -S android-tools


