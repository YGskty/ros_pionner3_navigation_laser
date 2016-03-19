## *********************************************************
## 
## File autogenerated for the rosaria package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 233, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 262, 'description': 'Translational acceleration (m/s^2)', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'trans_accel', 'edit_method': '', 'default': 0, 'level': 0, 'min': '-std::numeric_limits<double>::infinity()', 'type': 'double'}, {'srcline': 262, 'description': 'Translational deceleration (m/s^2)', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'trans_decel', 'edit_method': '', 'default': 0, 'level': 0, 'min': '-std::numeric_limits<double>::infinity()', 'type': 'double'}, {'srcline': 262, 'description': 'Lateral acceleration (m/s^2)', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'lat_accel', 'edit_method': '', 'default': 0, 'level': 0, 'min': '-std::numeric_limits<double>::infinity()', 'type': 'double'}, {'srcline': 262, 'description': 'Lateral deceleration (m/s^2)', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'lat_decel', 'edit_method': '', 'default': 0, 'level': 0, 'min': '-std::numeric_limits<double>::infinity()', 'type': 'double'}, {'srcline': 262, 'description': 'Rotational acceleration (rad/s^2)', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'rot_accel', 'edit_method': '', 'default': 0, 'level': 0, 'min': '-std::numeric_limits<double>::infinity()', 'type': 'double'}, {'srcline': 262, 'description': 'Rotational deceleration (rad/s^2)', 'max': 'std::numeric_limits<double>::infinity()', 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'rot_decel', 'edit_method': '', 'default': 0, 'level': 0, 'min': '-std::numeric_limits<double>::infinity()', 'type': 'double'}, {'srcline': 262, 'description': 'Encoder ticks/mm', 'max': 2147483647, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'TicksMM', 'edit_method': '', 'default': 0, 'level': 0, 'min': -2147483648, 'type': 'int'}, {'srcline': 262, 'description': 'Value in 1/8192 increments to be added or subtracted from the left encoder ticks in order to compensate for tire differences.', 'max': 2147483647, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'DriftFactor', 'edit_method': '', 'default': 0, 'level': 0, 'min': -2147483648, 'type': 'int'}, {'srcline': 262, 'description': 'The number of differential encoder ticks for a 180-degree revolution of the robot.', 'max': 2147483647, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/indigo/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'RevCount', 'edit_method': '', 'default': 0, 'level': 0, 'min': -2147483648, 'type': 'int'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

