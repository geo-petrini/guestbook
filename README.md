# Gustbook

A simple flask application developed to demonstrate how to use Docker as part of a small tutorial.

## Content

The tutorial covers the following topics:
1. How to prepare a web application for containerization using environment variables
2. How to create a docker image
3. How to deploy the image as container and set up port forwarding
4. How to test if the container is running (using docker commands)

From this point on, the tutorial uses the same application to integrate additional elements:
1. Interface with a DBMS (in this case MySQL) using docker compose
2. Define the correct environment variables
    - via command line
    - via portainer
3. Define conditions and healthcheck
4. Add data persistance
5. Verify if the stack is running correctly

Last part of the tutorial includes monitoring
1. Setup Grafana
2. Setup Prometeus
3. Integrate the application
4. Create a dashboard