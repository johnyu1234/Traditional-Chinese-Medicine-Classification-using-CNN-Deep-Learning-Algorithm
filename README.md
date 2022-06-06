# Traditional-Chinese-Medicine-Classification-using-CNN-Deep-Learning-Algorithm
A mobile application with camera feature and model prediction.

## Note
This app is developed on Samsung Galaxy S10+.
If app is used on another phone, some adjustment in the code has to be made to suit the dimension of the device.

## Install:

- Flutter
- Python 3.x
- Python packages (OpenCv2, fastapi, keras, and etc.)
- IDE (VS Code, Android Studio, etc.)

## Flutter installation guide

1. Go to Flutter official website [here](https://flutter.dev/docs/get-started/install).
2. Select which OS on which you are installing Flutter on.
3. Follow detailed guides.

## IDE: VS Code installation guide

1. Download VS Code [here](https://code.visualstudio.com/).
2. Once download is finished, start VS Code.
3. Go to Extensions tab on the left-hand side or click and hold (Ctrl+Shift+X).
    * If above instruction doesn't work, click View -> Command Palette.
    * Type "install", and select Extensions: Install Extensions.
4. Type "flutter" in the extensions search field, select Flutter in the list, and click Install. This also installs the required Dart plugin.
5. Validate setup using Flutter Doctor:
    * Invoke View -> Command Palette.
    * Type “doctor”, and select the Flutter: Run Flutter Doctor.
    * Review the output in the OUTPUT pane for any issues. Make sure to select Flutter from the dropdown in the different Output Options.
6. Cross-check your installations [here](https://flutter.dev/docs/development/tools/vs-code).

## IDE: Android Studio installation guide
Refer the installation guide [here](https://flutter.dev/docs/development/tools/android-studio).

## How to deploy app (Android)
Make sure device has version Android Oreo or higher.
Below is the instruction on how to deploy app to device:

### Deploy in VS Code

1. In VS Code, make sure there is a target device on bottom corner right-hand side.
    * If No device is shown, it means target device is not found or device not properly plugged in.
    * Make sure your device has enabled developer option [here](https://www.digitaltrends.com/mobile/how-to-get-developer-options-on-android/).
2. Once target device is found, click F5 or go to Run and Debug tab on the left menu pane and press the green button on top to deploy app to device.

Process might take a while before the app can run on the device.

### Deploy in Android Studio

1. In Android Studio, make sure that in the Flutter Device Selection is the device you want to deploy in.
    * If No device is shown, it means target device is not found or device not properly plugged in.
    * Make sure your device has enabled developer option [here](https://www.digitaltrends.com/mobile/how-to-get-developer-options-on-android/).
2.  Once target device is found, click Shift + F10 or press the green arrow/Run Button  on the top right menu pane to deploy app to device.

Process might take a while before the app can run on the device.

## For dimension adjustment:
* Change the fontsize of the text
* Change the height of the sizedbox widget
* Change the padding and margin of the container


## Server
- Our server is run through locally on our laptop.
###### for Windows
- you would need to deactivate your firewall in order to allow the mobile application to access the server
##### for MacOs/Linux
- no firewall deactivation neeeded
##### Running the server
1. in order to run the server, you would need to download all the dependencies/libaries that has been included in the python file (Tcm_api.py)
2. make sure you are connected with the same wifi with as the mobile application  
3. python3 Tcm_api.py
4. Server is now running


## Contributions
* Model Development: 余更忠 F74077023
* App Development: 蔡孝龍 F74077120 +  余更忠 F74077023
* Server integration: 余更忠 F74077023



