from weblocker import *

def main() -> None:
    try:
        weblocker = WebLocker()
        weblocker.run()
    except OSError as e:
        print(e)
    
if __name__ == '__main__':
    main()