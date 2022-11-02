cmake_minimum_required(VERSION 3.4)

project(horti_description)

find_package(catkin REQUIRED
)

catkin_package()

include_directories(${catkin_INCLUDE_DIRS})
