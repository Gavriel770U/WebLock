"""
    WebLocker Constants divided into separate groups.
"""

#==== Operation Systems ====
LINUX: str = "Linux"
WINDOWS: str = "Windows"
#===========================

#==== Hosts File Paths =====
WINDOWS_HOSTS_PATH: str  = r'C:\Windows\System32\Drivers\etc\hosts'
LINUX_HOSTS_PATH: str = r'/etc/hosts'
#===========================

#==== Cache Clear Support ==
RESOLVECTL_DISTROS: tuple = (
    'Linux Mint',
    'Freedesktop SDK', # Fedora
)
#===========================

#==== Window Properties ====
WIDTH: int = 600
HEIGHT: int = 400
#===========================

#===== File Management =====
FILE_APPEND: str = 'a'
FILE_READ: str = 'r'
FILE_WRITE: str = 'w'
#===========================

#==== Useful Characters ====
NEWLINE: str = '\n'
SPACE: str = ' '
#===========================

#==== Used IP Addresses ====
NEW_IP: str = '0.0.0.0'
#===========================