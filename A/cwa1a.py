# Filename: cwa1a.py
# Author: Leong Chei Chau
# Description: Program to check and validate staff details and input to STAFF.DAT

import os
import datetime

def CREATESTAFF():
    try:
        if os.path.exists("STAFF.DAT"):
            print("File already exists. It will be overwritten.")
            StaffFile = open("STAFF.DAT","w")

        Date = datetime.date.today()
        LastUpdateDate = Date.strftime("%d-%m-%Y")

        ValidRecordNumber = False
        while not ValidRecordNumber:
            NumberOfRecords = 

        else:
            StaffFile = open("STAFF.DAT","r+")

            Date = datetime.date.today()
            LastUpdateDate = Date.strftime("%d-%m-%Y")
            print(LastUpdateDate)

            StaffFile.readline()

            for Record in StaffFile.readlines():
                NumberOfRecords = NumberOfRecords + 1
        
    except IOError:
        print("File cannot be created.")

if __name__ == "__main__" :
    CREATESTAFF()
