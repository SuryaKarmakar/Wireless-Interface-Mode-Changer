import subprocess

interfaceName = input("Enter your interface name :")
mode = input("Enter the mode (monitor,managed) :")

def modeChanger(interfaceName,mode):
    subprocess.call(["ifconfig",interfaceName,"down"])
    subprocess.call(["iwconfig",interfaceName,"mode",mode])
    subprocess.call(["ifconfig",interfaceName,"up"])
    subprocess.call(["iwconfig"])

modeChanger(interfaceName,mode)
