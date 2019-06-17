/* Software License Agreement (BSD License)
 *
 * Copyright (c) 2011, Willow Garage, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 *  * Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above
 *    copyright notice, this list of conditions and the following
 *    disclaimer in the documentation and/or other materials provided
 *    with the distribution.
 *  * Neither the name of Willow Garage, Inc. nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 * FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 * ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 *
 * Auto-generated by genmsg_cpp from file /home/aditya/catkin_ws/src/dynamixel_motor-master/dynamixel_msgs/msg/MotorStateList.msg
 *
 */


#ifndef DYNAMIXEL_MSGS_MESSAGE_MOTORSTATELIST_H
#define DYNAMIXEL_MSGS_MESSAGE_MOTORSTATELIST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <dynamixel_msgs/MotorState.h>

namespace dynamixel_msgs
{
template <class ContainerAllocator>
struct MotorStateList_
{
  typedef MotorStateList_<ContainerAllocator> Type;

  MotorStateList_()
    : motor_states()  {
    }
  MotorStateList_(const ContainerAllocator& _alloc)
    : motor_states(_alloc)  {
    }



   typedef std::vector< ::dynamixel_msgs::MotorState_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::dynamixel_msgs::MotorState_<ContainerAllocator> >::other >  _motor_states_type;
  _motor_states_type motor_states;




  typedef boost::shared_ptr< ::dynamixel_msgs::MotorStateList_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::dynamixel_msgs::MotorStateList_<ContainerAllocator> const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;

}; // struct MotorStateList_

typedef ::dynamixel_msgs::MotorStateList_<std::allocator<void> > MotorStateList;

typedef boost::shared_ptr< ::dynamixel_msgs::MotorStateList > MotorStateListPtr;
typedef boost::shared_ptr< ::dynamixel_msgs::MotorStateList const> MotorStateListConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::dynamixel_msgs::MotorStateList_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::dynamixel_msgs::MotorStateList_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace dynamixel_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'dynamixel_msgs': ['/home/aditya/catkin_ws/src/dynamixel_motor-master/dynamixel_msgs/msg'], 'std_msgs': ['/opt/ros/hydro/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::dynamixel_msgs::MotorStateList_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dynamixel_msgs::MotorStateList_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dynamixel_msgs::MotorStateList_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dynamixel_msgs::MotorStateList_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dynamixel_msgs::MotorStateList_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dynamixel_msgs::MotorStateList_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::dynamixel_msgs::MotorStateList_<ContainerAllocator> >
{
  static const char* value()
  {
    return "9e94ccf6563ca78afce19eb097f9343c";
  }

  static const char* value(const ::dynamixel_msgs::MotorStateList_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x9e94ccf6563ca78aULL;
  static const uint64_t static_value2 = 0xfce19eb097f9343cULL;
};

template<class ContainerAllocator>
struct DataType< ::dynamixel_msgs::MotorStateList_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dynamixel_msgs/MotorStateList";
  }

  static const char* value(const ::dynamixel_msgs::MotorStateList_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::dynamixel_msgs::MotorStateList_<ContainerAllocator> >
{
  static const char* value()
  {
    return "MotorState[] motor_states\n\
\n\
================================================================================\n\
MSG: dynamixel_msgs/MotorState\n\
float64 timestamp   # motor state is at this time\n\
int32 id            # motor id\n\
int32 goal          # commanded position (in encoder units)\n\
int32 position      # current position (in encoder units)\n\
int32 error         # difference between current and goal positions\n\
int32 speed         # current speed (0.111 rpm per unit)\n\
float64 load        # current load - ratio of applied torque over maximum torque\n\
float64 voltage     # current voltage (V)\n\
int32 temperature   # current temperature (degrees Celsius)\n\
bool moving         # whether the motor is currently in motion\n\
";
  }

  static const char* value(const ::dynamixel_msgs::MotorStateList_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::dynamixel_msgs::MotorStateList_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.motor_states);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct MotorStateList_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::dynamixel_msgs::MotorStateList_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::dynamixel_msgs::MotorStateList_<ContainerAllocator>& v)
  {
    s << indent << "motor_states[]" << std::endl;
    for (size_t i = 0; i < v.motor_states.size(); ++i)
    {
      s << indent << "  motor_states[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::dynamixel_msgs::MotorState_<ContainerAllocator> >::stream(s, indent + "    ", v.motor_states[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // DYNAMIXEL_MSGS_MESSAGE_MOTORSTATELIST_H
