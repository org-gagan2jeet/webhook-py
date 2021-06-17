# Github Webhook with Flask and Python on Windows

## Code exercise example:
?Please create a simple web service that listens for organization events to know when a repository has been created. When the repository is >created please automate the protection of the master branch. Notify yourself with an @mention in an issue within the repository that outlines the >protections that were added.

## Pre-requisite
Before we can start with this example, please install the following on the machine:
Software | URL
------------ | -------------
Visual Studio Code | https://code.visualstudio.com/
Python | https://www.python.org/downloads/
Ngrok | https://dashboard.ngrok.com/get-started/setup
` Ngrok is used to expose the localhost endpoint`

## Get the code repoistory and execute
* Create a new code repository
  Open the windows powershell and create a new code repo `mkdir codeblock`
* Clone the repository locally
  `git clone https://github.com/org-gagan2jeet/webhook-py.git`
* enter the repository and activate the Flask 
  `cd .\webhook-py\webhooks\Scripts>activate`
  >(webhooks) PS C:\Gagan\Github\Gagan\webhook-py\webhooks\Scripts> cd ..
  >(webhooks) PS C:\Gagan\Github\Gagan\webhook-py\webhooks>
* Set the global flask app variable (**lister_github.py is the main python executable file**)
  `$env:FLASK_APP=".\lister_github.py"`
* Run the Flask server
  `flask run`
 > Serving Flask app '.\\lister_github.py' (lazy loading)
 > Environment: production
 >   WARNING: This is a development server. Do not use it in a production deployment.
 >   Use a production WSGI server instead.
 > Debug mode: off
 > Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


 ## Execute the Ngrok server to expose the locahost
 ngrok is a free tool that allows us to tunnel from a public URL to our application running locally.

 * make sure you add the PATH variable to the for ngrok exe

 * Open command prompt and Run ngrok on the above running port
   `ngrok http 5000`

   >Session Status                online          
   >Session Expires               1 hour, 59 minutes                                                                        >Version                       2.3.40                                                                                    >Region                        United States (us)                                                                        >Interface                     http://127.0.0.1:4041                                                                     >Forwarding                    http://0f3997f5e543.ngrok.io -> http://localhost:5000                                     >Forwarding                    https://0f3997f5e543.ngrok.io -> http://localhost:5000

 * Browse the URL to see if the application is running
   `browse http://0f3997f5e543.ngrok.io`

   > Output : This is FLASK Web API
