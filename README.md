# NVO_OpenStack_Lab

### Objective 1: Openstack Overview - Dhaval

1.	Explain the following components of OpenStack -
    a.	Nova:
    Nova component is for provisioning compute instances and supporting the creation of virtual machines, bare metal servers, and limited support of containers. 
    
    b.	Swift:
    Swift is an object storage service that is similar to cloud storage like google drive or drop box. It is a standalone service for providing only object storage to end users     and not the setting up the infrastructure-as-a-service. 

    c.	Cinder:
    Cinder is a block storage service that is similar to an external HDD. It provides volumes to Nova virtual machines, bare metal hosts, containers, and more.

    d.	Neutron:
    Neutron is a networking component of OpenStack and it provides network connectivity as a service between interface devices managed by other OpenStack services like Nova.

    e.	Glance:
    Glance is an image service of OpenStack where users can register, retrieve, and discover the images that they want to use with their VMs or Containers.

    f.	Keystone:
    Keystone is an identity service of OpenStack and it provides API client authentication, service discovery, and distributed multi-tenant authorization. It supports various       authentication services like LDAP, OAuth, OpenID Connect, SAML, etc. 

    g.	Horizon:
    Horizon provides the dashboard or web-based UI for OpenStack services.

2.	What is the difference between Users and Roles?
    Users are member/part of one or more projects whereas roles defines which actions users can perform.

3.	What is a hypervisor and which hypervisors are supported in OpenStack?
    Hypervisor is a software that creates and runs virtual machines by separating a system’s operating system and resources from the hardware to allocate VMs.
    Following hypervisors are supported in OpenStack:
    •	KVM
    •	LXC
    •	QEMU
    •	VMware ESX/ESXi
    •	XenServer
    •	Hyper-V
    •	Ironic
    •	UML
    •	Virtuozzo

4.	Explain the meaning of ‘flavor’ in OpenStack.
    Flavor is a combination of compute, memory, and storage capacity of nova computing instances.

5.	Create a new network of 64 IP addresses in the Network tab and enable DHCP for 32 of the IPs using either the GUI or the CLI.

    ![image](https://user-images.githubusercontent.com/63819641/106371615-e01e0100-6323-11eb-94ad-6017c250ed5d.png)
    
    ![image](https://user-images.githubusercontent.com/63819641/106371631-f3c96780-6323-11eb-9f0b-333f2f2050f0.png)
 
6.	Create a router that connects this new network with the existing “public network” using either the GUI or the CLI.

    ![image](https://user-images.githubusercontent.com/63819641/106371635-fdeb6600-6323-11eb-9e45-b15d615b1d85.png)

    ![image](https://user-images.githubusercontent.com/63819641/106371639-05ab0a80-6324-11eb-94a4-ab432b8537e5.png)

    ![image](https://user-images.githubusercontent.com/63819641/106371645-122f6300-6324-11eb-8adb-812eb0e61acb.png)
 
7.	Start two instances with the Cirros image present that connects to the new network of 64 IPs using either the GUI or the CLI.
 
    ![image](https://user-images.githubusercontent.com/63819641/106371650-1a879e00-6324-11eb-8a3d-c097120fa551.png)

    ![image](https://user-images.githubusercontent.com/63819641/106371660-22dfd900-6324-11eb-870a-06253522ce66.png)
 
### Objective 2: Auto-scaling application using Python: Mukesh
  - The autoscale tool will first login into the servier via SSH, and monitor the CPU load at the interval of every 40 secs(evaluation_period). 
  - Whenever the current load at the server is more than the predefined threshold value, the autoscale tool will create a new replica of monitored server. 
  - Here we can take input form the user for the flavor,network_id and the source image too. For now the values are defined in the tool itself. 
  - The tool will also keep count of created autoscale servers. As soon the count is reached to a pre defined max_scaling_size, the tool will not create any new servers and will       just keep monitoing the orginal server load.
  - Here we have cirros image as the OS. Cirros image is a very basic linux OS, so any specific linux stress tool will not work. So for generating stress, i have used the           bash commands to start/stop the stress load on the server.
    
    #### Start stress: "for i in 1 2 3 4; do while : ; do : ; done & done"
    #### Stop stress:  "for i in 1 2 3 4; do kill %$i; done"
   
   ## Steps executed for this objective:
   
  - Start the tool via "python3 sdn_lab2.py" command.
  
  -	Before activity only one server can be seen in the dashboard.
    
    ![image](https://user-images.githubusercontent.com/71536049/106373808-8b39b500-633a-11eb-8792-c6d8c97e1b42.png)
  
  - Stress generated to the server:
    
    ![image](https://user-images.githubusercontent.com/71536049/106373817-a0aedf00-633a-11eb-8eb7-9bfd9a846d4e.png)
  
  - New 4 Autoscale servers created:
    
    ![image](https://user-images.githubusercontent.com/71536049/106373833-b7edcc80-633a-11eb-8103-8a27561591ed.png)
  
  -	Console output of the tool:
    
    ![image](https://user-images.githubusercontent.com/71536049/106373844-c89e4280-633a-11eb-8174-c96b06c155dc.png)
  
  - After activity, the process killed:
    
    ![image](https://user-images.githubusercontent.com/71536049/106373848-d784f500-633a-11eb-9a72-9ed95fe5defd.png)
    
    

Objective 3: Multi-tenants

•	In this objective, you are introduced to the function of basic tenant implementation and management with OpenStack.

•	The goal is to create two virtual networks and three VMs as is shown in Figure 1.

![image](https://user-images.githubusercontent.com/4688397/106393188-0179fe00-63b3-11eb-8862-9bd99e71a8a8.png)
 
Figure 1. Final goal of Objective 3
Section 1: Creating project, user, flavor and image

1.	Within OpenStack UI Identity tag, create a project called lab2. Then create a user called lab2_admin and attach it to the project lab2.
 
 
2.	Within OpenStack UI Admin tag, create a VM Flavor called ngn.tiny with the following setting:
vCPU 			= 1
RAM 			= 128MB
Root Disk 		= 1GB
Ephemeral Disk 	= 1GB
Swap Disk 		= 1GB
 
3.	Within OpenStack UI Admin tag, upload a VM image into OpenStack. You can use this URL: http://tinycorelinux.net/7.x/x86/release/Core-current.iso.
Remember to make it public.
 
4.	Before proceeding, logout and login with your newly created user lab2_admin.
 
Section 2: Setup Virtual Networks

1.	Login back into OpenStack UI, within the Project tag, create a new Network called VN-A with network address 192.168.100.0/24.
2.	Repeat the above steps to create a second network VN-B with network address 192.168.200.0/24.
 
Section 3: Launch VM instances


