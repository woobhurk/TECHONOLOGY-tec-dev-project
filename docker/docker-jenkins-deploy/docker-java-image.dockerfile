FROM openjdk:8
MAINTAINER tyfanchz

# Project file, argument is passed by command line
ARG PROJECT_FILE
# Project directory
ARG PROJECT_DIR="/project"
ARG TIMEZONE="Asia/Shanghai"

# Mount container's /tmp to host's tmeporary directory
VOLUME /tmp

# Initialize container
RUN ln -sf "/usr/share/zoneinfo/$TIMEZONE" "/etc/localtime"; \
    echo "$TIMEZONE" > "/etc/timezone"; \
    mkdir -p "$PROJECT_DIR/"

# Change working directory in container
WORKDIR "$PROJECT_DIR/"

# Copy all files in context directory to container's working directory ($PROJECT_FILE/)
COPY ./* ./

RUN mv "./$PROJECT_FILE" "./app.jar"

#ENTRYPOINT ["java", "-jar", "./app.jar"]
ENTRYPOINT ["/bin/bash", "./docker-project-entrypoint.sh"]
