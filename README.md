# Wiki-Scraper API
This is a brief description of what this app does and how these apis work <br/>
As specified, this is a Wiki-Scraper REST API<br/>

To start the project, one needs to run the server first using the specified virtual environment.<br/>
On Linux,<br/>
Enter following commands once you are in this directory<br/>
<pre>
    - source venv/bin/activate 
    - pip install -r requirements.txt
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py runserver
</pre>
Now the application server has started,<br/><br/>

<h3>Every Functionality implemented in the code could have been implemented using various other methods. I have used methods which I felt would be appropriate</h3>
<br/><br/>

</pre><br/>
<b>After launching the localhost, you can use below ENDPOINTS </b>
<br/><br/>
Make a Get Request To
<h4>View all Country's list</h4><br/>
ENDPOINT - <a href="http://localhost:8000/api/list/">http://localhost:8000/api/list/</a><br/>
<br/><br/>
Make a POST request to the ENDPOINT <br/>
<b>To search for any country </b><br/>
ENDPOINT - <a href="http://localhost:8000/country_info/">http://localhost:8000/country_info/</a><br/>
<br/><br/>

