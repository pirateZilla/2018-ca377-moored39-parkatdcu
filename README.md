# PARK@DCU
#### by Declan Moore
Please find the application at [GitLab](https://gitlab.computing.dcu.ie/moored39/2018-ca377-moored39-parkatdcu) or [PythonAnywhere](http://moored39.pythonanywhere.com/park_at_dcu/)

## The App
Park@DCU is an application for the staff, students and visitors to DCU's campuses who want to avail of the parking facilities available. Users of the app can make a number of queries related to car parks across the university, these include:
* Look at historical data for particular car parks on a particular date.
* Look at Real Time parking information for a particular cap park.
* Find the optimal car park for the facility they are going to.
* Find car parks that are open at a particular time.

Our hope is that these functionalities will result in parking at DCU being an easier process than it previously was for staff, students and visitors alike.

## How to install the app locally
1. From the 'Project' page for the app on Gitlab click 'Fork' to create your own fork of the project. 
2. Rename your new fork of the project to something like `2018-ca377-<yourusername>-park-at-dcu`
3. Open the terminal in Linux. Clone the repository using the following commands:
    ```bash
    $ git clone https://gitlab.computing.dcu.ie/<yourusername>/2018-ca377-<yourusername>-parkatdcu
    $ cd 2018-ca377-<yourusername>-parkatdcu
    ```
4. Now the app is locally installed on your machine. Next, assuming you have both Python3 and Django installed on your Linux machine, type the following commands:
    ```bash
    $ cd src
    $ python3 manage.py runserver
    ```
5. Now open your browser and type `127.0.01:8000/park_at_dcu` and press `Enter`
6. The app's UI should now appear in your browser, installed and running locally for you to use.

## How to deploy the app to PythonAnywhere
1. Go to pythonanywhere.com and create an account (i.e. <yourusername>)
2. Open you settings file at `2018-ca377-<yourusername>-parkatdcu/src/ca377/settings.py` and add you PythonAnywhere URL to the list of `ALLOWED_HOSTS`.
    ```python
    ALLOWED_HOSTS = ['127.0.0.1', '<yourusername>.pythonanywhere.com']
    ```
3. Open `2018-ca377-<yourusername>-parkatdcu` in your local file explorer and write click your `src` folder and compress it to a `tar.gz` file.
4. Open the Files tab on your PythonAnywhere account and upload to `tar.gz` file.
5. Open the Consoles tab on PythonAnywhere and create a bash console. 
6. In your bash console extract your newly uploaded compressed src file.
    ```bash
    $ tar zxvf src.tar.gz
    ```
7. Make a virtualenv and install Django and required libraries onto it.
    ```bash
    $ mkvirtual --python=/usr/bin/python3.4 mysite-virtualenv
    (mysite-virtualenv) $ pip install django
    (mysite-virtualenv) $ pip install requests
    ```
8. Open the Web tab and create a new webapp using 'Add a new web app'.
9. Select 'Manual configuration'.
10. On the Web tab fill in your values for 'Source Code' (i.e. `/home/<yourusername>/.virtualenvs/mysite-virtualenv/bin/python3.4`), 'Working Directory' (i.e. `/home/<yourusername>`), and 'Virtualenv' (i.e. `/home/<yourusername>/.virtualenvs/mysite-virtualenv`)
11. Open your WSGI file (i.e. `/var/www/<yourusername>_pythonanywhere_com_wsgi.py`) and edit it to include just the Django code. It should look similar to this:
    ```python
    import os
    import sys
    path = '/home/moored39/src'
    if path not in sys.path:
    sys.path.append(path)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'src.ca377.settings'
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    ```
12. Open your bash console and set up your database.
    ```bash
    (mysite-virtualenv) $ ./manage.py migrate
    ```
13. Open the Web tab and click 'Reload <yourusername>.pythonanywhere.com'
14. Open the deployment URL to confirm it is correctly deployed (i.e. '<yourusername>.pythonanywhere.com/park_at_dcu')

## Running Test Cases
The test cases are written in Python and located in '2018-ca377-<yourusername>-parkatdcu'. They can be run locally, from the GitLab repository, or within your PythonAnywhere deployment.

#### Locally
1. Using the terminal navigate to your project directory.
    ```bash
    $ cd 2018-ca377-<yourusername>-parkatdcu
    ```
2. Run your test cases using the project's `manage.py` utility
    ```bash
    $ ./manage.py test
    ```
3. Passes, failures are errors of your unit test cases will then be presented within the terminal.

#### Gitlab
1. In your terminal, commit your most recent version of the project to your GitLab repository.
    ```bash
    $ git add .
    $ git commit -m "<insert concise commit message here>"
    $ git push -u origin master
    ```
2. Once the version has been pushed to GitLab, open the GitLab Repository in your browser.
3. Navigate to the 'Pipelines' tab.
4. All commits will be visible here with a status of 'passed' or 'failed'. In the 'Stages' column of each commit if you hover over that icon you can see each test case status. Clicking these will open the log information from the test cases indicating any passes, failures or errors from the unit test.

#### PythonAnywhere
1. Similarly to running the unittests locally, on PythonAnywhere you can run `./manage.py test` from your Bash Console.
2. The output of these tests is then printed in the console showing the passes, failures, and errors of the unit tests.
3. From the Web tab on PythonAnywhere under the 'Log files' section the 'Error log' can be accessed to view the outputs of unit tests.
    
    
    
    
    
    
    
    
    
    
    