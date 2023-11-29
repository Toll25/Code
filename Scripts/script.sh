#!/bin/bash
#sudo ldapsearch -x -H ldap://ngfs.intra "(&(objectClass=Person)(ou="3BHITS"))" sn givenName | grep -e "sn: " -e "givenName: " | sed "s/givenName: //g" | sed "s/sn: //g"
numbers=sudo ldapsearch -x -H ldap://ngfs.intra "(&(objectClass=Person)(ou="3BHITS"))" dn | grep -e "dn: "| sed "s/givenName: //g" | sed "s/sn: //g"
SAVEIFS=$IFS   # Save current IFS (Internal Field Separator)
IFS=$'\n'      # Change IFS to newline char
numbers=($numbers) # split the `names` string into an array by the same name
IFS=$SAVEIFS   # Restore original IFS

for (( i=0; i<${#numbers[@]}; i++ ))
do
    echo "$i: ${numbers[$i]}"
done