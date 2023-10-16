# Chat App
Developed by:
*   Bruno Bianchi Pagani
*   João Gabriel Feres

## 1 About
This section will run over the concepts and ideias while developing this app, such as needs, contents and requirements over the whole proccess.

### 1.1 About the App
This app was developed by the purpose of supllying activities from DSO lectures. The group decided to code a chatting app that would englobe all OOP concepts seen during the lectures. Finally, this early version still doesn't contain guided user interface (GUI), which is going to be implementend in future versions.

### 1.2 About the Activity
The activity was given for the purpose of understanding of proggraming concepts using the python language. The students were proposen to have an ideia which could be usefull to englobe all OOP properties, where, the ambientance was left to them to think about. Thus, the students decided to make a chatting application

### 1.3 About the Proccess
The students worked along with each other for every choice made, since the UML scratches until the final version to the first delivery. They used a strategy similar to SCRUM, where they would frequently debate and talk abou the going proccess of the idea.
#### 1.3.1 UML
When developing the UML Class Diagram the students met each other and then started chatting and brainstorming abou what ideia would be choosen and also how each new Class would interact and relation with the others. 
#### 1.3.2 Implementation
The implementation of the Chat App was done similarly to the UML Class Diagram's procces. Furthermore, João was reponsible for making the "skeletons" of the classes and also the first relations and functions while Bruno worked making the messages and chat history working and quotatio of all functions. Both worked together for bug hunting and code quality improvementation.

### 2 How The App Works
The following sections will talk about how the app works and furthermore how to use it in the right way.
#### 2.1 Creating an User
The first proccess required for using the Chat App is obviously creating an user, this is done by a simple formulary registering a user nickname and a password, which is then hashed before storing it. If all requirements are done, such like password lenght or non duplicated username, then it's created a new user object and now you can log in!

#### 2.2 What Can An User Do?
The user can change its nickname and password, he also can delete its own account. While in the Chat Display, the user might create new chats, browse through existing chats and join them as well. A user can sen text, video and image messages into a chat, which will be displayed for all participants throughout the app history.
If an user delete its account, its name will be displayed as ```Deleted User```where his messages where kept. This feature works by updating the chat messages right before loading them, merging stored users to the ones displayed in the messages' information.

#### 2.3 What Is A Chat And What Can Be Done In It?
A chat is an instance of an object responsible for storing messages and letting different users to interact while joining a community or not. The chat can store three different kind of messages, which are, text, image and video messages. Each one of them works similarly, except that text messages store the proper text of the message while video and image ones store paths to files in the media folder

#### 2.4 How Are The Messages Stored?
Each Chat contains a personal ChatHistory instance where, this attribute contains all new messages, being able to show them and add new ones

#### 2.5 Model View Controll
This App also uses the Model View Controll coding strategy where all the inputs and outputs are done in exclusive classes, here named as Displays. All the objects are controlled by Controller classes which will ensure to manage all CRUD operations and functions related to the app run. All the other objects are instances that are manipulated by the controllers.

### 3 Future implementations
This section talks about what future implementations are going to exist and also which implementations are promissing ideas in order to improove the app's quality

#### 3.1 GUI
GUI or Guided User Interface is a must have in this app, because then, all the presentation of the application and also the praticity for each user is going to get better.

#### 3.2 Database
As the App works with a huge ammount of data flowing from each one of the chats, the requirement for database usage highers, leading to a possible improvement ir order to make a more professional version of the app.

#### 3.3 Making the App Real Time
Making the App a Real Time One ensures the users more confort and usability while do not require to login in and logout for each user to answering the chats. It's a promissing idea that might be done in the future

### 4 Conclusions
This app surely worked improving the students' habilities and understanding while dealing with OOP projects and activities. All the proccess also improoved their comprehension about teamwork and responsability dealing with deadlines and project flow.