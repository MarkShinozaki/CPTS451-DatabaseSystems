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

1. Basic Operations in Relational Algebra:

    - Union (∪), Intersection (∩), Difference (−): These are set operations that operate on relations with the same schema.
    - Selection (σ): Filters rows in a relation based on a specified condition.
    - Projection (π): Selects specific columns from a relation, eliminating duplicates.
    - Cartesian Product (×): Combines all rows from two relations, pairing each row of one relation with every row of the other.
    - Join (⨝): Combines rows from two relations based on a related column between them.

2. Extended Relational Algebra:

    - Theta-Join (⨝θ): A join that uses a general condition to combine rows.
    - Natural Join (⨝): A special kind of join that automatically matches columns with the same name and eliminates redundant columns.
    - Outer Joins (Left, Right, Full): Variants of join that include unmatched rows from one or both relations, padding with NULL values.

3. Operations on Bags:

    - Unlike sets, bags (or multisets) can contain duplicate tuples.
    - Relational algebra operations are adapted for bags, including bag union, bag intersection, and bag difference.

4. Extended Operators:

    - Duplicate Elimination (δ): Removes duplicate tuples from a relation.
    - Sorting (τ): Orders tuples in a relation based on specified attributes.
    - Grouping and Aggregation (γ): Groups tuples and applies aggregate functions like SUM, AVG, COUNT, etc.

5. Expression Trees and Complex Expressions:

    - Relational algebra expressions can be represented as trees where leaves are operands and internal nodes are operators.
    - These trees help in understanding the flow of operations in a query.

---
### [WEEK 5 - SQL - Part 1](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Slides-Lectures/Week%205)

#### Key Topics and Concepts Covered:

1. SQL as a Query Language:

    - SQL is the standard language for querying and manipulating relational databases. It has several aspects, including Data Definition Language (DDL), Query Language (SELECT), and Data Manipulation Language (DML - INSERT, DELETE, UPDATE).

    - SQL allows users to describe what they want from the database, and the DBMS figures out how to execute the query efficiently.

2. Basic SQL Query Structure:

    - The basic form of an SQL query is the `SELECT-FROM-WHERE` structure:

      - `SELECT`: Specifies the attributes you want to retrieve.
      - `FROM`: Specifies the tables from which to retrieve the data.
      - `WHERE`: Specifies the conditions the data must meet.

3. SQL vs. Relational Algebra:

    - SQL queries can be represented using relational algebra, but SQL often uses "bag" semantics (allowing duplicates) as opposed to "set" semantics in relational algebra.

4. The "SELECT" Clause:

    - Specifies which attributes to project in the final result. It can include renaming of attributes, mathematical operations, and the use of functions like `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX`.

    - The `SELECT` clause can also handle single and multiple relation queries.

5. Eliminating Duplicates:

    - By default, SQL does not eliminate duplicates in query results. The keyword `DISTINCT` can be used to remove duplicates.

6. Conditions in the "WHERE" Clause:

    - The `WHERE` clause is used to specify conditions that rows must satisfy to be included in the result. This includes using comparison operators, pattern matching (LIKE), and dealing with NULL values.

7. Set Operations:

    - SQL supports set operations like `UNION`, `INTERSECT`, and `EXCEPT`, which can be used to combine results from multiple queries.

8. Aggregation:

    - SQL provides aggregation functions such as `MIN`, `MAX`, `SUM`, `COUNT`, and `AVG`, which can be used to perform calculations on a set of values.

9. GROUP BY and HAVING Clauses:

    - The `GROUP BY` clause is used to group rows that have the same values in specified columns, often used with aggregate functions.

    - The `HAVING` clause is used to filter groups based on aggregate conditions, similar to how the WHERE clause filters rows.

10. Ordering Output:

    - The `ORDER BY` clause is used to sort the result set by one or more columns. It can also handle NULL values explicitly using options like `NULLS FIRST` or `NULLS LAST`.









---
### [WEEK 6](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Slides-Lectures/Week%206)


---
### [WEEK 7](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Slides-Lectures/Week%207)

---
### [WEEK 8](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Slides-Lectures/Week%208)


---
### [WEEK 9](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Slides-Lectures/Week%209)


---
### [WEEK 10](https://github.com/MarkShinozaki/CPTS451-DatabaseSystems/tree/Slides-Lectures/Week%2010)
