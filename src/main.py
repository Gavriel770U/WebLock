from weblocker import *
import platform

if platform.system() == 'Windows':
    from pyuac import main_requires_admin

    @main_requires_admin
    def windows_main() -> None:
        try:
            weblocker = WebLocker()
            weblocker.run()
        except OSError as e:
            print(e)

if platform.system() == 'Linux':
    def linux_main() -> None:
        try:
            weblocker = WebLocker()
            weblocker.run()
        except OSError as e:
            print(e)

def main() -> None:
    linux_main()
    print(platform.system())

if __name__ == '__main__':
    main()