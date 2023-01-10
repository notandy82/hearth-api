# The Hearth of the Dungeon API

Tabletop games, while always popular, have greatly increased in popularity over the last several years. This is also true of tabeltop role-playing games, such as Dungeons & Dragons, Pathfinder, and a host of others. Libraries, bookstores, cafés, and sometimes bars host game nights, while families and groups of friends will meet wherever they can to play. During the COVID-19 pandemic, people turned to playing their games online using virtual tabletops. The purpose of this site is to enable people to find new groups to play with and for those already in groups to be able to engage in discussion regarding their games. Groups can be created by users and can then be followed. Users can post images and conversation topics to these groups, with commenting and liking available. A group owner can also post event notifications to their group.
Live demo [_here_](https://notandy82-hearth-api.herokuapp.com/)


## Table of Contents
* [User Experience (UX)](#user-experience)
  * [User Stories](#user-stories)
* [Features](#features)
  * [Existing Features](#existing-features)
  * [Features to Implement](#features-to-implement)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
  * [GitHub](#github)
  * [Heroku and Django](#heroku-and-django)
* [Credits](#credits)
* [Contact](#contact)


## User Experience (UX)

### User Stories

-User
 - As a user, I would like to be able to create a user account on the site.
 - As a user, I would like to be able to create multiple bookings for the event.
 - As a user, I would like to be able to review and edit my bookings.
 - As a user, I would like to know how much the event will cost.


## Features

### Existing Features

- Profiles
  - Users are able to sign up to view the site. They can include their name, an image, and a short description of themselves.

- Parties
  - The party is the focal point of the site. Users can create a party. Within the party, images and comments can be uploaded, and comments can be made on these. Events can also be scheduled within the party. Users can then follow these parties. Posts and events will then be displayed on their feed. The main information for each party includes a name, a description, an image, and a location.

- Posts
  - Users can post images or discussion to parties that they are following.

- Comments
  - Users can post comments on other users' posts

- Likes
  - Users can 'like' another user's post. The number of likes on each post is displayed on the post.

- Following
  - Users are able to follow parties. This will result in any posts and dates made for that party to display in their feed.

- Dates
  - A party owner can create events so that followers will know when the party is having a game night.

- Admin Panel
  - The admin panel provides the admin with the ability to manage users, groups, and posts.

### Features to Implement
- Allowing party owners to approve any party follower (this would then change to party members).


## Technologies Used

### Languages

- Python

### Libraries and Programs
- GitPod for building and editing code
- GitHub for storing code and deploying site
- Git for version control
- Django REST framework
- Django allauth and dj-rest-auth for user verification
- Balsamiq for initial development
- Heroku for project deployment
- ElephantSQL for database management
- Cloudinary for image hosting


## Testing

- Python
  - All python code was run through [ExtendsClass](https://extendsclass.com/python-tester.html). One syntactical error was found several of the model files, but as this conformed to the syntax used in lessons, this error was ignored.
- API function was checked manually and through Postman.


## Deployment
The site was deployed through GitHub and Heroku

### Github
 - The repository was created as follows:
   - Log in to GitHub
   - In the search bar, search for Code Institute's gitpod full template
   - Select Use this template
   - Fill in a repository name
   - Click Create repository from template
   - Click the greeen Gitpod button to create a new workspace

### Heroku and Django
 - The process of setting up Django and deploying to Heroku was done by following the Code Institute [cheatsheet](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit)


## Credits

### Content
- View clarification provided by Django Rest Framework documentation found [here](https://www.django-rest-framework.org/)
  
- Thanks
  - Thanks to my family for their support and patience
  - Thanks to my mentor Adegbenga Adeye for his guidance


## Contact
Created by Andrew Stanek (notandystanek@gmail.com)