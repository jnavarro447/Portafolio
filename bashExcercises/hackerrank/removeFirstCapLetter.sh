#!/bin/bash

#Declare an array
declare -a countries=( $(cat ./country.txt) )

# All capital letter are replaced by a dot(.)
echo ${countries[@]/[A-Z]/.}


