#!/usr/bin/env python 

import roslib
import rospy
# import sys
import tf 
from std_msgs.msg import Float64 
# import numpy as np
import math


## Callbacks for subscribers 
def bot_0_cb(data):
    q0 = data.pose.pose.orientation.w;
    q1  = data.pose.pose.orientation.x;
    q2  = data.pose.pose.orientation.y;
    q3 = data.pose.pose.orientation.z;
    th[0] = np.arctan2(2*(q0*q3+q1*q2),1-2*(q2*q2+q3*q3));
    xb[0] = data.pose.pose.position.x;
    yb[0] = data.pose.pose.position.y;


def main_node(): #(data_var):
    # initialize this node 
	rospy.init_node('inv_contr', anonymous=False) 

    # Publish to 'namespace'/cmd-vel topic that was created by "spawn_model" script in "gazebo_ros" package 
	lf_haa_comm = rospy.Publisher('/hyq/lf_haa_joint_position_controller/command', Float64, queue_size=10)

    # Transform listner 
	listener = tf.TransformListener()     

    # set rate
	rate = rospy.Rate(20) # 10hz 

    # initialize 
	t = 0 
	v_lf_kfe = 0 

    # main loop
	while not rospy.is_shutdown():
        # save pose data 
        # data_var.append(th.tolist())
        # data_var.append(xb.tolist())
        # data_var.append(yb.tolist())

        # Listen to the tf 
		try:
			(trans,rot) = listener.lookupTransform('hyq/trunk', 'hyq/lf_lowerleg', rospy.Time(0))
        	# print stuffs 
			print "LF KFE Joint: "
			print "X-pos: %f" % trans[0]
			print "Y-pos: %f" % trans[1] 
			print "Z-pos: %f" % trans[2] 
			print " "
		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
			continue

        # Vel_cmd.linear.x = v1
        # Vel_cmd.angular.z = v2 
		t = t+0.01
		v_lf_kfe = math.sin(2*math.pi*t) 
		print "Vel comm - LF KFE: %f" % v_lf_kfe

		lf_haa_comm.publish(v_lf_kfe)
        
		rate.sleep()

if __name__ == '__main__':
	try:
		# dat = []
		main_node() #(dat) 
	except:
		pass    
    # finally:
    #     with open('/home/put_your_user_name_here/Desktop/sc635_asgn2_data.csv', 'w') as fi:
    # 		#print dat
    # 		print "done"
    # 		for row in dat:#
    	  		# for col in row:
    #     			fi.write('{},'.format(col))
    #         		fi.write('\n')
