#!/bin/bash

docker rmi $(docker images -q --filter "dangling=true")

docker volume rm $(docker volume ls -qf dangling=true)