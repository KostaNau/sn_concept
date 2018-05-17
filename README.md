# Message System Submission

### Description
Example of primitive API for social network with user's feed and messages.
Base functionality:  
  - ```Post(X, Y)```: Post message X as user Y
  - ```Follow(X, Y)```: User X now follows user Y
  - ```Unfollow(X, Y)```: User X no longer follows user Y
  - ```UserFeed(X, K)```: Return the first (most recent) K messages of the timeline of user X


### Installation
1. Clone repository ```git clone https://github.com/KostaNau/sn_concept.git```
2. Install dependency ``` pip install requirements/base.txt```
3. Run development server ```./manage.py runserver --settings=config.settings.local```

##### Docker
1. Clone repository ```git clone https://github.com/KostaNau/sn_concept.git```
2. Make initial migrations ```docker-compose run up```


### How to work
Main entry point of app API is http://127.0.0.1:800/api/ 
- For user list use ```/api/users/```
- For user detail use ```/api/users/user_id```
- For message list use ```/api/messages/```
- For message detail use ```/api/messages/message_id```
- For user feed use ```/api/feeds/```


### High-level esign
My concept app consist of 3 entities (models):
- `User` - define user entity and user's relations with other user (following); 
- `Message` - define user's message and relations with other messages (reply to);
- `UserFeed` - define user's feed with display own messages and other users which user follow; 


### Design decisions
The main problem was a properly update `UserFeed` for actions like follow new user, unfollow user, post new message folloed user. I implemented it via `signals`, but I think it was bad decision for production-ready system. I see at lest two problems - Signals are very expensive and my implementation has a undesirable nested algorithm. I would suggest that `Celery` can resolve this two problems, but my knowledge of this tool is minimum. Anyway in limitation of time, I decided to present raw concept with limitation functionality and so-so features, but it works and can give introduction about concept.

##### Several details:
 ```view``` for avoid repeating view logic I decided to use a single class for detail and list view - ```ViewSet```;
 ```managers``` I wrote my custom manager and redefine logic of delete objects for keep all data/ Instead of physical delete, object mark as ```void``` and exclude from queryset;
 ```model behaviors``` According DRY principles I used several abstract models for model inheritance. All abstract models keeps in ```behaviors.py```;

My main mistake was to redefine ```User``` from ```django.contrib.auth.models```. Unfortunatly I understood it at the end, when I tried implemented business logic for different category users. In this matters I can't write permissions for users and authorization.


The code is written for trial assignment.
