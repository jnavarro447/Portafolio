#!/bin/bash

# Given a list of countries, each on a new line,
# your task is to read them into an array and then display 
# the element indexed at 3.

# Create an array, passing as parameter the file w names(elements)
declare -a country=( $(cat ./country.txt) )

# Display the 3th element
echo ${country[@]:3:1}
