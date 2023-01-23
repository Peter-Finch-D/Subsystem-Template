############ ini code ###############################################
# Based on https://stackoverflow.com/questions/8884188/how-to-read-and-write-ini-file-with-python3
import configparser
class IniFile(ConfigParser):
  pass
############ Script body ############################################
def Main(ini_path):
  ini = IniFile(ini_path)
  """
  TODO Parse inputs and call function to start subsystem.
  """

Main("../input/system-params.ini")
