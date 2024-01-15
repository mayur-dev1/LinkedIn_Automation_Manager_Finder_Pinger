from utils.Functions import *
from utils.lib_list import *

LoginToLinkedIN(driver)
managers= SearchManagers(driver)
print(managers)
SendMessageToManager(driver, managers)