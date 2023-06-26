from ppadb.client import Client

class Control:
    def __init__(self):
        self.device = Client(host='127.0.0.1', port=5037).devices()[0]

    def tap(self, x, y):
        self.device.shell(f'input tap {x} {y}')

    def screenshot(self):
        screenshot = self.device.screencap()

        with open('result.png', 'wb') as f:
            f.write(screenshot)
            print('Saved screenshot to result.png')

    def open_app(self, package_name):
        self.device.shell('monkey -p {} -c android.intent.category.LAUNCHER 1'.format(package_name))

    def close_app(self, package_name):
        self.device.shell('am force-stop {}'.format(package_name))

    def swipe(self, x0, y0, x1, y1):
        self.device.shell(f'input swipe {x0} {y0} {x1} {y1}')

