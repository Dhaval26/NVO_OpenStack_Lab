try:
    from netmiko import ConnectHandler
    from novaclient import client
    import time
    import sys
except Exception as e:
    print(e)

max_scale_size=4
evaluation_period=40
cpu_threshold='3.0'

def create_vm(scale_size):
    try:
        nova = client.Client(version = 2.1, username = "admin", password = "stack", project_name = "demo", auth_url = "http://192.168.112.128/identity", user_domain_id="default",user_domain_name="default",project_domain_name="default")
        instance_image=nova.glance.find_image("ngn_lab2_cirros")
        instance_flavour=nova.flavors.find(name="ngn.tiny")
        instance_network_private=nova.neutron.find_network(name="lab2-autoscale").id
        instance_name='Autoscale_'+str(scale_size)
        nova.servers.create(name=instance_name, flavor=instance_flavour, image=instance_image, nics=[{'net-id':instance_network_private}])
        print("Instance created with the name:{}".format(instance_name))
    except Exception as e:
        print(e)

def main(max_scale_size,evaluation_period,cpu_threshold):
    try:
        scale_size=1
        device = { 'device_type': 'linux', 'host': '172.24.4.41', 'username': 'cirros', 'password': 'gocubsgo'}
        net_connect = ConnectHandler(**device)
        print("\nSSH connecion done with the server")
        interval=0
        while 1:
            if net_connect:
                load=net_connect.send_command('uptime').split()[-3].split(',')[0]
                print('Time:{} Load:{}'.format(interval,load))
                if load>cpu_threshold:
                    if scale_size<=max_scale_size:
                        print("\nCPU load is more than the threshold value. Now creating a new VM\n")
                        create_vm(scale_size)
                        scale_size+=1
                    else:
                        print("\n------------------Maximum scale size reached. So only monitoting will be done form now------------------")
                interval+=evaluation_period
                time.sleep(evaluation_period)
        net_connect.disconnect()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        net_connect.disconnect()
        sys.exit()

main(max_scale_size,evaluation_period,cpu_threshold)

