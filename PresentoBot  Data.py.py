#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Dictionary to hold the topics and sub-topics
data = {
    "Data Science": {
        "Sub Topics": ["Data Mining", "Big Data"],
        "Intro": {
            "Data Mining": "Data mining is the process of extracting valuable information from large datasets.",
            "Big Data": "Big data refers to extremely large datasets that can be analyzed to reveal patterns, trends, and associations.",
            
        }
    },
    "A.I": {
        "Sub Topics": ["Machine Learning", "Computer Vision"],
        "Intro": {
            "Machine Learning": "Machine learning is a method of teaching computers to learn from data without being explicitly programmed.",
            "Computer Vision": "Computer vision is a field of artificial intelligence that trains computers to interpret and understand visual data from the world around them."
        }
    },
    "ML": {
        "Sub Topics": ["Deep Learning", "Neural Networks", "Supervised Learning", "Unsupervised learning", "Reinforcement Learning", "Linear regression", "Logistic regression", "Random forest"],
        "Intro": {
            "Deep Learning": "Deep learning is a type of machine learning that uses artificial neural networks to model and solve complex problems.",
            "Neural Networks": "Neural networks are a type of machine learning algorithm that are modeled after the structure and function of the human brain.",
            "Supervised Learning": "Supervised Learning is a type of machine learning where the algorithm is trained on a labeled dataset, where the output for each input is known.",
            "Unsupervised learning": "Unsupervised learning is a type of machine learning where the algorithm is not given labeled data or specific instructions,but instead must find patterns and relationships in the data on its own.",
            "Reinforcement Learning": "Reinforcement learning is a type of machine learning that trains agents to make decisions by rewarding desired behavior and punishing undesired behavior.",
            "Linear regression": "Linear regression is a machine learning algorithm based on supervised learning. It performs a regression task. Regression models a target prediction value based on independent variables.",
            "Logistic regression": "Logistic regression is a supervised machine learning algorithm used for classification tasks, which predicts the probability of an outcome based on one or more input variables.",
            "Random forest": "Random forest is a machine learning algorithm that combines multiple decision trees to improve predictive accuracy and reduce overfitting."
        }
    },
    "CSE": {
        "Sub Topics": ["Operating Systems", "Computer Networks", "Database Management Systems", "Artificial Intelligence", "Data Science", "Cyber Security", "Data Stracture and Algorithm"],
        "Intro": {
            "Operating Systems": "An operating system is a software that manages computer hardware and software resources and provides common services for computer programs.",
            "Computer Networks": "A computer network is a group of computers and other devices connected together to share resources and communicate with each other.",
            "Database Management Systems": "Database Management Systems (DBMS) are software applications that manage the storage, organization, and retrieval of data in a structured format.",
            "Artificial Intelligence": "Artificial Intelligence (AI) refers to the ability of machines to mimic human intelligence and perform tasks that would normally require human-level intelligence.",
            "Data Science": "Data science is an interdisciplinary field that uses statistical and computational methods to extract knowledge and insights from data.",
            "Cyber Security": "Cybersecurity refers to the practice of protecting computer systems, networks, and digital information from unauthorized access, theft, damage, or other threats.",
            "Data Stracture and Algorithm": " Data structures are ways of organizing and storing data for efficient access and modification, while algorithms are step-by-step procedures for solving problems."
        }
    },
    "IOT": {
        "Sub Topics": ["Wireless Sensor Networks", "Smart Home", "Face Recognition Bot", "Control TV With Alexa", "Smart Agriculture System", "Weather Reporting System", "Smart Parking System", "Flood Detection System" ],
        "Intro": {
            "Wireless Sensor Networks": "Wireless sensor networks are networks of spatially distributed sensors that communicate with each other and send data to a central location for analysis.",
            "Smart Home": "A smart home is a residence that uses internet-connected devices to control and automate lighting, heating, and other appliances.",
            "Face Recognition Bot": "A face recognition bot to identify individuals through facial features. It can be integrated with IoT devices such as cameras and sensors to monitor and control access to secure locations.",
            "Control TV With Alexa": "Controlling TV with Alexa in IoT involves connecting a smart TV to an Amazon Echo device, which acts as a voice-activated hub.",
            "Smart Agriculture System": "Smart Agriculture System in IoT uses sensors and devices to monitor and automate farming operations for increased efficiency and yield.",
            "Weather Reporting System": "Weather reporting system in IoT is a network of interconnected devices that collect, transmit and analyze weather data for accurate forecasting.",
            "Smart Parking System": "Smart parking system in IoT is a technology that uses sensors to detect parking space availability and provides real-time data.",
            "Flood Detection System": "Flood detection system in IoT detects and alerts the user of potential flood hazards through sensor data and communication technologies."
        }
    }
}

