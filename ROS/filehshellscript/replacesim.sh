#prev=$(head -1 m.txt)
#new=$(tail -1 m.txt)
read prev < /root/prevsim.txt
read new < /root/newsim.txt

eval sed -i 's/$prev/$new/g' /root/cobra/src/transformer/src/dynamix.cpp
cd /root/cobra/
source devel/setup.bash
catkin_make
