# **Real-Time Chat Application**

## **Description**

This project provides a **real-time chat application** built with **Flask** and **Flask-SocketIO**, enabling users to communicate seamlessly in real time. It supports **chat rooms**, secure user authentication, and persistent chat history storage using **SQLite**. The application is designed with a clean, modular structure to ensure scalability and maintainability.



## **Features**

- **Real-Time Messaging**  
    Enables instant message delivery using **Flask-SocketIO**.
    
- **Chat Rooms**  
    Supports creating and managing **rooms** for group-based conversations.
    
- **Secure User Authentication**  
    Ensures that only registered and logged-in users can access chat rooms.
    
- **Persistent Data Storage**  
    Stores chat history and user data in a **SQLite** database.
    
- **Scalable and Modular Design**  
    Organized code structure ensures maintainability and scalability for future enhancements.
    


## Prerequisites

- Python 3.9+
- pip
- Virtual environment support
## **Libraries Used**

- **Flask** 
- **Flask-SocketIO** 
- **SQLite** 
- **Flask-Login** 
- **SQLAlchemy** 



## **Installation and Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/pavandandla/Real-Time-Chat-Application.git
cd Real-Time-Chat-Application
```



### **2. Create a Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```



### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```



### **4. Configure the Environment Variables**

Create a `.env` file in the project root directory with the following configuration:

```plaintext
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///chat_app.db
```

- **SECRET_KEY**: A secret key for secure sessions.
- **DATABASE_URL**: Connection string for SQLite.



### **5. Initialize the Database**

Run the following command to set up the database and tables:

```bash
python src/init_db.py
```



### **6. Run the Application**

Launch the Flask development server:

```bash
flask run
```

The application will be available at: `http://127.0.0.1:5000`



## **Real-Time Workflow**

1. **User Authentication**  
    Users must **register** and **log in** to access the chat application.
    
2. **Chat Rooms**  
    Users can join specific **rooms** for group-based conversations.
    
3. **Real-Time Messaging**  
    Messages sent in a room are broadcasted instantly to all users in the room using **Flask-SocketIO**.
    
4. **Persistent Storage**  
    All messages and chat history are stored in the **SQLite** database.
    



## **Example Chat Room Workflow**

1. **Join a Room**:
    - A user selects or creates a room to join.
2. **Send a Message**:
    - Messages are sent via WebSockets and broadcasted to all connected users in the room.
3. **View History**:
    - Upon joining, the previous chat history for the room is loaded from the database.



## **Environment Configuration**

Sample `.env` file:

```plaintext
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///chat_app.db
```


## **Contact**

For questions, suggestions, or issues, contact:

- GitHub: [pavandandla](https://github.com/pavandandla)
