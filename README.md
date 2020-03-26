# python-automation

To run this solution you need to have Docker. Extract the zip file to a folder in your user’s directory 
(or anywhere that docker can access and share file volumes). 

A small tweak is needed to the docker compose file, then the docker image can be built, and docker-compose up will run the solution. 

Report files will be accessible on local machine. 

The docker-compose file need a tweak on the volumes section to to run locally – the paths to the left hand side of the colon ( : ) 
are hardcoded absolute paths to the local project source code locations.

e.g. /mnt/c/users/USERNAME/PROJECT 
e.g c:\users\USERNAME\PROJECT

On windows an environment variable of COMPOSE_CONVERT_WINDOWS_PATHS = 1 is required

After updating the docker-compose.yml, the docker image can be built. 

    docker build -t ppodgorsek/robot-framework -f Dockerfile .
    
This build should complete all steps without error. It may take a minute or two. 

You can check that this docker image after it has built by running

    docker images | grep "robot-framework"

While inside the project folder, run docker compose up as per the command below. 
This will bring up the docker container, mount the folders on local filesystem so that they can be executed by the container. 
The test results will show in the console window, and will also be saved as report files and available on your local machine. 

    docker-compose -f docker-compose.yml up
    
After tests exit, it is advised to spin the docker container down using compose down

    docker-compose -f docker-compose.yml down
        
        
    
    
