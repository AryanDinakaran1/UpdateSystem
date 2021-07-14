"""
* This program does the job of updating your packages in linux without using the apt update and apt upgrade command.
* It is just once that you write update and done!
*
* Author : Aryan Dinakaran
*
* Date : 13th July, 2021.
"""

#Imports
import os

#Check For Update
def CheckUpdates():
    #Check for update using sudo apt update
    print("Checking for updates")
    os.system("sudo apt update")

#Upgrade system if user wants
def Upgrade():
    #Ask user
    yesOrNo1 = input("Would you like to upgrade?\n>> ")

    #Check if user wants to upgrade
    if yesOrNo1 == "y" or yesOrNo1 == "yes":
        #If yes sudo apt upgrade -y
        print("Upgrading system")
        os.system("sudo apt upgrade -y")
        Reboot()
    else:
        #else don't do anything
        print("Not upgrading linux")

#Ask user if he wants to reboot the system
def Reboot():
    #Ask User
    yesOrNo2 = input("Would you like to reboot your system\n>> ")
    
    if yesOrNo2 == "y" or yesOrNo2 == "yes":
        #If yes use sudo reboot
        print("Rebooting System")
        os.system("sudo reboot")
    else:
        #else don't reboot
        print("Not rebooting")

#Call the functions
CheckUpdates()  #CheckForUpdates
Upgrade()   #Upgrade

