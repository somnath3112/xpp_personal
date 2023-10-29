%
rosinit 

% Subscribe to tf
sub = rossubscriber('/tf');
%
lf_h = 1; lf_u = 2; lf_l = 3;
lh_h = 4;

% Publish controls
pub_lf_h = rospublisher('/hyq/lf_haa_joint_position_controller/command'); 
pub_lf_f = rospublisher('/hyq/lf_hfe_joint_position_controller/command'); 
pub_lf_k = rospublisher('/hyq/lf_kfe_joint_position_controller/command'); 
pub_lh_h = rospublisher('/hyq/lh_haa_joint_position_controller/command'); 
pub_lh_f = rospublisher('/hyq/lh_hfe_joint_position_controller/command'); 
pub_lh_k = rospublisher('/hyq/lh_kfe_joint_position_controller/command'); 
pub_rf_h = rospublisher('/hyq/rf_haa_joint_position_controller/command'); 
pub_rf_f = rospublisher('/hyq/rf_hfe_joint_position_controller/command'); 
pub_rf_k = rospublisher('/hyq/rf_kfe_joint_position_controller/command'); 
pub_rh_h = rospublisher('/hyq/rh_haa_joint_position_controller/command'); 
pub_rh_f = rospublisher('/hyq/rh_hfe_joint_position_controller/command'); 
pub_rh_k = rospublisher('/hyq/rh_kfe_joint_position_controller/command'); 
% initialize message type 
cmsg = rosmessage(pub_lf_h); 

%%
%
% smsg = receive(sub,1); 
%
cmsg.Data = 0;  
send(pub_lf_h,cmsg); send(pub_lf_f,cmsg); send(pub_lf_k,cmsg); 
send(pub_lh_h,cmsg); send(pub_lh_f,cmsg); send(pub_lh_k,cmsg); 
send(pub_rf_h,cmsg); send(pub_rf_f,cmsg); send(pub_rf_k,cmsg); 
send(pub_rh_h,cmsg); send(pub_rh_f,cmsg); send(pub_rh_k,cmsg); 

%
keyboard 
rosshutdown 