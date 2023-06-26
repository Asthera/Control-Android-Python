# Why you need it ?
Maybe you need todo testing or automation on you android device by you pc by pure-python android developer bridge.

## Connecting
1. Give all acceses on your phone for usb debugging.(Once)
2. Download ppadb on your pc, and run adb server(you need just Adroid Studio running)
3. Connect phone to pc by usb cable.
4. Run script on Python
See result

## Commands (basic)
~~~
from ppadb.client import Client

# Connecting
device = Client(host='127.0.0.1', port=5037).devices()[0]

# Tap
x, y = 15, 15
device.shell(f'input tap {x} {y}')

package_name = "com.google.android.youtube" # Youtube

# Opening, closing app. You need a package nape of app
device.shell('monkey -p {} -c android.intent.category.LAUNCHER 1'.format(package_name)) 
device.shell('am force-stop {}'.format(package_name))

#  Swipe
x0, y0, x1, y1 = 100, 200, 100, 500
device.shell(f'input swipe {x0} {y0} {x1} {y1}') 
~~~
### Other commands
[About library](https://pypi.org/project/pure-python-adb/), 
[More simple](https://itnext.io/how-you-can-control-your-android-device-with-python-45c3ab15e260)
## How works x, y

For finding x,y you can use screenshot and finding in it point in pixels, in photo editor.

![Cordinates](https://github.com/Asthera/Control-Android-Python/blob/main/1*VCKZWOpxz_dgLtYXbxgFPA.webp)



