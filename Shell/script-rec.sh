#!/bin/bash

FIFO_FILE=$(pwd)/script-rec.fifo
LOG_FILE=$(pwd)/script-rec.log

main() {
    echo "**** Start script recording, file is ${LOG_FILE}..."
    rm -rf ${FIFO_FILE}
    mkfifo ${FIFO_FILE}
    cat ${FIFO_FILE} | tee -a ${LOG_FILE} &
    exec 1>${FIFO_FILE}
    exec 2>&1
    bash --login -i
    echo "---- Script recording finished, file is ${LOG_FILE}."
}

main "$*"
