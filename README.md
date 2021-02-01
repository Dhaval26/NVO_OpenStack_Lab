# NVO_OpenStack_Lab_2

### Objective 1: Openstack Overview (Dhaval)

1.	Explain the following components of OpenStack:

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
 
### Objective 2: Auto-scaling application using Python (Mukesh)
  -	To access nova client via CLI/python3, first need to export some specific items. It can be done via “source openrc” and then “export | grep OS_” commands.
  -	The autoscale tool will first login into the server via SSH and monitor the CPU load at the interval of every 40 secs (evaluation period).
  -	Whenever the current load at the server is more than the predefined threshold value, the auto scale tool will create a new replica of monitored server.
  -	Here we can take input form the user for the flavor, network_id and the source image too. For now, the values are defined in the tool itself.
  -	The tool will also keep count of created autoscale servers. As soon the count is reached to a predefined max_scaling_size, the tool will not create any new servers and will just keep monitoring the original server load.
  -	Here we have Cirros image as the OS. Cirros image is a very basic linux OS, so any specific linux stress tool will not work. So, for generating stress, I have used the bash commands to start/stop the stress load on the server.
    
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
    
    
    

### Objective 3: Multi-tenants (Swati)

•	In this objective, you are introduced to the function of basic tenant implementation and management with OpenStack.

•	The goal is to create two virtual networks and three VMs as is shown in Figure 1.

![image](https://user-images.githubusercontent.com/4688397/106393188-0179fe00-63b3-11eb-8862-9bd99e71a8a8.png)
 
Figure 1. Final goal of Objective 3

#### Section 1: Creating project, user, flavor and image

1.	Within OpenStack UI Identity tag, create a project called lab2. Then create a user called lab2_admin and attach it to the project lab2.

![image](https://user-images.githubusercontent.com/4688397/106393236-35552380-63b3-11eb-9e7a-706d994fe991.png)

![image](https://user-images.githubusercontent.com/4688397/106393242-3d14c800-63b3-11eb-9265-742190184e0d.png)

2.	Within OpenStack UI Admin tag, create a VM Flavor called ngn.tiny with the following setting:
vCPU 			= 1
RAM 			= 128MB
Root Disk 		= 1GB
Ephemeral Disk 	= 1GB
Swap Disk 		= 1GB

![image](https://user-images.githubusercontent.com/4688397/106393252-4bfb7a80-63b3-11eb-9dc0-8ccc61070918.png)

3.	Within OpenStack UI Admin tag, upload a VM image into OpenStack. You can use this URL: http://tinycorelinux.net/7.x/x86/release/Core-current.iso.
Remember to make it public.

![image](https://user-images.githubusercontent.com/4688397/106393260-59b10000-63b3-11eb-8924-7a4e54c795d3.png)

4.	Before proceeding, logout and login with your newly created user lab2_admin.

![image](https://user-images.githubusercontent.com/4688397/106393270-646b9500-63b3-11eb-86a8-0f6cac33a6ec.png)


#### Section 2: Setup Virtual Networks

1.	Login back into OpenStack UI, within the Project tag, create a new Network called VN-A with network address 192.168.100.0/24.
2.	Repeat the above steps to create a second network VN-B with network address 192.168.200.0/24.

![image](https://user-images.githubusercontent.com/4688397/106393361-e52a9100-63b3-11eb-9109-d5c0ad49eb99.png)


#### Section 3: Launch VM instances

Launch the following VMs using the flavor and image created in Section 1.
1.	Launch VN-A_VM-1 and VN-A_VM-2 into virtual network VN-A.
2.	Launch VN-B_VM-1 into virtual network VN-B.

![image](https://user-images.githubusercontent.com/4688397/106393385-04292300-63b4-11eb-963f-56e7abd741dc.png)

![image](https://user-images.githubusercontent.com/4688397/106393392-11461200-63b4-11eb-9f6a-15f6cf39e2a6.png)


#### Section 4: Ping testing

1.	Use the console within OpenStack UI to test if VMs in VN-A can ping each other, while the VM in VN-B cannot reach VMs in VN-A.

![image](https://user-images.githubusercontent.com/4688397/106393401-21f68800-63b4-11eb-8016-b8daff44bc95.png)


2.	Assign floating IP’s to the VM’s both in VN-A and VN-B, and test connectivity to the Internet.
Internet connectivity does not require associating floating IPs to the VMs. It just requires a router enabled with SNAT having two interfaces connected to the two subnets. Inter-VN communication requires floating IPs to be configured for the two subnets.

![image](https://user-images.githubusercontent.com/4688397/106393422-42bedd80-63b4-11eb-91ec-c83da1f3bfb8.png)

![image](https://user-images.githubusercontent.com/4688397/106393430-481c2800-63b4-11eb-88c5-2bb13026a1a3.png)

![image](https://user-images.githubusercontent.com/4688397/106393431-4bafaf00-63b4-11eb-81df-7590b83516f6.png)

![image](https://user-images.githubusercontent.com/4688397/106393432-4f433600-63b4-11eb-8103-921e019de40d.png)

![image](https://user-images.githubusercontent.com/4688397/106393435-523e2680-63b4-11eb-87a7-20705ef15411.png)

![image](https://user-images.githubusercontent.com/4688397/106393437-55d1ad80-63b4-11eb-8988-a351863d7c50.png)


Floating IPs:


![image](https://user-images.githubusercontent.com/4688397/106393448-641fc980-63b4-11eb-9f3b-01902511b0d5.png)

![image](https://user-images.githubusercontent.com/4688397/106393452-67b35080-63b4-11eb-895b-6838166703f8.png)

![image](https://user-images.githubusercontent.com/4688397/106393455-6b46d780-63b4-11eb-865d-77114600e00e.png)

![image](https://user-images.githubusercontent.com/4688397/106393459-6e41c800-63b4-11eb-9c0a-4cc4ed09e188.png)


### Objective 4: Network policies in OpenStack (Section 1/2: Roni; Section 3: Nikhil)


#### Section 1: VM and Virtual Network Setup

The network is setup as per below figure:

![image](https://user-images.githubusercontent.com/8337251/106398020-bb7e6380-63cd-11eb-9e1b-242b9a1db7c1.png)

Network setup in Openstack topology:

![image](https://user-images.githubusercontent.com/8337251/106398070-17e18300-63ce-11eb-969d-8cb833d13053.png)

![image](https://user-images.githubusercontent.com/8337251/106398131-5119f300-63ce-11eb-81be-0f8cb1652e42.png)


#### Section 2: Achieve Inter-VN Communication

1. The Router (R1) has 3 interfaces:
    i. Connected to VN-A: IP Address --> 192.168.100.100
    ii. Connected to VN-B: IP Address --> 192.168.200.200
    iii. External Gateway: IP Address --> 172.24.4.224
    
2. Added default gateway 192.168.100.100 to both the VN-A VM's:

![image](https://user-images.githubusercontent.com/8337251/106399511-47948900-63d6-11eb-8d3a-0bb33c3f2071.png)

3. Added default gateway 192.168.200.200 to the VM in VN-B:

![image](https://user-images.githubusercontent.com/8337251/106399562-97735000-63d6-11eb-992f-09c1d44b8a0c.png)

4. The VM's can now ping between networks VN-A and VN-B:

![image](https://user-images.githubusercontent.com/8337251/106399602-eae59e00-63d6-11eb-8b68-6e3502dd7889.png)

5. Ping working from VN-B_VM-1 to VN-A_VM-1 and VN-A_VM-2:

![image](https://user-images.githubusercontent.com/8337251/106399736-b3c3bc80-63d7-11eb-9c48-b632932eb375.png)

6. Ping working from VN-A_VM-1 to VN-B_VM-1:

![image](https://user-images.githubusercontent.com/8337251/106399883-83c8e900-63d8-11eb-8ce9-6dea8bcfbd7f.png)

7. Ping working from VN-A_VM-2 to VN-B_VM-1:

![image](https://user-images.githubusercontent.com/8337251/106399977-00f45e00-63d9-11eb-974c-c937d3ad1491.png)


#### Section 3: Network Policy Management

1.	VN-A_VM-1 can ping VN-B_VM-1, but VN-A_VM-2 cannot ping VN-B_VM-1

Configure Security Groups, create Security Group for each VM

![image](https://user-images.githubusercontent.com/63819430/106493245-1f5c6700-6476-11eb-9e2b-78f57892d000.png)

Reference Security Groups of each other in Security Group

![image](https://user-images.githubusercontent.com/63819430/106493317-38651800-6476-11eb-81eb-06c5ee3ecf71.png)

![image](https://user-images.githubusercontent.com/63819430/106493360-45820700-6476-11eb-815b-b69b6d26af9c.png)

![image](https://user-images.githubusercontent.com/63819430/106493438-5e8ab800-6476-11eb-861e-e61eaf5b6ee7.png)

2.	VN-B_VM-1 can go out to the Internet, but VN-A_VM-1 and VN-A_VM-2 cannot

Considering 8.8.8.8 as the Internet and using ICMP to check connectivity

VN-B_VM-1 to 8.8.8.8

Alow ICMP to 8.8.8.8 in Ingress as well as Egress

![image](https://user-images.githubusercontent.com/63819430/106493497-719d8800-6476-11eb-993d-3ba881d4a289.png)

![image](https://user-images.githubusercontent.com/63819430/106493584-909c1a00-6476-11eb-9b97-344fc63dec4f.png)

VN-A_VM-1 to 8.8.8.8

![image](https://user-images.githubusercontent.com/63819430/106493651-aa3d6180-6476-11eb-80bc-83dadc7d24be.png)

![image](https://user-images.githubusercontent.com/63819430/106493667-add0e880-6476-11eb-8839-800687816291.png)

VN-A_VM-2 to 8.8.8.8

![image](https://user-images.githubusercontent.com/63819430/106493702-ba554100-6476-11eb-91f4-7a44d7f09cf2.png)

![image](https://user-images.githubusercontent.com/63819430/106493713-bf19f500-6476-11eb-8b8b-e15ba475e019.png)
