import sys
sys.path.insert(1, '../deps/')
import IniFile

def Main(ini_path):
  ini = IniFile(ini_path)
  """
  TODO Parse inputs and call function to start subsystem.
  """

Main("../input/system-params.ini")
