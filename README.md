# CoWin-Notifier 🤩💉

# Architecture : 
<img  src="https://github.com/ishika2020/CoWin-Notifier/blob/main/project-images/architecture.png" />
  
### In this project we have used Web scraping process. 💁🏻‍♀️<br />
## Web scraping, also known as web data extraction, is the process of retrieving or “scraping” data from a website. This information is collected and then exported into a format that is more useful for the user. Be it an API.

<img src="https://github.com/ishika2020/CoWin-Notifier/blob/main/project-images/web-scrapping.png" />

### 👉🏻 First we have to access the Python library in our python Environment, So we have installed library named “requests”. Then we need to import some package like requests, datetime, timedelta , time , json, etc. Here requests library to used grab the page, datetime module is used toshow the date , time module  is used to show the time and the JSON module is used to convert the python dictionary into a JSON string that can be written into a file. <br />

<img src="https://github.com/ishika2020/CoWin-Notifier/blob/main/project-images/flask-mongodb.jpg" />

### 👉🏻 Also, to connect the backend database, here we have used document-based database, MongoDB, with python we have used pymongo library such that if any data is retrieved from the registration page it would be directly saved in the database. <br />

<img src="https://github.com/ishika2020/CoWin-Notifier/blob/main/project-images/pymongo-mongodb.png" />

### 👉🏻 Now, as new user comes to the website and registers by provide his/her details like username, email id, password. The details will be saved in MongoBD database and further mail will be sent to the user that his/her registration is confirmed. This would be done with the help of Automation Tool “Ansible”. <br />

### 👉🏻 As we are looking for  slot of availability nearby, so we have performed the search based on Pin-Code. One can also pass pin-codes. Now user can decide for how many days slot are to be checked and give the value of num of days as per their choice. 

### 👉🏻 Now, we have run a loop to convert into list format. Here, we have used timedelta method to convert it into list format. Again, we have run a loop to fetch the dates from the list and we will make use of strftime method. <br />

### 👉🏻 Next, we have run a while loop to fetch the details of the slots. Now we have defined a URL and passed two parameters that is pincode. (To fetch details for each pin-code) and date (to fetch details for each date in the given pin-code). Every time the inner loop will run then this URL will be called and respective date and pin code will be passed as an argument. <br />

### 👉🏻 In order to get requests, we have defined a header and to call the request we use “get” method. Here our response will get stored in a result. To print the Result, we have used text method. But the details(data) we get is not in structured properly so now have used json module. <br />

### 👉🏻 Then as soon as the centers are retrieved, we will save the details in one file using python file handling concepts and then ansible playbook will be triggered and mail will be sent to the user “Vaccine is available” with the center details and if we didn’t find any details then again ansible playbook will be triggered and mail will be sent to the user “Vaccine is not available” <br />

<img src="https://github.com/ishika2020/CoWin-Notifier/blob/main/project-images/get-vaccine.jpg" />
