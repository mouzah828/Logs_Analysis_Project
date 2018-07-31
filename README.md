#Logs_Analysis_Project
##This project is  for generating report from fetching the data  from news database which includes three tables articles,authors,log

##In order to run this project you have to follow this steps:
1. you nedd to have virtual machine installed in your PC, so install VirtualBox
2. Install Vagrant
3. Download the VM configuration  form https://github.com/udacity/fullstack-nanodegree-vm, save and unzip the FSND-Virtual-Machine.zip to your machine
4. After Finish installation, start the virtual machine by opening your terminal such as Git Bash

### before run this command change your directory into inside the vagrant subdirectory, and run the following command in order:
5.vagrant up
6.vagrant ssh
7.download newsdata.sql file and Put this file into ypur vagrant directory
8.cd /vagrant
9.psql -d news -f newsdata.sql
10.you have to creat this view in order to run python code without any error
*I creat this view to answer the Q3.On which days did more than 1% of requests lead to errors

> (CREATE VIEW log_error_view AS
SELECT TO_CHAR( time :: DATE, 'Month dd, yyyy')  AS error_date ,
ROUND((SUM(CASE WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END)) * 100.0 / (count(*)),1) AS error_percent
FROM log
GROUP BY error_date)

11.change your directory to the project folder using this command: cd Logs_Analysis_Project
12.run the python code that is inside project folder by this command: python newsdp_query.py



