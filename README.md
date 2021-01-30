# NVO_OpenStack_Lab

### Objective 2: Mukesh
  - The autoscale tool will first login into the servier via SSH, and monitor the CPU load at the interval of every 40 secs(evaluation_period). 
  - Whenever the current load at the server is more than the predefined threshold value, the autoscale script will create a new replica of monitored server. 
  - Here we can take input form the user for the flavor,network_id and the source image too. for now the values are defined in the tool itself. 
  - The tool will also keep count of created autoscale server. As soon the count is reached to a predefined max_scaling_size, the tool will not create any new server and will just     keep monitoing the orginal server load.
  - Here we have cirros image as os. So any specific linux stress tool will not work as cirros image is avery basic linux os. So for generating stress, i have used the following       commands to start/stop the load on the server.

  Start stress: "for i in 1 2 3 4; do while : ; do : ; done & done"
  Stop stress:  "for i in 1 2 3 4; do kill %$i; done "
  
  -	Before activity only one server in the dashboard.
    https://github.com/mukesh0733/images/commit/a599a29dce409defd3f0a05759477f29955bd463#commitcomment-46538272
  
  - Stress generated to the server:
  https://github.com/mukesh0733/images/commit/a599a29dce409defd3f0a05759477f29955bd463#commitcomment-46538288
  
  - After activity, the process killed:
 https://github.com/mukesh0733/images/commit/a599a29dce409defd3f0a05759477f29955bd463#commitcomment-46538298

  - New 4 Autoscale servers created:
  https://github.com/mukesh0733/images/commit/a599a29dce409defd3f0a05759477f29955bd463#commitcomment-46538305
  
  -	Console output of the tool:
  https://github.com/mukesh0733/images/commit/a599a29dce409defd3f0a05759477f29955bd463#commitcomment-46538312
  https://github.com/mukesh0733/images/issues/1#issue-797351077
