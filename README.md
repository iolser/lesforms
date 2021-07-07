# lesforms
 
<h1>Getting started</h1>

<h2>Requirements</h2>
<a href="https://www.npmjs.com/get-npm">Node 14</a><br>
<a href="https://www.python.org/downloads/">Python 3.9.5 or higher</a><br>
<a href="https://visualstudio.microsoft.com/visual-cpp-build-tools/">Microsoft Visual C++ 14.0 (You might already have this)</a><br>
(Optional) VirtualEnv: pip install virtualenv

<h2>Instalation</h2>
Open two terminals and use these commands to get started:

<h3>Terminal 1</h3>
<ol>
  <li>
    cd frontend
  </li>
  <li>
    npm install
  </li>
</ol>


<h3>Terminal 2</h3>
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
    python manage.py migrate
  </li>
  <li>
    python manage.py createsuperuser
  </li>
</ol>

<p>
  If problems arise related to node-sass, <a href="https://github.com/sass/node-sass#supported-nodejs-versions-vary-by-release-please-consult-the-releases-page-below-is-a-quick-guide-for-minimum-support">refer to the version guide</a> and install the appropriate version. <br>
  E.g., for Node 12 install node-sass 4.12 - npm install node-sass 4.12. <br>
  The problem can also be due to your internet blocking npm from installing from github.
  </p>

<h2>Running the servers</h2>

<h3>Terminal 1</h3>
<ol>
  <li>
    cd frontend 
  </li>
  <li>
    npm run serve
  </li>
</ol>


<h3>Terminal 2</h3>
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
  
  Edit frontend/vue.config.js line 5 to enable local network access. Find your local IP with ipconfig.<br>
  Also add your IP to the Django ALLOWED_HOSTS at backend/Event_Management/settings.py line 29.<br>
  Finally, run the server with "python manage.py runserver 0.0.0.0:8000"
  
  The api is at forms/api. For instance, http://127.0.0.1:8000/forms/api.
</p>

<h2>Preparing Sublime Text</h2>
<p>
  Press CTRL+SHIFT+P<br>
  Type "Install Package" and press ENTER<br>
  Install:<br>
  Vue Syntax Highlight<br>
  TypeScript<br>
  JsPrettier<br>
  Sass<br>
  <br>
  Go to Preferences > Package Settings > JsPrettier > Settings - Default and change "auto_format_on_save" to true<br>
  When on a Vue file, select View > Syntax > Vue Component<br>
  For easy navigation, go to File > Open Folder and select the project folder
</p>
  
<h2>Contributing</h2>

<p>After adding a new Python package, run pip freeze > requirements.txt</p>
