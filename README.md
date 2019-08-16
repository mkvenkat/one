# Sendmail

A simple script to trigger email with IP address whenever any user login to laptop/desktop.

## Only for Linux based systems

1. Place the sendmail.py file in some folder(eg., /home/user/Documents) in the system.
2. Make sure to set permission for the sendmail.py to allow executing as program.
2. Place the 90-network-ip.sh file in the directory /etc/NetworkManager/dispatcher.d.
3. Make sure to denote correct path of sendmail.py file inside 90-network-ip.sh, so that bash script executes    correctly.

Once done, whenever any user login to the system and connects to internet, email will be triggered with the external IP details.

