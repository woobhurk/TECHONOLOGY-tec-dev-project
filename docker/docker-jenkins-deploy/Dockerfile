FROM openjdk:8
MAINTAINER jeecg-boot

# App file, argument is passed by command line
ARG APP_FILE
# App project directory
ARG APP_DIR="/data/project"
ARG TIMEZONE="Asia/Shanghai"

# Mount container's /tmp to host's tmeporary directory
VOLUME /tmp

# Initialize container
RUN ln -sf "/usr/share/zoneinfo/$TIMEZONE" "/etc/localtime"; \
    echo "$TIMEZONE" > "/etc/timezone"; \
    mkdir -p "$APP_DIR/"

# Change working directory in container
WORKDIR "$APP_DIR/"

# Copy all files in context directory to container's working directory ($APP_FILE/)
COPY ./* ./

RUN mv "./$APP_FILE" "./app.jar"

#ENTRYPOINT ["java", "-jar", "./app.jar"]
ENTRYPOINT ["/bin/bash", "./docker-project-entrypoint.sh"]
