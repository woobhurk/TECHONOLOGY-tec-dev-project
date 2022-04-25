#!/usr/bin/env bash

# #################
# Customized Script
{
    echo -e "\n\n\n\n"
    echo "172.16.223.18 jeecg-boot-redis"
    echo "172.16.223.18 jeecg-boot-mysql"
    echo "172.16.223.18 jeecg-boot-rabbitmq"
    echo "172.16.223.18 jeecg-boot-nacos"
    echo "172.16.223.18 jeecg-boot-gateway"
    echo "172.16.223.18 jeecg-boot-system"
    echo "172.16.223.18 jeecg-boot-xxljob"
} >> /etc/hosts

# #############
# DO NOT MODIFY
# Output logs to specified file
java -jar "/project/app.jar" >> "$1"
