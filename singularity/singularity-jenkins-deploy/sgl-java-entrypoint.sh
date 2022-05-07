#!/usr/bin/env bash

# #################
# Customized Script
if [[ -z "$(grep "<CUSTOM>\$" "/etc/hosts")" ]]; then
    {
        echo -e "\n\n\n\n"
        echo "# ##################"
        echo "# App Hosts <CUSTOM>"
        echo "172.16.223.18 jeecg-boot-redis"
        echo "172.16.223.18 jeecg-boot-mysql"
        echo "172.16.223.18 jeecg-boot-rabbitmq"
        echo "172.16.223.18 jeecg-boot-nacos"
        echo "172.16.223.18 jeecg-boot-gateway"
        echo "172.16.223.18 jeecg-boot-system"
        echo "172.16.223.18 jeecg-boot-xxljob"
    } >> /etc/hosts
fi

# #############
# DO NOT MODIFY
# Java options
PROJECT_OPTION="$1"
# Output logs to specified file
PROJECT_LOG_FILE="$2"
{
    echo ================================
    echo "Project option: $PROJECT_OPTION"
    echo "Project log file: $PROJECT_LOG_FILE"
    ## Using `xargs` to pass params to `java` to prevent exposing secrets
    #xargs -I JOPT java JOPT -jar "/project/app.jar" < <(echo "$PROJECT_OPTION")
    java $PROJECT_OPTION -jar "/project/app.jar"
} &>> "$PROJECT_LOG_FILE"
