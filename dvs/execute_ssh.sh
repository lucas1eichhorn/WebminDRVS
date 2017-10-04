#!/bin/bash
#Script que accede por ssh a un nodo remoto mediante sshpass y ejecuta un comando remoto pasado como parametro
#params: $1=nodo; $2=usuario; $3=password; $4=comando;
echo "sshpass -p $3 ssh $2@$1 $4" 
sshpass -p "$3" ssh $2@$1 $4 


