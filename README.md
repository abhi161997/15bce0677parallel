# 15bce0677parallel
This repository is created for submitting my project on parallel computing


In this project, I will be extracting the coordinate point from the database and plotting it to graph using python map library as visualizing the output while processing distance computation using parallel computing libraries in python. 


extract.py

The purpuse of this file is to extract the data from the data base using multiple threads, calculate distance between coordinates or the locations and check weather the location satisfies the shortest path equation of the two points, which is almost a linear graph but with a slight distortion from the original equation.

At first the database is divide into 4 sections(can be more depends on the no of cores the processing system has), each section is taken care by the thread containing the sql_fetch command to fetch data from the database.

As now the database is divided into 4 section(each to be executed by a thread contains mysql command) fetch the data from the database and compare it to other parallel threads in execution that satisfies the equation. 

The coordinates which satisfies the equation is stored into the array.

Here I used parafor loop for executing parallel commands and running threads successfully on different core architecture.
