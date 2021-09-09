# MezzeMode
![mockup](static/assets/img/mockup.png)

### Table of contents 
* [UX (User Experience)](#ux--user-experience-)
    + [User Stories](#user-stories)
    + [User Goals](#user-goals)
* [Design](#design) 
    + [Color Scheme](#colorscheme) 
    + [Typography](#typography)
* [Wireframes](#wireframes)    
* [Features](#features)
   + [Existing Features](#existing-features)
   + [Future Features](#future-features) 
* [Information Architecture](#information-architecture)
* [Admin Credentials](#admin-credentials)
* [Technologies Used](#technologies-used)
   + [Languages Used](#languages-used)
   + [Frameworks](#frameworks)
* [Testing](#testing)
    + [User Stories Testing]()
    + [Further Testing]()
* [Bugs](#bugs)
* [Unsolved Bugs]()
* [Deployment](#deployment)
    + [Instructions](#instructions)
    + [Heroku Deployment](#deployment)
* [Credits](#credits)
    + [Content]()
    + [Media]()
    + [Aknowledgements]()

## UX
### User Stories
### User Goals
## Design
### Colour Scheme
![scheme](static/assets/img/scheme.jpg)
For this particular project, I chose to go with a shade of Hunter Green and Papaya Whip (which both compliment the hero image), Jet (black) and Platinum(white) for the text and Silver for the card edges. 

### Typography
The font I have used throughout my website is Roboto, with Sans Serif as a fallback.

## Wireframes

## Features
### Existing features
### Future features


## Information architecture
## Admin credentials


## Technologies Used 
### Languages Used
   [HTML](https://en.wikipedia.org/wiki/HTML)

   [CSS](https://en.wikipedia.org/wiki/CSS)

   [Javascript](https://en.wikipedia.org/wiki/JavaScript)

   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks
[Flask](https://flask.palletsprojects.com/en/2.0.x/)

[Werkzeug](https://flask.palletsprojects.com/en/2.0.x/)

[Jinja](https://flask.palletsprojects.com/en/2.0.x/)

[Favicon](https://en.wikipedia.org/wiki/Favicon)

[MDB Bootstrap](https://mdbootstrap.com/)

[MongoDB](https://www.mongodb.com/cloud/atlas/register)

[Start Bootstrap](https://startbootstrap.com/)

[GitHub](https://github.com/)

[Gitpod](https://www.gitpod.io/)

## Testing
### User stories testing
### Further testing

## Bugs
## Unsolved bugs
## Deployment
### Instructions

The followings must be installed :

    1. PIP
    2. Python 3.7
    3. Git ()
    4. MongoDB

a) Make sure PIP is upgraded (type the following in the CLI): 

    pip install --upgrade pip.

b) Install the necessary module in the CLI:

    pip install -r requirements.txt.

c) Within your local IDE you must create a file named .flaskenv.


d) Within the .flaskenv file, you must create a SECRET_KEY variable and a MONGO_URI to link to your own database. Please make sure to call your database goodfoodmood, with 2 collections named users and recipes.

e) If using VSCode you must create a folder named .vscode and a file named settings.json inside then add the below:

    "terminal.integrated.env.windows": {
    "SECRET_KEY": "",
    "DEV": "1",
    "HOSTNAME": "0.0.0.0",
    "PORT": "5000",
    "MONGO_URI": "[Database uri here]",
    } 

f) You may now run the application with the command line:

    python app.py

### Heroku Deployment

To deploy your website to Heroku, you should follow the instructions set out below:

1. Create a requirements.txt file with the command line:

        pip3 freeze –local > requirements.txt

2. You now need to create a Procfile by typing the command line:

        echo web: python app.py > Procfile

3. One the Procfile has been created, access the file and delete the empty line at the bottom and save the file to avoid issues.

4. Proceed to the Heroku website where you should log in and click "New" then "Create new app" and then proceed to selecting the closest region to you.

5. Proceed to the "Deploy" nav link at the top, then to "Deploy method". Once found, select the github button. Link to GitHub by entering your website repo name and clicking search and connect.

6. Click "Settings" on the top navbar and scroll to "Config Vars" then click the "Reveal Config Vars" button.

7. Copy the key, value pairs from your IDE env file and enter into the fields provided on Heroku.

8. Proceed back to your terminal and add and commit the requirements.txt file and push to GitHub.

9. Once these steps are completed, go back to Heroku and click "Deploy" and scroll down to "Automatic deploys" section then proceed and click "Enable Automatic Deploys". 

10. You should then recieve a message stating that your app has been succesfully deployed.

## Credits
### Content
### Media
### Aknowledgements