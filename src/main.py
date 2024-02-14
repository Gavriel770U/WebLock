from weblocker import *
import platform

if WINDOWS == platform.system():
    from pyuac import main_requires_admin

    @main_requires_admin
    def windows_main() -> None:
        try:
            weblocker = WebLocker()
            weblocker.run()
            #w = WebLockerHostsManager()
            #w.delete_from_hosts('www.instagram.com')
        except OSError as e:
            print(e)

if LINUX == platform.system():
    def linux_main() -> None:
        try:
            weblocker = WebLocker()
            weblocker.run()
        except OSError as e:
            print(e)

def main() -> None:
    if LINUX == platform.system():
        linux_main()
    elif WINDOWS == platform.system():
        windows_main()
        
if __name__ == '__main__':
    main()