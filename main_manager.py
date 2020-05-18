from pwd import PASSWORD
import os


class SlaveDriver:
    def __init__(self):
        self.name = 'pi'
        self.ip = '10.0.0.170'
        self.password = PASSWORD

    def ssh_in(self):
        os.system(f'ssh {self.name}@{self.ip}')


s = SlaveDriver()
