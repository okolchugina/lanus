import os


def lock():
    os.system('loginctl lock-session')


def unlock():
    os.system('loginctl unlock-session')
