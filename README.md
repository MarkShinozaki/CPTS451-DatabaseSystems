# Project Description

## [Project Description Overview](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Project/Project%20Description)

- The project for CptS 451 involves developing a data search application for Yelp.com's business review data, with a focus on database infrastructure. The main objectives include:

1. **Database Modeling and Design**: You'll model and design a database schema that accurately represents the Yelp dataset.
   
2. **Populating the Database**: You'll populate the database with large datasets, including data from Yelp and U.S. Census zipcode data.
   
3. **Querying Large Databases**: You'll perform queries to extract useful information from these large datasets.
   
4. **Optimizing Query Performance**: You'll use indexes to optimize the performance of these queries.
   
5. **JSON Parsing**: You'll work with JSON data, extracting necessary information for the application.
    
6. **Database Application Development**: You'll develop a standalone Python application that users can interact with to gather business information.

---


### 1. Milestone 0 (No Submission Required):

- Download and install PostgreSQL Database Server.

---

### 2. [Milestone 1](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Project/Project%20Milestone%201)

#### Steps Overview:

1. Download the Yelp Dataset and JSON Parser:
      - Download the dataset from the provided course item.
      - Download the JSON parser program (Python) from the Canvas resources.
      - Examine each JSON file (e.g., `yelp_business.json`, `yelp_review.json`, `yelp_user.json`, `yelp_checkin.json`) to understand the data structure.
      - Modify the parser to extract relevant key-value pairs from these JSON files and save the parsed data into text files.

2. Parse Check-In Data:

- Focus on parsing "check-in" data that records the number of check-ins for a particular business, formatted by day and hour.

3. Design a Database Schema:

   - Design an ER (Entity-Relationship) diagram based on the application scenario described in Appendix A.
   - Your schema should be both precise and complete to ensure efficient and effective data retrieval.
   - Translate your ER model into relational tables and create DDL SQL statements to define the schema in a relational database management system (RDBMS).

4. Create and Populate a PostgreSQL Database:

   - Download the `milestone1DB.csv` file and create a PostgreSQL database named `milestone1db`.
   - Define a `business` table schema and populate it using the data from the CSV file.
   - Write a simple Python application that connects to the database and allows users to query the business data by state and city.

5. Deliverables:

   - ER Diagram and SQL DDL: Submit a PDF file of your ER diagram (`<your-name>_ER_v1.pdf`) and a .sql file with the DDL statements (`<your-name>_relations_v1.sql`).
   - Source Code: Submit a zip archive (`<your-name>_milestone1.zip`) containing your JSON parsing code and the Python application.



--- 

### 3. [Milestone 2](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Project/Project%20Milestone%202)

In Milestone 2, you will refine your initial database design, populate your database with real data, write SQL triggers, and start developing the application GUI.


1. **Refine Database Schema**:

      - Review and refine the database schema created in Milestone 1 to ensure it stores all necessary data and supports efficient queries.

2. **SQL DDL Statements (Refined)**:

      - Update the CREATE TABLE statements if necessary, including all required constraints.

3. **Data Insertion**:

      - Populate your database with the Yelp data.
      - Generate and run `INSERT` statements for your tables.
      - Make sure to initialize attributes like `numCheckins` and `reviewrating` for businesses.

4. **Calculate and Update Business Metrics**:

      - Write `UPDATE` statements to calculate and update `numCheckins`, `reviewcount`, and reviewrating for businesses.

5. **Write Triggers**:

      - Implement SQL triggers to enforce additional constraints or automate certain updates.

6. **Initial Application GUI Development**:

      - Start developing the user interface of your application.

      - Include features to display distinct states, cities, zip codes, and business categories.

7. **Deliverables**:

      - Revised ER diagram in PDF format.
      - SQL script with CREATE TABLE statements.
      - Text file with the number of tuples in each table.
      - SQL script with UPDATE statements.
      - A 2-page paper describing metrics for classifying businesses.
      - Source code of your application in a ZIP file.


---

### 4. [Milestone 3](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Project/Project%20Milestone%203)

Milestone 3 is focused on the final implementation and demonstration of your application. You will complete your application and demonstrate its functionality through a recorded video.


#### Steps:

1. **Complete Application Implementation**:

   - Finalize the development of your application, ensuring that all required features and functionalities outlined in the project description are fully implemented.

   - Test your application thoroughly to ensure it works as expected and meets all the project requirements.

2. **Prepare Source Code**:

   - Gather all your source code files related to the application.

   - Do not include any database files or unnecessary files in the submission.

   - Create a ZIP archive named _milestone3.zip containing only your source code.

3. **Record a Demo Video**:

   - Record a demo video that showcases the use cases listed in Appendix A of the project description.

   - The video should demonstrate all the key features of your application, focusing on the user interface and how the application functions.

   - The recommended video length is around 10 minutes, but shorter videos are acceptable as long as they cover all required features.

4. **Upload the Video**:

   - Upload your demo video to a streaming service like YouTube. Make sure the video is either unlisted or private so that only people with the link can view it.

   - Alternatively, you can use Zoom's 'Record to the Cloud' feature to record the demo.

5. **Submit Milestone 3**:

   - Upload the _milestone3.zip file to Canvas before the deadline.

   - Include the link to your demo video in the submission comments.



- **Complete the Application**: Implement the full application based on the detailed requirements in Appendix A.

- **Demo Video**: Record and submit a video showcasing the application's features.

### Application Functionality:

- The application allows users to search for businesses in a specific location, filter by category, and analyze businesses to determine their popularity and success. The application retrieves all data from the database, ensuring that no internal data structures are used for storage.


































