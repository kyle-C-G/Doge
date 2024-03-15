#!/bin/bash

error () {
    RED=$(tput setaf 1)
    RESET=$(tput sgr0)
    >&2 echo "${RED}ERROR: $1 ${RESET}" 
}

check_python () {
    which python3 >/dev/null
    if [[ ! $? -eq 0 ]]; then
        error "Python3 is not installed"
        exit 1
    fi
}

create_venv () {
    if [[ ! -d "venv" ]]; then
        python3 -m venv venv
        if [[ ! $? -eq 0 ]]; then
            error "Failed to create venv"
            exit 1
        else
            echo "Doge: Created venv"
        fi
    fi
}

install_requirements () {
    create_venv
    if [[ ! -f requirements.txt ]]; then
        error "requirements.txt not found"
        exit 1
    fi
    source venv/bin/activate
    pip install -r requirements.txt >/dev/null
    if [[ ! $? -eq 0 ]]; then
        error "Failed to intall requirements"
        exit 1
    else
        echo "Doge: Installed requirements"
    fi
}

create_env () {
    if [[ ! -f .env ]]; then
        touch .env
        echo "DISCORD_TOKEN=" >> .env
        echo "Doge: Created .env"
    fi
}

main () {
    check_python
    install_requirements
    create_env
}

main