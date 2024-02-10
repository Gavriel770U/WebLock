import os

class WebLocker(object):
    def __init__(self) -> None:
        if 'nt' == os.name:
            self.__hosts_path = r'C:\Windows\System32\Drivers\etc\hosts'  
        else:
            raise OSError(f'WebLocker does not support OS [{os.name}]')
    
    def __write_to_hosts(self, website_url: str) -> None:
        with open(self.__hosts_path, 'a') as hosts_file:
            hosts_file.write(website_url)
    
    def run(self) -> None:
        self.__write_to_hosts('www.instagram.com')
        
        #while True:
        #    pass