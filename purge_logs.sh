#!/usr/bin/env bash

RED='\e[31m'
GREEN='\e[32m'
YELLOW='\033[33m'
NC='\e[0m'
echo ""
printf "${RED}Are you sure you want to purge the logs?${NC}\n"
echo ""
echo "We are currently in the directory:"
printf "========${YELLOW}\n"
pwd
printf "${NC}========\n"
echo ""
echo "Pls enter y/n"
read choice

if [[ "$choice" == "y" || "$choice" == "Y" ]]
then
    echo ""
    printf "${RED}Purging Logs [\]\n${NC}"
    echo ""
    rm -rf ./logs
    mkdir ./logs
    echo "i generated this as a placeholder to prevent empty folder messing with docker\n ik sounds weird but it is what it is" > ./logs/placeholder.txt
    printf "${GREEN}Purged Successfully [!]\n"
    printf "Exiting...${NC}\n"
else
    printf "${GREEN}Not Purging the logs\n"
    printf "Exiting...\n${NC}"
fi

# rm -rf ./logs