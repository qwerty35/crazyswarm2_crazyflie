# crazyswarm2


## Install
1. Install Crazyswarm2 (https://imrclab.github.io/crazyswarm2/installation.html)
2. Overwrite this packagein your crazyswarm2 folder
3. In the terminal,

```
pip install ruamel.yaml
cd ~/ros2_ws
colcon build --symlink-install
```

## Usage
alias cfserver='ros2 launch crazyflie launch.py'
alias chooser='ros2 run crazyflie chooser.py'
alias swarm_manager='ros2 run crazyflie_example swarm_manager.py'
