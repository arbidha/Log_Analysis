###Log-Analysis
##Project Overview

This is a project assigned by Udacity as a part of the Udacity Full Stack Nanodegree program.
In this project, our task is to create a reporting tool that prints out reports based on the data in the database. This reporting tool is a Python program using the PostgreSQL database and Vagrant file settings to run a VM server to run the database.

##How to Run?

#PreRequisites:

	• Python3
	• Vagrant
	• VirtualBox

#Setup Project:

	1. Install Vagrant and VirtualBox
	2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
	3. Download the data from here.
	4. Unzip this file after downloading it. The file inside is called newsdata.sql .
	5. Copy the newsdata.sql file and content of this current repository, by either downloading or cloning it from Here

#Launching the Virtual Machine:

	1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
       	   $ vagrant up

	2. Then Log into this using command:
           $ vagrant ssh

	3. Change directory to cd  /vagrant and look around with ls.

#Setting up the database and Creating Views:

	1. Load the data in local database using the command:
	    psql -d news -f newsdata.sql

	    The database includes three tables:	    
		○ The authors table includes information about the authors of articles.
		○ The articles table includes the articles themselves.
		○ The log table includes one entry for each time a user has accessed the site.		
	2. Use psql -d news to connect to database.
	3. Create view popular_article_view using:

		CREATE VIEW popular_article_view AS
		    SELECT title ,count(*) AS views
		    FROM articles a
		    JOIN log l
		    ON a.slug = substring(l.path,10)
		    GROUP BY 1
		    order by 2 desc ;

	4. Create view error_log_view using:
		CREATE VIEW error_log_view AS
		    SELECT date(time) AS errortime ,round(100.0 * SUM(
			CASE log.status WHEN '200 OK'
			THEN 0 ELSE 1 END)
			/count(log.status),2) AS error_percent
		     FROM log
		     GROUP BY date(time)
		     ORDER BY error_percent  DESC;

#Running the queries:

	1. From the vagrant directory inside the virtual machine,run log_analysis.py
        $ python log_analysis.py
