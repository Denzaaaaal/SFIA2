# Random Name Generator

## Table of Contents

## Project Brief

### Proposal
For my SFIA2 project, I decided to build a name generator that would be deployed continuously when changes are detected to the code.

## Trello Board
### Start Point

### End Point
* In order to make the application deployment process as seemless as possible, Jenkins has been setup to auto build the application when changes are detected in Github. 

 * Encountered an issue with dockerswarm which prevents changes from being implemented in the container  before deployment. This issue was overcome by using Github intergration with docker allowing new builds to occur when a change is detected within specified directories in my Github Repository.

 * Nginx container has been amended to redirect all connections to HTTPS. Due to not being able to acquire a signed certificate, the container will generate a new key everytime it is rebuilt and will use that key to authorise the connection. ~~The key was not uploaded to Github as this could cause a security risk and due to dockerhub building the container when changes are detected in Github, this specific repository has been made private to prevent exposure of the key generated when the container was built.~~

## Risk Assessment
|Risk|Impact|Probability|Consequence|Action|
|----|------|-----------|-----------|------|
|Becoming Sick (Flu, Cold, COVID-19, etc) |Major|51%-75%|Could lead to serious delays in the project and to the workers health|Wash hands regularly, keep 2 Meter distance, leave your house for only essentials, take appropriate medicine|
|Eye Strain|Minor|26%-50%|Increased eye strain causes stress on the body and can deteriorate vision|Ensure regular breaks are taken away from the computer|
|Private details leaked  |Major|26%-50%|Reputation damage|Ensure confidential repositories are made private and use of .gitignore or .dockerignore is used to prevent details being uploaded to version control system or container system. Encryption can be used to further secure the application|
|Service being attacked (DDOS)|Critical|76%-100%|Service going down, Reputation damage|Ensure only relevant ports are opened and containers are suffienctly replicated|
|Running out of free credit on GCP|Major|1%-25%|Would require either a new account to be created on GCP or pay for the service|Ensure that credit hungry services are running only at essential times and choose instance specifications that do not incur large costs|

## Project Archetecture

## Overall Archetecture

## Toolset
- Jenkins
- Ansible
- Nginx
- Docker
- Flask
- Python
## Retrospective
### What went well
* The application has been set up for continuous deployment.
* The application does not have unnecessary ports opened or IP addresses shown in the code
* 
### What did not go well
* Ansibles documentation acts more like a reference instead of a how-to guide
* Ansibles documentation does not mention some arguments they that it accepts
* Setting a repository in dockerhub to private prevents it from being built using docker swarm
### Future Improvements
* ~~Incoporate Dockerhub autobuild feature when changes in a Github directory are detected~~
* Incorporate HTTPS redirection and certificate verification to ensure entries made into the database are transmited through a secure connection
* Incoporate CSS into website template
* Incoporate testing container to test different functionality of the API
* ~~Incorporate Jenkins autobuild feature when new changes are pushed to Github~~
## Installation
### Pre-requisits 
* Account with Google Cloud Platform
* Knowledge of using Google Cloud Platform
* Account with Github
### Steps
1 - On GCP (Google Cloud platform), navigate into Compute Engine > VM instance and Create 3 VM instances all with "Ubuntu 18.04 LTS" and select your closest reigon and zone for all the instances. For the case of this example we will name those 3 instances the following names:
* jenkins-ansible
* master
* worker
Leave all the other options as there defaults accept the worker where you will need to tick the box "allow HTTP Traffic" in the firewall option. This will enable the server to be accessed via a web browser on port 80 and leave all the other options as default.

2 - On GCP, navigate to VPC Network > Firewall rules and create 2 firewall rules with the following names:
* jenkins
* Docker
For the Jenkins firewall, add IP address the IP address you are working from and in the protocols and ports section, select "Specified protocols and ports", tick the "TCP" iton and add port 8080 and click "Save".

For the Docker firewall, add IP address the IP address of the manager and worker and in the protocols and ports section, select "Specified protocols and ports", tick the "TCP" iton and add port 2377 and click "Save".

Go back in Compute Engine > VM instance and click edit the jenkins-ansible instance and add the jenkins rule to the firewall.

On the manager and worker instances, add docker rule to the firewall.

3 - On GCP, Connect to the Jenkins-ansible instance via SSH. This should open up a new SSH window. 

Type the following commands
```
sudo apt update -y
sudo apt install openjdk-8-jdk -y
```
The first command updates the system and the second command installs openJDK 8 which is a dependency for jenkins.

Once this is complete, we need to add the repository

Type in the following commands
```
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
```
The first command will pull the key from jenkin.io and add it to aptitude. This will return an 'OK' if it has been successfully added. The second command then adds the adds the repository to the system.

Now we want to install jenkins. Type the following commands
```
sudo apt update -y 
sudo apt install jenkins -y
```
Upon completion of these commands, we need to test if Jenkins has been installed and is successufully running. 
Type 

`systemctl status jenkins`

and if the service has started you should see something similar to what it says below
```
jenkins.service - LSB: Start Jenkins at boot time
   Loaded: loaded (/etc/init.d/jenkins; generated)
   Active: active (exited) since Mon 2018-07-09 17:22:08 UTC; 6min ago
     Docs: man:systemd-sysv-generator(8)
    Tasks: 0 (limit: 1153)
   CGroup: /system.slice/jenkins.service
```
4 - Next we need to edit the sudo configuration file to allow us to get the administrators password to unlock jenkins. In order to do this type in 

`sudo visudo`

This should launch the nano text editor. Add the following line in the file

`jenkins ALL=(ALL) NOPASSWD:ALL`

Once this is done, save the changes and type 

`sudo su jenkins`

This will change you to the Jenkins user. Next we need to get the password to unlock jenkins

`cat /var/lib/jenkins/secrets/initialAdminPassword`

Copy the output and go to the IP address of the jenkins-ansible instance at port 8080 in your web browsers URL. The address should look something like this 

`0.0.0.0:8080`

It will ask you to enter the adminstrator password into the box on the screen. Paste the output copied from your cat command and press "Continue"

5 - If the password is correct, Jenkins will then ask you to install plugins. Select "Install suggested plugins" and the program will get to work downloading the plugins selected. 

Once this is completed, Jenkins will prompt you to create the first admin user. Fill in the details as desired and select "Save and Continue".

Jenkins will now ask you about the instance configuration, which it will ask you for the prefered URL to access the website. This will default to the instances IP address at port 8080. Click "Save and Finish". 

If all has been set up correctly, you will see a page saying that Jenkins is ready. 

Click "Start using Jenkins"

6 - Next we need to add IP addresses to the hosts file. Open an SSH connection to your Jenkins-ansible instance and enter in the following command. 

`vi /etc/hosts`

In here you will see the IP address of the localhost and the domain which in this case localhost. We are going to add our IP addresses of the manager and worker which should result in the file looking like below. Fill out the 0.0.0.0 with the external IP addresses of each instance
```
127.0.0.1 localhost
0.0.0.0 manager-node
0.0.0.0 worker-node
```
Save the changes and exit the terminal session.

7 - We now need to setup Jenkins to build the project.

Click on "New Item" on the left hand menu which will present you with a new page. In the item name, enter in "SFIA2" as the item name and select "pipeline" as the build configuration. Then click "Ok".

Here we will be taken to a page which requires us to further configure our build configuration.  


## Author
Denzel Douglas