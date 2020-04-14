# Random Name Generator

## Table of Contents

## Project Brief

### Proposal
For my SFIA2 project, I decided to build a name generator that would be deployed continuously when changes are detected to the code.

## Trello Board

Trello was the chosen tool used to manage the project and is a software implementation of the kanban board. This particular view helped me to adhere to the agile methodology. The work was only considered done when the feature was tested and implimented into the application.
### MoSCoW Analysis

#### Must have
* 4 Services each which are containerised using Docker
* Service 1 pulls information from Service 4
* Service 4 pulls information from Service 2 and 3 and joins the values
* Service 2 generates a random first name
* Service 3 generates a random last name

#### Should have
* Nginx as a reverse proxy 
* Ansible used to configure the instances
* docker-compose file for creating all the containers and the container network
* Jenkins used to trigger the build
* Testing the URL and the database to see if data can be inserted into the database

#### Could have
* Ensuring the application is deployed using 3 instances
* Full CRUD functionality of service 1
* HTTPS Connection to service 1 using Nginx
* All ports and IP addresses not exposed in the code
* Application is only accessable through port 80 unless HTTPS connection is implemented and therefore 443
* Ansible deploys the application in swarm mode
#### Won't have

### Start Point
![start_point](https://github.com/Denzaaaaal/SFIA2/blob/developer/images/start_point.JPG)
### End Point
![end_point](https://github.com/Denzaaaaal/SFIA2/blob/developer/images/end_point.JPG)
* In order to make the application deployment process as seemless as possible, Jenkins has been setup to auto build the application when changes are detected in Github. 

 * Encountered an issue with dockerswarm which prevents changes from being implemented in the container  before deployment. This issue was overcome by using Github intergration with docker allowing new builds to occur when a change is detected within specified directories in my Github Repository.

 * Nginx container has been amended to redirect all connections to HTTPS. Due to not being able to acquire a signed certificate, the container will generate a new key everytime it is rebuilt and will use that key to authorise the connection. ~~The key was not uploaded to Github as this could cause a security risk and due to dockerhub building the container when changes are detected in Github, this specific repository has been made private to prevent exposure of the key generated when the container was built.~~

## Risk Assessment
### Start Point
Below is a list of risks I predicted could impact the project.

|Risk|Impact|Probability|Consequence|Action|
|----|------|-----------|-----------|------|
|Becoming Sick (Flu, Cold, COVID-19, etc)|Major|51%-75%|Could lead to serious delays in the project and to the workers health|Wash hands regularly, keep 2 Meter distance, leave your house for only essentials, take appropriate medicine|
|Eye Strain|Minor|26%-50%|Increased eye strain causes stress on the body and can deteriorate vision|Ensure regular breaks are taken away from the computer|
|Private details leaked|Major|26%-50%|Reputation damage|Ensure confidential repositories are made private and use of .gitignore or .dockerignore is used to prevent details being uploaded to version control system or container system. Encryption can be used to further secure the application|
|Service being attacked (DDOS)|Critical|76%-100%|Service going down, Reputation damage|Ensure only relevant ports are opened and containers are suffienctly replicated|
|Running out of free credit on GCP|Major|1%-25%|Would require either a new account to be created on GCP or pay for the service|Ensure that credit hungry services are running only at essential times and choose instance specifications that do not incur large costs|

### End Point
Below is a list of risks in addition to the ones above that impacted the project.

|Risk|Impact|Probability|Consequence|Action|
|----|------|-----------|-----------|------|
|GCP going down|1%-25%|Major|Due to the lockdown, increased usage of cloud services are putting a strain on GCP servers causing them to crash|Explore other hosting solutions and consider building your application locally using several virtual machines to simulate the network|
|Spending an extended time understanding how ansible works|Major|26%-50%|Ansibles offical documentation was not updated and which made it difficult to find ways to do certain tasks on ansible|Pieced together different sources of documentation on the internet, dissern what works and implement it into my work|

## Project Archetecture
### Initial Archetecture
![inital_archetecture](https://github.com/Denzaaaaal/SFIA2/blob/developer/images/inital_archetecture.JPG)
### Final Archetecture
![final_archetecture](https://github.com/Denzaaaaal/SFIA2/blob/developer/images/final_archetecture.JPG)

### Toolset
- Jenkins
- Ansible
- Nginx
- Docker
- Flask
- Python

### Design Decisions
- Jenkins has been set up with web hooks to autobuild the application as soon as it has been deployed. Jenkins is also works as the trigger to tell ansible to configure, test and deploy the application. 

- Ansible was selected to configure the servers for the application initally but then during the process of going through the documentation, I discovered that it would be easier to use ansible to deploy the application instead of Jenkins due to it's simpler implimentation of copying the required files to the manager and then telling it to execute the command that uses those files. Ansible has also been configured to take down the service and rebuild the service on every new build preventing the user from having to leave the node manually.

- Docker was the container service used for this project and this specific deployment ultilises the docker-compose addition to docker. Within the project a docker-compose file has been created to pull the latest images from dockerhub which has been set up with a webhooks to specfic directories in my github to allow the build of the latest images from a specific directory.

- Nginx was used as a web proxy to prevent any unnessisary ports from being exposed and due to it being a web server as well, it also works as a barrier to prevent people from accessing the service directly reducing the likelyhood of a DDOS attack taking down the service.

- The container for the services all are built on a container called Python Slim. This uses Debian as the container operating system instead of alpine. I decided to use this instead as Debian is one of the distributions in linux that is known for it's stability. This will ensures that any issues that occurs within the container will be most likely due to my application being falty.

## Retrospective
### What went well
* The application has been set up for continuous intergration and continuous deployment.
* The application does not have unnecessary ports opened or IP addresses exposed in the code
* 
### What did not go well
* Ansibles documentation acts more like a reference instead of a how-to guide
* Ansibles documentation does not mention some arguments they that it accepts
* Setting a repository in dockerhub to private prevents it from being built using docker swarm
* If the any of the services are edited, dockerhub bulds the images at a slower rate than jenkins does which leads to the last dockerhub container being pulled.
### Future Improvements
* ~~Incoporate Dockerhub autobuild feature when changes in a Github directory are detected~~
* Incorporate HTTPS redirection and certificate verification to ensure entries made into the database are transmited through a secure connection
* Incoporate CSS into website template
* Incoporate testing container to test different functionality of the API
* ~~Incorporate Jenkins autobuild feature when new changes are pushed to Github~~

Below I have outlined the next sprint using a Kanban Board incorporating these features. Some of these features got implemented earlier than expected due to increasing build efficiency.

![additional_changes](https://github.com/Denzaaaaal/SFIA2/blob/developer/images/additional_changes.JPG)

## Installation
### Pre-requisites 
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

For the Jenkins firewall, add IP address the IP address you are working from and in the protocols and ports section, select "Specified protocols and ports", tick the "TCP" icon and add port 8080 and click "Save".

For the Docker firewall, add IP address the IP address of the manager and worker and in the protocols and ports section, select "Specified protocols and ports", tick the "TCP" icon and add port 2377 and click "Save".

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

It will ask you to enter the administrator password into the box on the screen. Paste the output copied from your cat command and press "Continue"

5 - If the password is correct, Jenkins will then ask you to install plugins. Select "Install suggested plugins" and the program will get to work downloading the plugins selected. 

Once this is completed, Jenkins will prompt you to create the first admin user. Fill in the details as desired and select "Save and Continue".

Jenkins will now ask you about the instance configuration, which it will ask you for the prefered URL to access the website. This will default to the instances IP address at port 8080. Click "Save and Finish". 

If all has been set up correctly, you will see a page saying that Jenkins is ready. 

Click "Start using Jenkins"

6 - Next we need to add IP addresses to the hosts file. Open an SSH connection to your Jenkins-ansible instance and enter in the following command. 

`vi /etc/hosts`

In here you will see the IP address of the localhost and the domain which in this case localhost. We are going to add our IP addresses of the manager and worker which should result in the file looking like below.Replace 0.0.0.0 with the external IP addresses of each instance
```
127.0.0.1 localhost
0.0.0.0 manager-node
0.0.0.0 worker-node
```
Save the changes

8 - Setting up environment variables

Next we need to set up an environment variables files which ansible will use to send the details to other nodes into the database. 

Enter the following command 

`vi ~/.environment_variables.env`

This will create a file in the jenkins home directory which will contain the details of your server. Add the code below to the file amending the variables to suit your SQL database.

```
MYSQL_HOST=0.0.0.0
MYSQL_USER=root
MYSQL_PASSWORD=changeme
MYSQL_DB=sfia2-db
```

Save the changes and exit the terminal session.

9 - We now need to setup Jenkins to build the project.

Click on "New Item" on the left hand menu which will present you with a new page. In the item name, enter in "SFIA2" as the item name and select "pipeline" as the build configuration. Then click "Ok".

Here we will be taken to a page which requires us to further configure our build configuration. 

Scroll down untill you see the 'Github project' under 'General' tab and enter in this Github Repository which is below

`https://github.com/Denzaaaaal/SFIA2.git`

Next click on the 'Pipeline' tab and change the definition to 'Pipeline script from SCM'. An option named 'SCM' will appear, select 'Git'.

Where it mentions the 'Repository URL', enter the same Git Repo below.

`https://github.com/Denzaaaaal/SFIA2.git`

You will now need to add your Github account to authorise the build. Click on the 'Add' button and a dropdown menu will appear. Click the option 'Jenkins' and this will pop up a new window. Add your Github details of your username and password in the corresponding boxes and click 'Add'.

Leave the branch as '*/master' and click 'Save'. This will take you back to the 'SFIA2 pipeline menu'.

From here, select 'Build Now'. This will pull the service from the github master branch and build the application. 

## Author
Denzel Douglas