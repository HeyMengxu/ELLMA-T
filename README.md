# ELLMA-T

This is the updated version of **ELLMA-T**, a language tutor in **VRChat**, with improved **voice response, body and facial expressions, and reasoning ability**.

---

## Participant Check-In System

This package contains a simple **participant check-in system** consisting of:

- A **front-end login page** built with the **Layui framework**.
- A **Java Spring Boot backend** for handling check-in logic.
- An **SQLite database** for storing check-in records.
- A **Python script** that connects the database with the AI agent program (**should be integrated into the main logic**).

---

## 1📂 Extract the Zip Files

1. **Download and unzip**:
   - `VRChatSignIn.zip` → Place its contents in your project folder.
   - `signin.zip` → Place its contents in your project folder.
   - Move `demo.db` to `D:/` directory (**this will serve as the local database**).

---

## 2🚀 Run the Backend

1. **Ensure JDK 8 is installed**. If needed, unzip and use `jdk-8.zip`.
2. **Open a command line** (CMD or Terminal).
3. **Navigate to the folder** containing the `.jar` file.
4. **Run the backend using**:
   ```sh
   java -jar book-1.0-SNAPSHOT.jar


### 3️ Connect the Python Script  

The Python script monitors the SQLite database for new entries.  
It retrieves participant check-in data and integrates it with the AI agent system.  
It should be integrated into the main logic in the Agent project Python file.  

#### **To Do:**  
- Implement the logic in the Python file to **constantly monitor participant check-in**.  
- Integrate the monitoring logic into the **conversation logic**:  
  - Once a participant checks in, they can initiate interaction with the agent.  
  - Their **conversation history will be created**.  
- Implement the logic so that when a **participant finishes the session**:  
  - The Python program **detects the end of the conversation**.  
  - The **conversation history is uploaded to MongoDB**.  
- **Await the next participant check-in.**  
