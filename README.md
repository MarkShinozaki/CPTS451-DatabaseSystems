# Slides / Lectures



### [WEEK 1 - Course Introduction and Database Fundamentals](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Slides-Lectures/Week%201)

#### Introduction to Database Systems

- **What is a Database?**

  - A large, integrated collection of data, such as student records or course enrollments.
  - Captures entities (e.g., students) and relationships (e.g., student enrollments in courses).

- **Database Management System (DBMS)**

  - A software package designed to store and manage databases.
  - Examples: Oracle, MySQL, PostgreSQL, Microsoft SQL Server.

- **Traditional DBMS Goals**

  - Efficient, reliable, and safe management of large amounts of persistent, shared information.
  - Evolved from file systems with advanced features like data consistency, reliability, and query language support (SQL).

- **Key Database Technologies**

  - **Data Models**: Relational Model, Entity-Relationship (ER) Model.
  - **DBMS Languages**: SQL, Relational Algebra.
  - **Transaction Processing**: Ensures consistency during concurrent access and system failures.

- **Data Models**

  - **Relational Model**: Uses tables (relations) to represent data.
  - **ER Model**: Visual representation of entities and relationships in a database.

- **Transaction Management**

  - Ensures the database remains in a consistent state despite failures.
  - ACID Properties:
    - **Atomicity**: All or nothing execution.
    - **Consistency**: Ensures system state is consistent.
    - **Isolation**: Transactions are isolated from each other.
    - **Durability**: Committed transactions survive permanently.

#### Entity-Relationship (ER) Model

- **Overview of ER Model**

  - A visual model to specify what information a database must hold and the relationships among that information.
  - Developed by Peter Chen in 1976.

- **Key Concepts**:

  - **Entity**: A real-world object distinguishable from other objects (e.g., an employee).
  - **Entity Set**: A collection of similar entities (e.g., all employees).
  - **Attributes**: Descriptive properties of entities (e.g., name, salary).
  - **Relationships**: Associations among entities (e.g., an employee works in a department).

- **Constraints**:

  - **Key Constraints**: Ensure each entity is uniquely identifiable.
  - **Participation Constraints**: Determine if all or some entities participate in a relationship.

- **Weak Entity Sets**:

  - Entities that do not have a unique key and are identified by being related to another entity (e.g., a transaction related to an account).

- **Specialization and Generalization**:

  - **Specialization**: Classifying a class of objects into more specialized subclasses.
  - **Generalization**: Combining subclasses into a higher-level entity set.


---
### [WEEK 2 - Relational Model](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Slides-Lectures/Week%202)


This week focuses on the relational model, which is the basis for relational databases. The relational model uses tables (relations) to represent data and relationships between data. The slides cover key concepts such as schema, tuples (rows), attributes (columns), and the importance of keys (primary and foreign). Additionally, it discusses constraints, such as domain constraints, key constraints, and integrity constraints, which ensure the accuracy and consistency of the data.


#### Key Points from the Relational Model Slides:

- **Tables/Relations**: A table represents a relation in a relational model where each column is an attribute and each row is a tuple.

- **Schem**a: The structure of a relation, defined by a set of attributes.

- **Keys**: Primary keys uniquely identify tuples within a relation, while foreign keys maintain referential integrity between relations.

- **Constraints**: Rules enforced by the DBMS to maintain data integrity, including domain constraints, key constraints, and referential integrity.

- **SQL**: The slides introduce SQL as a language used to interact with databases, focusing on Data Definition Language (DDL) commands like CREATE, ALTER, and DROP for managing database schema.



---
### [WEEK 3 - Entity-Relationship (ER) 2 ](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Slides-Lectures/Week%203)

#### Key Topics Explained:

1. **ER to Relational Mapping Overview**:

    - The process of converting an ER diagram (conceptual schema) into a relational schema (logical schema) is discussed. This involves mapping entity sets, relationship sets, and various constraints to tables and keys in a relational database.

2. **Mapping Strong Entity Sets**:

    - Strong entities are converted into tables where each attribute becomes a column. The primary key of the entity becomes the primary key of the table.

3. **Mapping Relationship Sets**:

    - Relationship sets are converted into tables as well. The table contains foreign keys that reference the primary keys of the associated entities. The primary key of the relationship table is typically a composite key formed by the primary keys of the involved entities.

4. **Handling Constraints**:

    - Different types of constraints such as key constraints (e.g., primary and foreign keys), participation constraints (total or partial participation), and multiplicity constraints (one-to-one, one-to-many, many-to-many) are mapped to relational schema design.

5. **Combining Relations**:

    - In certain scenarios, relationships and entities can be combined into a single relation to reduce redundancy or handle partial participation, where attributes from both the entities and relationships are included in one table.

6. **Multiway Relationships**:

    - Multiway relationships (relationships involving more than two entities) are mapped by creating a relation that includes foreign keys from all participating entities.

7. **Mapping Weak Entity Sets**:

    - Weak entities, which cannot be uniquely identified by their own attributes, are mapped by including both the weak entity's attributes and the key attributes of the identifying strong entity in the table.

8. **Handling Aggregation**:

    - Aggregation, a higher-level abstraction where relationships are treated as higher-level entities, is mapped by creating additional tables that incorporate the relationships between aggregated entities and other entities.

9. **Subclass and Superclass Structures**:

    - Various methods for handling subclass-superclass relationships (inheritance) in a relational model are discussed, including the ER approach (treating subclasses as weak entities) and the Object-Oriented approach (using disjoint and total participation constraints).


---
### [WEEK 4 - Relational Algebra](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Slides-Lectures/Week%204)

#### Key Topics Covered:

1. **Basic Operations in Relational Algebra**:

    - **Union (∪), Intersection (∩), Difference (−)**: These are set operations that operate on relations with the same schema.
      
    - **Selection (σ)**: Filters rows in a relation based on a specified condition.
      
    - **Projection (π)**: Selects specific columns from a relation, eliminating duplicates.
      
    - **Cartesian Product (×)**: Combines all rows from two relations, pairing each row of one relation with every row of the other.
      
    - **Join (⨝)**: Combines rows from two relations based on a related column between them.

2. **Extended Relational Algebra**:

    - **Theta-Join (⨝θ)**: A join that uses a general condition to combine rows.
      
    - **Natural Join (⨝)**: A special kind of join that automatically matches columns with the same name and eliminates redundant columns.
      
    - **Outer Joins (Left, Right, Full)**: Variants of join that include unmatched rows from one or both relations, padding with NULL values.

3. **Operations on Bags**:

    - Unlike sets, bags (or multisets) can contain duplicate tuples.
      
    - Relational algebra operations are adapted for bags, including bag union, bag intersection, and bag difference.

4. **Extended Operators**:

    - **Duplicate Elimination (δ)**: Removes duplicate tuples from a relation.
      
    - **Sorting (τ)**: Orders tuples in a relation based on specified attributes.
      
    - **Grouping and Aggregation (γ)**: Groups tuples and applies aggregate functions like SUM, AVG, COUNT, etc.

5. **Expression Trees and Complex Expressions**:

    - Relational algebra expressions can be represented as trees where leaves are operands and internal nodes are operators.
      
    - These trees help in understanding the flow of operations in a query.

---
### [WEEK 5 - SQL - Part 1](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Slides-Lectures/Week%205)

#### Key Topics and Concepts Covered:

1. **SQL as a Query Language**:

    - SQL is the standard language for querying and manipulating relational databases. It has several aspects, including Data Definition Language (DDL), Query Language (SELECT), and Data Manipulation Language (DML - INSERT, DELETE, UPDATE).

    - SQL allows users to describe what they want from the database, and the DBMS figures out how to execute the query efficiently.

2. **Basic SQL Query Structure**:

    - The basic form of an SQL query is the `SELECT-FROM-WHERE` structure:

      - `SELECT`: Specifies the attributes you want to retrieve.
      - `FROM`: Specifies the tables from which to retrieve the data.
      - `WHERE`: Specifies the conditions the data must meet.

3. **SQL vs. Relational Algebra**:

    - SQL queries can be represented using relational algebra, but SQL often uses "bag" semantics (allowing duplicates) as opposed to "set" semantics in relational algebra.

4. **The "SELECT" Clause**:

    - Specifies which attributes to project in the final result. It can include renaming of attributes, mathematical operations, and the use of functions like `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX`.

    - The `SELECT` clause can also handle single and multiple relation queries.

5. **Eliminating Duplicates**:

    - By default, SQL does not eliminate duplicates in query results. The keyword `DISTINCT` can be used to remove duplicates.

6. **Conditions in the "WHERE" Clause**:

    - The `WHERE` clause is used to specify conditions that rows must satisfy to be included in the result. This includes using comparison operators, pattern matching (LIKE), and dealing with NULL values.

7. **Set Operations**:

    - SQL supports set operations like `UNION`, `INTERSECT`, and `EXCEPT`, which can be used to combine results from multiple queries.

8. **Aggregation**:

    - SQL provides aggregation functions such as `MIN`, `MAX`, `SUM`, `COUNT`, and `AVG`, which can be used to perform calculations on a set of values.

9. **GROUP BY and HAVING Clauses**:

    - The `GROUP BY` clause is used to group rows that have the same values in specified columns, often used with aggregate functions.

    - The `HAVING` clause is used to filter groups based on aggregate conditions, similar to how the WHERE clause filters rows.

10. **Ordering Output**:

    - The `ORDER BY` clause is used to sort the result set by one or more columns. It can also handle NULL values explicitly using options like `NULLS FIRST` or `NULLS LAST`.


---
### [WEEK 6 - SQL - Part 2](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Slides-Lectures/Week%206)

#### Nested Queries
- Definition: Also called subqueries, these are queries embedded within an outer query, functioning similarly to function calls in programming languages.

- Usage: They can be used for conditions involving relations, such as IN, ALL, ANY, and EXISTS.

- Example: The document provides examples like finding employees in the same department as "Sally" or finding employees with the highest salary.

#### Subqueries Producing One Value
- Single-Value Subqueries: These subqueries return a single value, often used in comparisons within the main query.
  
- Example: Finding employees in a specific department where only one department matches the criteria.

#### Subqueries and Empty Relations
- EXISTS and NOT EXISTS: These operators are used to check whether a subquery returns any rows, which is useful for testing conditions related to the existence of data.
  
- Example: Finding employees who earn more than some managers by checking the existence of certain conditions.

#### Joins
- **Types of Joins**: The document explains various join operations, including:
    - **Inner Join**: Returns only the rows that match the search conditions.
      
    - **Natural Join**: A type of inner join that automatically matches columns with the same name.
      
    - **Outer Joins**: Includes Left, Right, and Full Outer Joins, which return matched rows plus unmatched rows from one or both sides of the join clause.
      
- Examples: The slides provide SQL code examples to illustrate how each type of join works.

#### Subqueries in the FROM Clause
- **Aggregation with Subqueries**: Subqueries can be used in the FROM clause to aggregate data before applying further conditions.
  
- Example: Finding departments with more than a certain number of employees or the department with the highest total salary.

#### Subquery Examples
- **Complex Queries**: The slides offer examples of more complex SQL queries, such as finding employees with salaries greater than the average, or suppliers who charge more than the average for specific parts.

---
### [WEEK 7 - Constrainsts & Triggers](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Slides-Lectures/Week%207)

1. **Database Modifications in SQL**
   
- INSERT, DELETE, UPDATE: These commands are used to modify the contents of a database.
  
    - `INSERT` adds new records.
    - `DELETE` removes records based on a condition.
    - `UPDATE` changes existing records.

2. **Constraints in SQL**
   
    - **Primary Keys and Unique Constraints**: Ensure that the data in a column is unique or that it can uniquely identify a row in the table.

    - **Foreign Key Constraints**: Enforces a link between two tables, ensuring that the value in a column corresponds to a value in another table.

    - **CHECK Constraints**: Used to limit the values that can be placed in a column.

    - **Assertions**: General constraints that can span across multiple tables and must always be true.

3. Triggers in SQL
    - **Event-Condition-Action (ECA) Model**: A trigger responds to specific events (INSERT, UPDATE, DELETE) by evaluating conditions and performing specified actions.

    - **Row-Level vs. Statement-Level Triggers**: Row-level triggers execute for each row affected by the event, while statement-level triggers execute once for the entire operation.

### Brief Explanation of Topics

- **Database Modifications**: This involves altering the data within tables using SQL commands like INSERT, DELETE, and UPDATE. These commands change the database state by adding, removing, or modifying records.

- **SQL Constraints**: Constraints are rules enforced on data columns to maintain the integrity and accuracy of the data. Primary keys, foreign keys, and CHECK constraints are fundamental tools to ensure that the database adheres to these rules.

- **Triggers**: Triggers are automated processes that occur when certain conditions in the database are met. They help enforce complex rules that can't be implemented with just constraints and are crucial for maintaining the integrity of database operations.

---
### [WEEK 8 - SQL Views](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Slides-Lectures/Week%208)

1. **SQL Views**:

    - **Three-Schema Architecture**: The slides introduce the concept of a three-schema architecture with physical, logical, and external levels. Views play a key role at the external level, allowing different applications or users to have tailored views of the data.

    - **Definition of Views**: A view in SQL is a virtual table based on the result set of a SQL query. Views can be either virtual (not stored physically) or materialized (physically stored in the database).

    - **Examples**: Several examples demonstrate creating views, such as a view for employees in the "Purchasing" department, showing their names, salaries, and managers. These views help simplify complex queries and enhance data independence.

    - **View Updates**: The slides discuss how views can be updated, which depends on certain conditions. Updatable views allow modifications, while others might require special handling, such as using triggers.

    - **Views for Data Independence**: Views can help maintain compatibility when database schemas change by recreating old schema structures from new ones.

2. **Indexes in SQL**:

    - **Purpose of Indexes**: Indexes are data structures that improve the speed of data retrieval operations on a database table at the cost of additional storage space and potentially slower writes.

    - **Creating Indexes**: The syntax for creating indexes in SQL is discussed, along with examples of creating indexes on one or multiple columns.

    - **Using Indexes**: The slides show how indexes can be used to optimize query performance by quickly locating the required rows, especially when dealing with large datasets.

    - **Database Tuning**: The importance of choosing the right indexes for database performance is emphasized, considering the trade-offs between faster read operations and slower write operations.

### Brief Explanation of the Topics:

- **SQL Views**: Views are an essential feature in SQL that allow the creation of virtual tables based on queries. They enable logical data independence, simplify complex queries, and enhance security by restricting access to specific data. There are two types of views: virtual and materialized. Virtual views are not stored in the database, while materialized views are stored physically and can be periodically refreshed.

- **Indexes in SQL**: Indexes are crucial for optimizing query performance. They act as pointers to data in a table, significantly speeding up data retrieval. However, they come with trade-offs, such as increased storage requirements and potentially slower write operations. Proper database tuning involves strategically creating and managing indexes to balance these factors.

---
### [WEEK 9 - Design Theory](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Slides-Lectures/Week%209)

#### Overview of Relational Design Theory:

- **Motivation & Overview**: The slides begin by discussing the importance of relational design theory, which helps in creating efficient and effective database schemas by eliminating redundancies and anomalies.

- **Functional Dependencies**: A key concept in database design, functional dependencies describe the relationship between attributes in a database. Understanding these dependencies is crucial for normalization.

- **Boyce-Codd Normal Form (BCNF)**: BCNF is a type of database normalization aimed at reducing redundancy and ensuring data integrity by organizing attributes into relations that follow specific rules.

- **Third Normal Form (3NF)**: The slides also touch upon 3NF, which is another form of database normalization that balances reducing redundancy with preserving functional dependencies.

#### Detailed Topics:

1. **Functional Dependencies**: The concept of functional dependencies is introduced as a fundamental element of database normalization. The slides explain how certain attributes (keys) can determine other attributes and how this understanding can help in designing a database schema that avoids redundancy and anomalies.

2. **Boyce-Codd Normal Form (BCNF)**: The material explains the conditions under which a database relation is considered to be in BCNF. This form of normalization is critical in reducing redundancy by ensuring that every non-trivial functional dependency involves a superkey.

3. **Third Normal Form (3NF)**: While BCNF is more stringent, 3NF is discussed as a compromise between reducing redundancy and preserving all functional dependencies. It allows some controlled redundancy but ensures that the schema is still efficient and maintains data integrity.

4. **Designing a Database Schema**: The slides walk through examples of how to design a database schema, starting from a "mega" relation and decomposing it into smaller, more manageable relations that follow normalization rules.

5. **Anomalies in Database Design**: Redundancy, update anomalies, and deletion anomalies are highlighted as problems that can occur in poorly designed schemas. The slides explain how to detect and avoid these issues through proper normalization.

6. **Schema Decomposition**: The process of decomposing a large relation into smaller relations to satisfy BCNF or 3NF is detailed. This includes algorithms and steps to ensure that the decomposition is both lossless (no data is lost) and dependency-preserving.

7. **Examples and Practice**: The slides provide multiple examples and practice problems that demonstrate how to apply the theory to real-world scenarios, such as decomposing a relation into BCNF and ensuring that the design is free of anomalies.

#### Summary:

- The overall goal of these slides is to equip students with the knowledge and tools to design robust database schemas that are normalized, reducing redundancy and avoiding anomalies. By understanding and applying concepts like functional dependencies, BCNF, and 3NF, students can create databases that are both efficient and reliable.


---
### [WEEK 10 - Storage & Indexing](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Slides-Lectures/Week%2010)


#### Key Topics Covered:

1. **DBMS Architecture Overview**:

    - The architecture of a DBMS is layered to manage various aspects of data processing, including query optimization, execution, access methods, buffer management, and disk space management. These layers must also consider concurrency control and recovery to ensure consistent and reliable operations.

2. **Data Storage**:

    - **File Management**: Data in a database is stored in files, which are collections of pages. Each page contains a number of records. The file management system must support operations like inserting, deleting, and modifying records, as well as fetching and scanning records.

    - **Page Formats**: Pages can store records in fixed-length or variable-length formats. Fixed-length records simplify space management, while variable-length records allow more flexible storage but require additional management overhead.

3. **File Organization**:

    - **Heap Files**: These are unordered collections of records. While simple to maintain, they can be inefficient for queries since they require scanning the entire file.

    - **Sorted Files**: These files are ordered based on a search key, making range queries efficient but increasing the complexity and cost of insertions and deletions.

    - **Indexes**: Indexes are data structures that provide fast access to records based on search keys. They can significantly speed up search queries and are typically implemented using tree structures or hashing techniques.

4. **Indexing**:

    - **Clustered vs. Unclustered Indexes**: A clustered index stores data in the same order as the index, making range queries very efficient. Unclustered indexes store data separately from the index, which may require additional I/O operations.

    - **B+ Trees**: A common type of index used in databases. B+ trees are balanced tree structures that store data entries in the leaf nodes, allowing efficient search, insert, and delete operations.

    - **Hash-Based Indexes**: These are best suited for equality searches. They distribute data across buckets based on a hash function, providing quick access but limited support for range queries.

5. **Cost Model for Analysis**:

    - The slides present a cost model that evaluates the performance of different file organizations and indexing strategies based on the number of disk I/O operations. This model helps in understanding the trade-offs between different storage and indexing methods.

6. **Choice of Indexes**:

    - Indexes should be chosen based on the workload of the database. The slides discuss strategies for selecting the right indexes, considering the nature of queries (e.g., range queries vs. equality searches) and the importance of clustering for performance.

#### Summary of Topics:
- **DBMS Architecture**: The architecture's role in managing data efficiently, ensuring concurrency, and supporting various query operations.

- **Data Storage**: How data is stored in files and pages, and the formats used to manage this data.

- **File Organization**: The different methods of organizing data in a database, including heap files, sorted files, and the use of indexes.

- **Indexing**: The types of indexes (clustered, unclustered, B+ trees, hash-based) and their impact on query performance.

- **Cost Analysis**: Evaluating the performance of storage and indexing strategies through disk I/O cost analysis.

- **Index Selection**: Guidelines for choosing the right indexes based on the database workload and query types.





























