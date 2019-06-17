/*
0 -> sidewinding left
1 -> sidewinding right
*/
#include "ros/ros.h"
#include "std_msgs/String.h"
#include <transformer/Angle.h>
#include <math.h>
#include <sstream>

#define nMotor 10

#define PI 3.14159265

#define POS1ARRAY {-51,-20,120,32,0,20,120,20,-69}
float A0,A1,A2,A3,A4,A5,A6,A7,A8,A9,W0,W1,W2,W3,W4,W5,W6,W7,W8,W9;
float ph0,ph1,ph2,ph3,ph4,ph5,ph6,ph7,ph8,ph9,dir,delta_x,delta_y,phi;
bool torque_of=0;
double tb = 0;

void set_gait_param()
{
  A0=0;A1=90;A2=30;A3=0;A4=30;A5=0;A6=30;A7=0;A8=30;A9=90;W0=90;W1=0;W2=3;W3=1;W4=3;W5=1;W6=3;W7=1;W8=3;W9=1;ph0=0;ph1=180;ph2=0;ph3=180;ph4=120;ph5=0;ph6=240;ph7=180;ph8=360;ph9=0;
      /* A1=8;
       A2=8;
       A3=8;8
       A4=8;
       A5=8;
       A6=8;
       A7=8;
       A8=8;
       A9=8;
       W0=3.14;
       W1=3.14;
       W2=3.14;
       W3=3.14;
       W4=3.14;
       W5=3.14;
       W6=3.14;
       W7=3.14;
       W8=3.14;
       W9=3.14;
       ph0=0;
       ph1=0;
       ph2=0;
       ph3=0;
       ph4=0;
       ph5=0;
       ph6=0;
       ph7=0;
       ph8=0;
       ph9=0;*/
       delta_x = 2*3.14/3;
       delta_y = 2*3.14/3;
       phi=0;
       dir=1;
}

double angle_gen(uint8_t motor_id, double t)
{
      double angle;
      if(motor_id==0)
           angle = A0*sin( W0*t + ph0*PI/180);
      if(motor_id==1)
           angle = A1*sin( W1*t + ph1*PI/180);
      if(motor_id==2)
           angle = (A2*sin( W2*t + ph2*PI/180));
      if(motor_id==3)
           angle = A3*sin( W3*t + ph3*PI/180);
      if(motor_id==4)
           angle = (A4*sin( W4*t + ph4*PI/180));
      if(motor_id==5)
           angle = A5*sin( W5*t + ph5*PI/180);
      if(motor_id==6)
           angle = (A6*sin( W6*t + ph6*PI/180));
      if(motor_id==7)
           angle = (A7*sin( W7*t + ph7*PI/180));
      if(motor_id==8)
           angle = ((A8*sin( W8*t + ph8*PI/180)));
      if(motor_id==9)
           angle = (A9*sin( W9*t + ph9*PI/180));

       return angle;
}


int main(int argc, char **argv)
{
       set_gait_param();      
       transformer::Angle msg;
       ros::init(argc, argv, "gait_generator");
       ros::NodeHandle n;
       ros::Publisher gait_pub = n.advertise<transformer::Angle>("gait_topic",1000);
       ros::Rate loop_rate(100);

double cTime;
       double iTime = ros::WallTime::now().toSec();        

       while(ros::ok())
       {
               cTime = ros::WallTime::now().toSec()-iTime;
               for(int i=0; i<nMotor; i++)
               {
                       msg.motor_id = i;
                       msg.angle_value = angle_gen(i,cTime);
                       gait_pub.publish(msg);
ROS_INFO("ID:%d Angle:%f", i, msg.angle_value);
               }      
               ros::spinOnce();
               loop_rate.sleep();        
       }

       return 0;
}   
