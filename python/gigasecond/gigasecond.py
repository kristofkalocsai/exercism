# 
#           _                                            __
#    ____ _(_)___ _____ _________  _________  ____  ____/ /
#   / __ `/ / __ `/ __ `/ ___/ _ \/ ___/ __ \/ __ \/ __  /
#  / /_/ / / /_/ / /_/ (__  )  __/ /__/ /_/ / / / / /_/ /
#  \__, /_/\__, /\__,_/____/\___/\___/\____/_/ /_/\__,_/
# /____/  /____/
#
from datetime import date,timedelta

def add_gigasecond(birthdate):
    gigasec = timedelta( days = 11574 , hours = 1 , minutes = 46 , seconds = 40 )
    gsdate = birthdate + gigasec
    return gsdate
