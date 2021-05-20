#bin/bash
#by: Cr1pto9

#colores
greenColour="\e[0;32m\033[1m"
eColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
bColour="\e[0;34m\033[1m"
yColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
gColour="\e[0;37m\033[1m"

trap ctrl_c INT
echo -e "${bColour}Ariendo script${eColour}${purpleColour}..${eColour}"
sleep 3
function ctrl_c(){
        echo -e "${gcolour}saliendo${ecolour}${bcolour}...${ecolour}"
}
#dependencias
tput civis
clear; dependencias=(python, python2, vim, micro)

echo -e "${yColour}[*]${eColour}${gColour} Comprobando programas necesarios...${eColour}"
 sleep 2

for program in "${dependencias[@]}"; do
         echo -ne "\n${yColour}[*]${eColour}${bColour} Paquetes${eColour}${purpleColour} $program${eColour}${bColour}...${eColour}"

        test -f /usr/bin/$program

        if [ "$(echo $?)" == "0" ]; then
                 echo -e " ${greenColour}(V)${eColour}"
         else
             echo -e " ${redColour}(X)${endColour}\n"
             echo -e "${yColour}[*]${eColour}${gColour} Instalando paquetes ${eColour}${bColour}$program${eColour}${yColour}...${eColour}"
              apt-get install $program -y > /dev/null 2>&1
              echo -e "${bColour}By${eColour}   ${yColour} Cr1pto9${eColour}"
            fi; sleep 1
            done
