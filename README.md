# Assignment 2 - CS5287

# Milestone 1

For this milestone both of us downloaded Vagrant to our local machines. We then edited the Vagrantfile for configuration details. 

Install Vagrant from: https://www.vagrantup.com/

We download the clouds.yaml file from Chameleon Cloud and made sure this file was placed correctly in the new virtual machine. You can locate this file under KVM.Access.Download.

The command `vagrant up` creates a virtual machine in VirtualBox and then automatically installs Ansible and runs an Ansible playbook. 

A demo for this milestone can be found at: https://youtu.be/svjahpe6LWs

## Distribution of Work 

Parish edited the Vagrant files, and then we both met over Zoom to test and get the playbooks working. Alex then created documentation and a demo video. 

# Milestone 2 

With the command vagrant up a vagrant VM is created, and then a [master playbook](github.com/parishwolfe/5287-A2/blob/main/vagrant_ansible/playbook_create_and_provision.yml) is called that subsequently calls a number of other playbooks. I will details these playbooks below. The master playbook is called with vagrant provision. 

We created a playbook that spins out two Cloud virtual machines (VM2, VM3). This playbook can be found [here](github.com/parishwolfe/5287-A2/blob/main/vagrant_ansible/tasks/create_cc_cloud_vm.yml). We had to find a specific type of clouds.yaml file as the one we had used before was not in the correct format for use here.  

We then created a playbooks that configure these virtual machines. The playbook to configure both machines is [here](github.com/parishwolfe/5287-A2/blob/main/vagrant_ansible/tasks/playbook_setup_both_cloud_vms.yml), and the playbook for VM3 specific configuration is [here](github.com/parishwolfe/5287-A2/blob/main/vagrant_ansible/tasks/playbook_VM3.yml). 

## Configuration details:

VM2: 
* Kafka 
* Broker_id = 0
* Zookeeper
* Cloned github repo

VM3:
* Kafka
* Broker_id = 1
* Cloned github repo

To install Kafka we created playbooks that followed the instructions found at: https://www.digitalocean.com/community/tutorials/how-to-install-apache-kafka-on-ubuntu-20-04

To configure Kafka, we wrote zookeeper.service and kafka.service files that were copied over into the correct directories using a playbook. We then edited the kafka server.properties files on both VMs as needed using a playbook. 

Using playbooks we also made sure all the needed packages were installed on VM2 and VM3. Additionally, there is a playbook that ensures the correct Firewall rules are on each VM. 

## Demo: 

A demo can be found here. This shows VM2 and VM3 being created by vagrant up, and it shows the consumer and producer code working on the correct machines. 




