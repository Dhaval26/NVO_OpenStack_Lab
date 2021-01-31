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
 
6.	Create a router that connects this new network with the existing “public network” using either the GUI or the CLI.
 
7.	Start two instances with the Cirros image present that connects to the new network of 64 IPs using either the GUI or the CLI.
 

 
### Objective 2: Mukesh
  - The autoscale tool will first login into the servier via SSH, and monitor the CPU load at the interval of every 40 secs(evaluation_period). 
  - Whenever the current load at the server is more than the predefined threshold value, the autoscale tool will create a new replica of monitored server. 
  - Here we can take input form the user for the flavor,network_id and the source image too. For now the values are defined in the tool itself. 
  - The tool will also keep count of created autoscale servers. As soon the count is reached to a pre defined max_scaling_size, the tool will not create any new servers and will       just keep monitoing the orginal server load.
  - Here we have cirros image as the OS. So any specific linux stress tool will not work as cirros image is avery basic linux os. So for generating stress, i have used the    
    bash commands to start/stop the stress load on the server.
    
  ### Start stress: "for i in 1 2 3 4; do while : ; do : ; done & done"
  ### Stop stress:  "for i in 1 2 3 4; do kill %$i; done "
  
  -	Before activity only one server in the dashboard.
    https://github.com/mukesh0733/images/commit/a599a29dce409defd3f0a05759477f29955bd463#commitcomment-46538272
  
  - Stress generated to the server:
  https://github.com/mukesh0733/images/commit/a599a29dce409defd3f0a05759477f29955bd463#commitcomment-46538288
  
  - New 4 Autoscale servers created:
  https://github.com/mukesh0733/images/commit/a599a29dce409defd3f0a05759477f29955bd463#commitcomment-46538305
  
  -	Console output of the tool:
  https://github.com/mukesh0733/images/commit/a599a29dce409defd3f0a05759477f29955bd463#commitcomment-46538312
  
  - After activity, the process killed:
 https://github.com/mukesh0733/images/commit/a599a29dce409defd3f0a05759477f29955bd463#commitcomment-46538298
