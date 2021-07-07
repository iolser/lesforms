# lesforms
 
<h1>Getting started</h1>

<h2>Requirements</h2>
<a href="https://www.python.org/downloads/">Python 3.9.5 or higher</a><br>
<a href="https://visualstudio.microsoft.com/visual-cpp-build-tools/">Microsoft Visual C++ 14.0 (You might already have this)</a><br>
(Optional) VirtualEnv: pip install virtualenv

<h2>Instalation</h2>
Open a terminal and use these commands to get started:

<h4>Optional</h4>
<ol>
  <li>
    virtualenv .
  </li>
  <li>
    Scripts\activate.bat
  </li>
</ol>

<h4>Not optional</h4>
<ol>
  <li>
    pip install -r requirements.txt
  </li>
  <li>
    cd backend
  </li>
<li>
    python manage.py makemigrations
  </li>
  <li>
    python manage.py migrate --fake (Or without fake if deploying to a new database)
  </li
</ol>

<h2>Running the servers</h2>

<h3>Terminal</h3>
<h4>Optional</h4>
<ol>
  <li>
    Scripts\activate.bat
  </li>
</ol>

<h4>Not optional</h4>
<ol>
  <li>
    cd backend
  </li>
  <li>
    python manage.py runserver
  </li>
</ol>

<h3> Information </h3>
<p>
  The app can be accessed at these addresses:<br>
  <ul>
    <li>
      http://localhost:8000/
    </li>
    <li>
      http://127.0.0.1:8000/
    </li>
  </ul>
  
  To enable local network access, find your local IP with ipconfig.<br>
  Then, add your IP to the Django ALLOWED_HOSTS at backend/Event_Management/settings.py line 29 (aprox).<br>
  Finally, run the server with "python manage.py runserver 0.0.0.0:8000"
  
  The api is at forms/api. For instance, http://127.0.0.1:8000/forms/api.
</p>
  
<h2>Contributing</h2>

<p>After adding a new Python package, run pip freeze > requirements.txt</p>
