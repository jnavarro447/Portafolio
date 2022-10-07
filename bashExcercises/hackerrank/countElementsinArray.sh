#!/bin/bash

# Given a list of countries, each on a new line,
# your task is to read them into an array and then
# display the count of elements in that array.


# Declare an array passing as parameter the file w countrynames
declare -a country=( $(cat ./country.txt) ) 

# Print the number of elements in the array.
echo "${#country[@]}"

