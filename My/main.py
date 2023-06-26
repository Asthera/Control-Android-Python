import time
from libsimple import Control


app = 'app'


def clean_app(control):
    control.close_app(app)
    time.sleep(1)
    control.open_app(app)
    time.sleep(2)
    control.tap(1018, 2316)
    time.sleep(2)
    control.tap(400, 1840)
    time.sleep(2)
    control.tap(180, 775)
    time.sleep(2)
    control.tap(760, 1368)
    time.sleep(2)
    control.screenshot()


def swipe_to_n_acc(control, n):
    "N from 1"
    control.swipe(500, 1350, 500, 1150)
    time.sleep(3)
    for i in range(n - 2):
        control.swipe(500, 1350, 500, 1180)
        time.sleep(1)


def attemp_on_n(control, n):
    control.open_app(app)
    time.sleep(6)
    control.tap(600, 2055)
    time.sleep(3)
    control.tap(500, 460)
    time.sleep(5)
    control.tap(600, 2052)
    time.sleep(1)
    control.tap(550, 1962)
    time.sleep(3)

    swipe_to_n_acc(control, n)

    control.tap(385, 752)
    time.sleep(5)

    for i in range(3):
        control.tap(600, 1938)
        time.sleep(7)
    time.sleep(5)
    control.screenshot()



control = Control()

control.open_app()

clean_app(control)
attemp_on_n(control, 7)
