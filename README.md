# Database Assistant using LangChain and Large Language Models

![Chat Interface](artifacts/chat_UI.png)

## Project Overview

The Database Assistant project introduces a transformative approach to database interactions. Through an advanced chat interface, users can seamlessly convert their natural language queries into executable SQL commands. This innovation extends further by automatically executing these commands behind the scenes and presenting users with the corresponding records from the database. By harnessing the capabilities of LangChain and Large Language Models, this project offers an exceptionally user-friendly and intuitive solution for querying databases.

Our goal is to redefine the way users engage with databases, making the process effortless and efficient. The database assistant empowers users to communicate with databases using familiar language, eliminating the need for specialized knowledge of SQL syntax. This user-centric approach, coupled with cutting-edge technology, sets the stage for a new era of database interactions.
## Features

- **Seamless NL to SQL Conversion**: The core feature of this project is its ability to convert natural language queries into SQL commands. Users can simply type their questions or requests in plain English, and the system will generate the corresponding SQL scripts and execute it.

- **Gradio-Powered Chat Interface**: To provide an interactive and engaging user experience, we have integrated Gradio, a user-friendly library for creating web interfaces. The chat interface allows users to input their queries and instantly receive the corresponding SQL query execution output.

- **Microsoft Azure Integration**: This project seamlessly connects the chat interface to a SQL database using Microsoft Azure services. Various tables are set up within the Azure environment to efficiently store and manage data.

- **Efficient Data Management**: The Azure-based setup ensures efficient data management, allowing users to store, retrieve, and manipulate data seamlessly through the chat interface.

- **LangChain Communication**: In the backend, LangChain plays a crucial role in facilitating communication between the chat interface and the database. It acts as the bridge that processes user inputs, interacts with the database schema, and generates SQL scripts based on the context.

## Getting Started

Follow these steps to set up and run the database assistant on your local machine:

1. **Clone the Repository**: Begin by cloning this repository to your local machine using the following command:

   ```
   git clone https://github.com/lovigoya/Database-Assistant.git
   ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies by running:

   ```
   pip install -r requirements.txt
   ```

3. **Azure Configuration**: Set up your Microsoft Azure account and configure the database settings as specified in the `backend/config.json` file.

4. **Run the Chat Interface**: Launch the chat interface by running the following command:

   ```
   cd /frontend
   python app.py
   ```

5. **Access the Interface**: Open your web browser and navigate to `http://localhost:7860` to access the database assistant. Start typing your natural language queries and witness the magic of instant SQL conversion!

## Future Enhancements

This project lays the foundation for a host of potential enhancements and extensions:

- **Multi-database Support**: Extend the project to support a variety of database systems, allowing users to interact with different databases seamlessly.

- **Query Optimization**: Implement query optimization techniques to enhance the performance of generated SQL scripts.

- **User Authentication**: Integrate user authentication and role-based access control for secure and personalized interactions.

- **Advanced Language Models**: Experiment with even more advanced language models to improve the accuracy and naturalness of the NL to SQL conversion.

## Contributions

Contributions to this project are welcome and encouraged! Whether you're interested in adding new features, fixing bugs, or improving documentation, your contributions can make a meaningful impact.

To contribute, simply fork this repository, create a new branch for your work, make your changes, and submit a pull request. Be sure to follow our contribution guidelines and code of conduct.