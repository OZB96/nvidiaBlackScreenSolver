#   ____ __________  
#  / __ \___  /  _ \ 
# | |  | | / /| |_) |
# | |  | |/ / |  _ < 
# | |__| / /__| |_) |
#  \____/_____|____/ 
# Version 0.1 Beta
import os


def main():
    print("Welcome...")
    who = os.popen("whoami").read()
    if who != "root\n":
        print("You must be root")
        exit()
    verfiy()
    ff = open("tmp.txt", "a+")
    ff.close
    f = open("tmp.txt", "r")
    fr = f.read()
    print(fr)
    if fr == '1\n':
        print("Run Nvidia Driver")
        os.system("echo 2 > tmp.txt")
        f.close()
        exit()
    elif fr == '2\n':
        psi = os.popen("nvidia-xconfig --query-gpu-info | grep 'BusID : ' | cut -d ' ' -f6").read()
        psi = psi[:-1]
        f1 = open("xorg.conf", "w+")
        f1.write('Section "ServerLayout"\n    Identifier "layout"\n    Screen 0 "nvidia"\n    Inactive "intel"\nEndSection\n\nSection "Device"\n    Identifier "nvidia"\n    Driver "nvidia"\n    BusID "{0}"\nEndSection\n\nSection "Screen"\n    Identifier "nvidia"\n    Device "nvidia"\n    Option "AllowEmptyInitialConfiguration"\nEndSection\n\nSection "Device"\n    Identifier "intel"\n    Driver "modesetting"\nEndSection\n\nSection "Screen"\n    Identifier "intel"\n    Device "intel"\nEndSection'.format(psi))
        f1.close()
        os.system("sudo mv xorg.conf /etc/X11/")
        print("Finished")
        os.system("reboot")
        exit()
    disableNouveau()

def verfiy():
    o = os.popen("sudo lspci | grep -E 'VGA|3D' | grep -i nvidia").read()
    if o == "":
        print("make sure that you have a Nvidia Graphic Card")
        exit()
    else:
        s = o.split("[")
        t = s[1].split("]")
        print("{0} found ".format(t[0]))
        print("\n Preceding ...")


def disableNouveau():
        os.system("sudo echo -e 'blacklist nouveau\noptions nouveau modeset=0\nalias nouveau off' > /etc/modprobe.d/blacklist-nouveau.conf")
        #in case Debian Destribution put instead of 'dracut -f', put 'update-initramfs -u'

        os.system("sudo dracut -v -f && reboot")
        os.system("sudo echo -e '1' > tmp.txt ")
        # os.system("reboot")



if __name__ == "__main__": main()
