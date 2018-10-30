#!/bin/sh

while true; do

       read -p "Continue (y/n)?" choice
       case "$choice" in
         y|Y ) echo "yes";break; ;;
         n|N ) echo "Exiting";
       echo "Exiting";
                                       exit 1; break; ;;
         * ) echo "invalid";;
       esac
done
