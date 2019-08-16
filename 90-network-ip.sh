#!/bin/bash
 
IF=$1
STATUS=$2
 
if [ "$IF" == "interfacename" ]
#Replace interface name with your actual ethernet/wifi interface name
then
    case "$2" in
        up)
        cd /home/user/Documents/dir1 && python3 pymail.py
        ;;
        *)
        ;;
    esac
fi
# You can denote either python or python3 based on the version you are using
