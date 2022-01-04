# Mindstorms python

Here some of my python scripts for LEGO® MINDSTORMS® Robot Inventor

When you have questions remarks or improvements please let me know

## Using Mindstorms on Ubuntu with VS code

- Connect your mindstorms brick via usb-cable or bluetooth
- When on bluetooth create a serial connection (done with blueman)
- Set the device to rw for all `sudo chmod /dev/ttyAMC0 666` or `sudo chmod /dev/rfcomm0 666`
- Set device to be owned by you `sudo chown $(whoami) /dev/ttyAMC0` or `sudo chown $(whoami) /dev/rfcomm0`
- Start VS code with the following pluging  [lego-spikeprime-mindstorms](https://marketplace.visualstudio.com/items?itemName=PeterStaev.lego-spikeprime-mindstorms-vscode&ssr=false#review-details)
- When VS Code was started before changing rights you will not be able to connect to your Mindstorms brick
- Connect to your Mindstorms brick at the bottom of your screen by selecting the correct serialport