# Random Name Generator

## Table of Contents

## Project Brief

### Proposal

## Trello Board

### Start Point

### End Point
 * Encountered an issue with dockerswarm which prevents changes from being implemented in the container  before deployment. This issue was overcome by using GitHub intergration with docker allowing new builds to occur when a change is detected within specified directories in my GitHub Repository.

 * Nginx container has been amended to redirect all connections to HTTPS. Due to not being able to acquire a signed certificate, the container will generate a new key everytime it is rebuilt and will use that key to authorise the connectixon. The key was not uploaded to GitHub as this could cause a security risk and due to dockerhub building the container when changes are detected in Github, this specific repository has been made private to prevent exposure of the key generated when the container was built.

## Risk Assessment
|Risk|Impact|Probability|Consequence|Action|
|----|------|-----------|-----------|------|
|Becoming Sick (Flu, Cold, COVID-19) |Major|51%-75%|Could lead to serious delays in the project and to the workers health|Wash hands regularly, Keep 2 Meter distance, leave your house for only essentials|
|Eye Strain|Minor|26%-50%|Increased eye strain causes stress on the body and can deteriorate vision|Ensure regular breaks are taken away from the computer|
|Private details leaked  |Major|26%-50%|Reputation damage|Ensure confidential repositories are made private and use of .gitignore or .dockerignore is used to prevent details being uploaded to version control system or container system. Encryption can be used to further secure the application|
|Service being attacked (DDOS)|Critical|76%-100%|Service going down, Reputation damage|Ensure only relevant ports are opened and containers are suffienctly replicated|
|Running out of free credit on GCP|Major|1%-25%|Would require either a new account to be created on GCP or pay for the service|Ensure that credit hungry services are running only at essential times and choose instance specifications that do not incur large costs|

## Project Archetecture
## Entity Relationship Diagram

## Overall Archetecture

## Toolset

## Bug Fix

## Improvements

### Author
Denzel Douglas