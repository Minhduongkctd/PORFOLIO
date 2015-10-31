from datetime import datetime
from datetime import timedelta


hqTime = datetime.now()-timedelta(hours=1)
nycTime = hqTime.now() + timedelta(hours=3)
londonTime=hqTime.now() + timedelta(hours=7)
germanyTime=hqTime.now() + timedelta(hours=8)
hawaiiTime=hqTime.now()- timedelta(hours=3)

def nycHours():
  if nycTime.hour < 9:
      print "Branch1: NYC Office is now closed"
  elif nycTime.hour > 21:
      print "Branch1: NYC Office is now closed"
  else:
      print "Branch1: NYC Office is open"
        
def londonHours():
  if londonTime.hour < 9:
      print "Branch2: London Office is now closed"
  elif londonTime.hour > 21:
      print "Branch2: London Office is now closed"   
  else:
      print "Branch2: London Office is open"
      
def germanyHours():
  if germanyTime.hour < 9:
      print "Branch3: Germany Office is now closed"
  elif germanyTime.hour > 21:
      print "Branch3: Germany Office is now closed"   
  else:
      print "Branch3: Germany Office is open"

def hawaiiHours():
  if hawaiiTime.hour < 9:
      print "Branch4: Hawaii Office is now closed"
  elif hawaiiTime.hour > 21:
      print "Branch4: Hawaii Office is now closed"   
  else:
      print "Branch4: Hawaii Office is open"
      
nycHours()
londonHours()
germanyHours()
hawaiiHours()
