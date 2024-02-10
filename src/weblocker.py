import os

class WebLocker(object):
    def __init__(self) -> None:
        if 'nt' == os.name:
            self.__hosts_path = ''  
        else:
            raise OSError(f'WebLocker does not support OS [{os.name}]')
    
    def run(self) -> None:
        while True:
            pass