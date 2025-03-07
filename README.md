# ELLMA-T
This is the updated version of ELLMA-T, an langauge tutor in VRChat, with improved voice response, body and facial expressions and reasoing ability

#Participant Check-In System
This package contains a simple participant check-in system consisting of:

A front-end login page built with the Layui framework.
A Java Spring Boot backend for handling check-in logic.
An SQLite database for storing check-in records.
A Python script that connects the database with the AI agent program (should be integrate to the main logic).

Extract the Zip Files
1.Download and unzip:

VRChatSignIn.zip → Place its contents in your project folder.
signin.zip → Place its contents in your project folder.
Move demo.db to D:/ directory (this will serve as the local database).

2️.Run the Backend
Ensure JDK 8 is installed. If needed, unzip and use jdk-8.zip.
Open a command line (CMD or Terminal).
Navigate to the folder containing the .jar file.
Run the backend using:
java -jar book-1.0-SNAPSHOT.jar
The backend should be running and receving input from the frontpage.

3️.Connect the Python Script
The Python script monitors the SQLite database for new entries.
It retrieves participant check-in data and integrates it with the AI agent system.
It should be integrated to main logic in the Agent project python file.

To do:
implement the logic in python file to constantly monitor participant check in
integrate the monitor logic to the conversation logic (once participant checks in, they can intiate interaction will agent and their conversation history will be created)
implment the logic so that when participant finishes the session, python program detects the end of the converstion and upload converstion hisotry to mongDB
-> await next participant check in
