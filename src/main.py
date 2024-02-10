from weblocker import *
from pyuac import main_requires_admin

@main_requires_admin
def main() -> None:
    try:
        weblocker = WebLocker()
        weblocker.run()
    except OSError as e:
        print(e)
    
if __name__ == '__main__':
    main()