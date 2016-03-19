# ros_pionner3_navigation_laser
@author:zhw    
@time:2016-3-17    
the workspace develped on ros to achieve navigation on pionner3AT robot with sickLMS200 laser
#分布式系统用法：    
    bbb和pc上跑同一个cakin_ws，唯一需要修改的是 ～/.bashrc 文件    
        1、bbb和pc连入同一个网段，互相可ping    
        2、分别在bbb和pc上面修改 ~/.bashrc 文件    
	    ## pc上面添加：    
	        export ROS_HOSTNAME=192.168.191.4     #本机的IP    
	        export ROS_MASTER_URI=http://192.168.191.4:11311  #跑主节点的url    

            ## bbb上面添加：    
            export ROS_HOSTNAME=192.168.191.3     #bbb的IP    
	        export ROS_MASTER_URI=http://192.168.191.4:11311  #跑主节点的url      

