# cd /home/hero/Desktop/rm_vision01zxw/rm_vision01
# . install/setup.sh 
# sudo ps -ef | grep ros | grep -v grep | awk '{print $2}' | xargs sudo kill -9
# ros2 launch /home/hero/Desktop/rm_vision01zxw/rm_vision01/src/rm_vision_bringup/launch/vision_bringup.launch.py

# # sleep 120
# # cd ~/Desktop/bag
# # gnome-terminal -x bash -c "ros2 bag record /detector/result_img/compressed /image_raw/compressed /tf /tracker/marker /detector/marker /aiming_point --max-bag-size 4073741824 "

cd /home/hero/Desktop/rm_vision01zxw/rm_vision01
#colcon build --symlink-install
sudo chmod 777 /dev/rmvision
. install/setup.sh
sudo ps -ef | grep ros | grep -v grep | awk '{print $2}' | xargs sudo kill -9
cmds=(
	# "ros2 launch rm_bringup bringup_real.launch.py world:=RMUC mode:=mapping lio:=fastlio"
	"ros2 launch /home/hero/Desktop/rm_vision01zxw/rm_vision01/src/rm_vision_bringup/launch/vision_bringup.launch.py"
	# "ros2 launch rm_bringup bringup_real.launch.py world:=RMUC mode:=nav lio:=fastlio localization:=slam_toolbox"
	# "ros2 run rm_behavior_tree rm_behavior_tree"

	# "'/home/pq/Desktop/bubble_slam/src/rm_behavior_tree/rm_decision_interfaces/publish_script.sh'"
	)


for cmd in "${cmds[@]}";
do
	echo Current CMD : "$cmd"
	gnome-terminal -x bash -c "cd /home/hero/Desktop/rm_vision;source /opt/ros/humble/setup.bash ;$cmd;exec bash;"
	sleep 0.2
done