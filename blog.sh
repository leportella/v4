#!/bin/bash

count_en=$( ls -R content/en/posts | wc -l )
count_pt=$( ls -R content/pt-br/posts | wc -l )
count_es=$( ls -R content/es/posts | wc -l )

echo "Inglês: "  $count_en

echo "Português: " $count_pt

echo "Espanhol: " $count_es

total=$( expr $count_en + $count_pt + $count_es )

echo "------"
echo "Total:" $total 
