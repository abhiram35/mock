from app.database import SessionLocal
from app.models.topic import Topic
from app.models.question import Question
from app.enums.question_difficulty import QuestionDifficulty


TOPIC_NAME = "DBMS"


QUESTIONS = [
    # =========================================================
    # EASY — 20 QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "Difference between primary key and foreign key?"
        ),
        "expected_answer": (
            "A primary key uniquely identifies each row in a table and "
            "cannot be null or duplicated. A foreign key is a column in "
            "one table that references the primary key of another table, "
            "establishing a relationship between the two tables and "
            "enforcing referential integrity."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is normalization? Explain 1NF, 2NF, 3NF."
        ),
        "expected_answer": (
            "Normalization is the process of organizing a database to "
            "reduce redundancy and dependency. 1NF requires that each "
            "column contain only atomic (indivisible) values with no "
            "repeating groups. 2NF requires 1NF plus every non-key "
            "column must depend on the entire primary key, not just "
            "part of it. 3NF requires 2NF plus no non-key column "
            "should depend on another non-key column (no transitive "
            "dependencies)."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "Difference between DELETE, TRUNCATE, DROP?"
        ),
        "expected_answer": (
            "DELETE removes specific rows based on a WHERE clause and "
            "can be rolled back; it fires triggers. TRUNCATE removes "
            "all rows quickly without logging individual deletions and "
            "resets identity counters; it generally cannot be rolled "
            "back in most databases. DROP removes the entire table "
            "structure and its data from the database."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a JOIN? Types of joins in SQL?"
        ),
        "expected_answer": (
            "A JOIN combines rows from two or more tables based on a "
            "related column. The main types are INNER JOIN (returns "
            "only matching rows), LEFT JOIN (all rows from the left "
            "table plus matches), RIGHT JOIN (all rows from the right "
            "table plus matches), FULL OUTER JOIN (all rows from both "
            "tables), and CROSS JOIN (Cartesian product of both tables)."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "Difference between WHERE and HAVING?"
        ),
        "expected_answer": (
            "WHERE filters individual rows before any grouping takes "
            "place and cannot use aggregate functions. HAVING filters "
            "groups after GROUP BY has been applied and can use "
            "aggregate functions like COUNT, SUM, and AVG."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is an index, and why use one?"
        ),
        "expected_answer": (
            "An index is a data structure (typically a B-tree or "
            "hash table) that speeds up data retrieval by allowing "
            "the database to locate rows without scanning the entire "
            "table. Indexes improve read performance for queries with "
            "WHERE, JOIN, and ORDER BY clauses but add overhead to "
            "write operations because the index must be maintained."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "SQL vs NoSQL -- key differences?"
        ),
        "expected_answer": (
            "SQL databases are relational, use structured schemas and "
            "SQL for querying, and enforce ACID transactions. NoSQL "
            "databases are non-relational, support flexible or "
            "schema-less data models (document, key-value, column-family, "
            "graph), and often prioritize horizontal scalability and "
            "availability over strict consistency."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a candidate key vs a super key?"
        ),
        "expected_answer": (
            "A super key is any set of one or more columns that can "
            "uniquely identify a row in a table. A candidate key is a "
            "minimal super key, meaning no subset of it can still "
            "uniquely identify rows. The primary key is chosen from "
            "among the candidate keys."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a composite key?"
        ),
        "expected_answer": (
            "A composite key is a primary key or candidate key that "
            "consists of two or more columns. Together, the combination "
            "of those columns uniquely identifies each row, even though "
            "individually none of them may be unique."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between UNION and UNION ALL?"
        ),
        "expected_answer": (
            "UNION combines the result sets of two SELECT statements "
            "and removes duplicate rows. UNION ALL combines the result "
            "sets without removing duplicates, making it faster because "
            "it skips the deduplication step."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a view in SQL?"
        ),
        "expected_answer": (
            "A view is a virtual table defined by a stored SELECT "
            "query. It does not store data itself but dynamically "
            "retrieves data from the underlying tables when queried. "
            "Views simplify complex queries, provide a layer of "
            "abstraction, and can restrict access to specific columns "
            "or rows."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a schema in a database?"
        ),
        "expected_answer": (
            "A schema is the overall logical structure or blueprint "
            "of a database. It defines the tables, columns, data types, "
            "relationships, constraints, indexes, and other objects "
            "that make up the database's organization."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between CHAR and VARCHAR?"
        ),
        "expected_answer": (
            "CHAR is a fixed-length string type that pads shorter "
            "values with spaces to fill the declared length. VARCHAR "
            "is a variable-length string type that stores only the "
            "actual characters plus a small length prefix, using less "
            "storage for strings shorter than the maximum length."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a constraint (NOT NULL, UNIQUE, CHECK)?"
        ),
        "expected_answer": (
            "A constraint is a rule enforced by the database to "
            "maintain data integrity. NOT NULL prevents a column from "
            "containing null values. UNIQUE ensures all values in a "
            "column or set of columns are distinct. CHECK validates "
            "that values satisfy a specified Boolean condition before "
            "allowing insertion or update."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between DDL, DML, DCL, "
            "and TCL commands?"
        ),
        "expected_answer": (
            "DDL (Data Definition Language) defines structure: CREATE, "
            "ALTER, DROP. DML (Data Manipulation Language) manipulates "
            "data: SELECT, INSERT, UPDATE, DELETE. DCL (Data Control "
            "Language) manages permissions: GRANT, REVOKE. TCL "
            "(Transaction Control Language) manages transactions: "
            "COMMIT, ROLLBACK, SAVEPOINT."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is an aggregate function? Give examples."
        ),
        "expected_answer": (
            "An aggregate function performs a calculation on a set of "
            "values and returns a single result. Common examples "
            "include COUNT (number of rows), SUM (total of numeric "
            "values), AVG (average), MIN (smallest value), and MAX "
            "(largest value). They are typically used with GROUP BY."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is a subquery?"
        ),
        "expected_answer": (
            "A subquery is a SELECT statement nested inside another "
            "SQL statement, such as within a WHERE, FROM, or SELECT "
            "clause. It executes first and its result is used by the "
            "outer query. Subqueries can return a single value, a "
            "single column, or a full result set."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the difference between a database and a DBMS?"
        ),
        "expected_answer": (
            "A database is an organized collection of data stored "
            "electronically. A DBMS (Database Management System) is "
            "the software that manages, stores, retrieves, and secures "
            "that data. The DBMS provides interfaces for users and "
            "applications to interact with the database."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is referential integrity?"
        ),
        "expected_answer": (
            "Referential integrity is a constraint ensuring that a "
            "foreign key value in one table always refers to an "
            "existing primary key value in the referenced table. It "
            "prevents orphaned rows and maintains consistent "
            "relationships between tables."
        ),
    },
    {
        "difficulty": QuestionDifficulty.EASY,
        "question_text": (
            "What is the purpose of the GROUP BY clause?"
        ),
        "expected_answer": (
            "GROUP BY groups rows that share the same values in "
            "specified columns into summary rows. It is used with "
            "aggregate functions like COUNT, SUM, and AVG to produce "
            "results per group rather than per individual row."
        ),
    },

    # =========================================================
    # MEDIUM — 20 QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain ACID properties with an example transaction."
        ),
        "expected_answer": (
            "ACID stands for Atomicity (a transaction is all-or-nothing), "
            "Consistency (the database moves from one valid state to "
            "another), Isolation (concurrent transactions do not "
            "interfere with each other), and Durability (committed data "
            "survives system failures). For example, a bank transfer "
            "debits one account and credits another; atomicity ensures "
            "both operations succeed or both are rolled back."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "When would you denormalize a schema?"
        ),
        "expected_answer": (
            "Denormalization is appropriate when read performance is "
            "more critical than write efficiency, such as in reporting "
            "or analytics systems with heavy aggregation queries. By "
            "storing precomputed or redundant data, you reduce the "
            "number of joins needed at query time. The trade-off is "
            "increased storage and the need to keep redundant data "
            "consistent during writes."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Clustered vs non-clustered index -- what's the difference?"
        ),
        "expected_answer": (
            "A clustered index determines the physical order of data "
            "in the table; there can be only one per table, and it is "
            "usually created on the primary key. A non-clustered index "
            "maintains a separate structure with pointers back to the "
            "actual data rows; a table can have many non-clustered "
            "indexes. Clustered index scans are fast for range queries "
            "because rows are physically adjacent."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain SQL transaction isolation levels."
        ),
        "expected_answer": (
            "SQL defines four isolation levels. Read Uncommitted allows "
            "dirty reads. Read Committed prevents dirty reads but "
            "allows non-repeatable reads. Repeatable Read prevents "
            "dirty and non-repeatable reads but allows phantom reads. "
            "Serializable prevents all three anomalies by fully "
            "isolating transactions, but at the cost of reduced "
            "concurrency. Higher isolation provides more correctness "
            "but more contention."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is a database deadlock, and how is it resolved?"
        ),
        "expected_answer": (
            "A database deadlock occurs when two or more transactions "
            "each hold locks that the other needs, forming a cycle "
            "so none can proceed. The DBMS detects deadlocks using a "
            "wait-for graph and resolves them by rolling back one of "
            "the transactions (the victim). Prevention strategies "
            "include acquiring locks in a consistent order and keeping "
            "transactions short."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain INNER, LEFT, RIGHT, and FULL OUTER joins "
            "with examples."
        ),
        "expected_answer": (
            "INNER JOIN returns only rows where a match exists in both "
            "tables. LEFT JOIN returns all rows from the left table and "
            "matched rows from the right, with NULLs where there is no "
            "match. RIGHT JOIN is the mirror of LEFT JOIN. FULL OUTER "
            "JOIN returns all rows from both tables, filling NULLs on "
            "either side where there is no match. The choice depends on "
            "whether you need unmatched rows from one or both sides."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What are stored procedures and triggers -- "
            "pros and cons?"
        ),
        "expected_answer": (
            "A stored procedure is a precompiled block of SQL logic "
            "stored in the database and invoked by name. A trigger is "
            "a stored procedure that fires automatically in response "
            "to INSERT, UPDATE, or DELETE events on a table. Pros "
            "include encapsulating business logic, reducing network "
            "round trips, and enforcing rules at the database layer. "
            "Cons include harder debugging, tight coupling to the "
            "database vendor, and potential performance issues if "
            "overused."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain normalization vs denormalization trade-offs "
            "in a reporting system."
        ),
        "expected_answer": (
            "A normalized schema reduces redundancy and keeps writes "
            "clean, but reporting queries often require many joins "
            "across tables, which is slow on large datasets. A "
            "denormalized schema precomputes aggregates or flattens "
            "relationships, making reads faster at the cost of more "
            "complex writes and potential data inconsistency. Reporting "
            "systems commonly use star or snowflake schemas that are "
            "partially denormalized."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is a correlated subquery vs a regular subquery?"
        ),
        "expected_answer": (
            "A regular subquery is independent; it executes once and "
            "its result is used by the outer query. A correlated "
            "subquery references columns from the outer query and "
            "is re-executed for each row processed by the outer query. "
            "Correlated subqueries can be less efficient because of "
            "repeated execution, but they are useful for row-by-row "
            "comparisons."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain the difference between EXISTS and IN."
        ),
        "expected_answer": (
            "IN checks whether a value matches any value in a list or "
            "subquery result set. EXISTS checks whether a subquery "
            "returns at least one row and short-circuits as soon as a "
            "match is found. EXISTS often performs better for large "
            "subquery results because it stops early, while IN can be "
            "faster for small result sets. EXISTS also handles NULLs "
            "more predictably."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is database replication, and what are its "
            "common types?"
        ),
        "expected_answer": (
            "Database replication copies data from one database server "
            "to one or more replicas to improve availability, fault "
            "tolerance, and read scalability. Common types include "
            "synchronous replication (all replicas confirm writes "
            "before commit), asynchronous replication (replicas receive "
            "changes after commit with some lag), and semi-synchronous "
            "replication (at least one replica confirms)."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain optimistic vs pessimistic concurrency control."
        ),
        "expected_answer": (
            "Pessimistic concurrency control locks resources before "
            "accessing them, preventing other transactions from "
            "modifying the data until the lock is released. Optimistic "
            "concurrency control allows transactions to proceed without "
            "locks and checks for conflicts at commit time, typically "
            "using version numbers or timestamps. Optimistic is better "
            "when conflicts are rare; pessimistic is safer under high "
            "contention."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is a covering index, and how does it improve "
            "performance?"
        ),
        "expected_answer": (
            "A covering index includes all the columns needed to "
            "satisfy a query, so the database can answer the query "
            "entirely from the index without accessing the base table "
            "rows. This eliminates random I/O lookups to the table and "
            "can dramatically speed up read-heavy queries. The trade-off "
            "is a larger index that consumes more storage and slows "
            "writes."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain how foreign key constraints affect "
            "INSERT/DELETE performance."
        ),
        "expected_answer": (
            "On INSERT, the database must verify that the referenced "
            "primary key exists in the parent table, adding a lookup "
            "per row. On DELETE from the parent table, the database "
            "must check for or cascade to dependent rows in child "
            "tables. These checks require index lookups and can slow "
            "bulk operations. In high-throughput scenarios, some teams "
            "defer or disable foreign key checks during batch loads "
            "and re-enable them afterward."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is database partitioning, and when should you use it?"
        ),
        "expected_answer": (
            "Database partitioning divides a large table into smaller "
            "physical segments (partitions) based on a key, such as "
            "date ranges (range partitioning), hash values (hash "
            "partitioning), or explicit lists (list partitioning). "
            "Partitioning improves query performance by enabling "
            "partition pruning, simplifies maintenance tasks like "
            "archiving old data, and is useful when tables grow to "
            "billions of rows."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain the N+1 query problem and how to avoid it."
        ),
        "expected_answer": (
            "The N+1 problem occurs when an application executes one "
            "query to retrieve a list of N records and then issues a "
            "separate query for each record to fetch related data, "
            "resulting in N+1 total queries. It is avoided by using "
            "eager loading (JOIN or subquery) to fetch related data in "
            "a single query, or by using batch loading where the ORM "
            "fetches related records in groups."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is the difference between OLTP and OLAP systems?"
        ),
        "expected_answer": (
            "OLTP (Online Transaction Processing) handles high volumes "
            "of short, real-time transactions like inserts and updates "
            "and is optimized for write throughput with normalized "
            "schemas. OLAP (Online Analytical Processing) handles "
            "complex analytical queries on large datasets and is "
            "optimized for read performance, often using denormalized "
            "star or snowflake schemas and columnar storage."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "How would you design indexes for a table with "
            "frequent range queries?"
        ),
        "expected_answer": (
            "Use a B-tree index on the columns used in range "
            "predicates (e.g. date ranges, numeric ranges), because "
            "B-trees support efficient range scans of sorted data. "
            "Place the range column last in a composite index after "
            "equality columns. Consider a clustered index on the "
            "range column if most queries filter by it. If multiple "
            "range columns are queried independently, separate indexes "
            "or partial indexes may be more effective."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "Explain database connection pooling and why it matters."
        ),
        "expected_answer": (
            "Connection pooling maintains a cache of reusable database "
            "connections rather than opening and closing a new "
            "connection for every request. Establishing a connection "
            "is expensive (TCP handshake, authentication, memory "
            "allocation), so pooling amortizes that cost. Pool settings "
            "like minimum/maximum size and idle timeout must be tuned "
            "to match the application's concurrency level."
        ),
    },
    {
        "difficulty": QuestionDifficulty.MEDIUM,
        "question_text": (
            "What is a materialized view, and how does it differ "
            "from a regular view?"
        ),
        "expected_answer": (
            "A regular view is a stored query that is executed every "
            "time it is referenced, with no persistent data of its own. "
            "A materialized view stores the precomputed query result "
            "physically on disk, making reads much faster but requiring "
            "periodic refresh to stay in sync with the base tables. "
            "Materialized views are useful for expensive aggregation "
            "or join queries that do not need real-time accuracy."
        ),
    },

    # =========================================================
    # HARD — 20 QUESTIONS
    # =========================================================

    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how a B+ Tree index works internally."
        ),
        "expected_answer": (
            "A B+ Tree is a self-balancing tree where all values are "
            "stored in the leaf nodes, and internal nodes contain only "
            "keys used for routing. Leaf nodes are linked together in "
            "a doubly-linked list, enabling efficient sequential range "
            "scans. Insertions and deletions maintain balance by "
            "splitting or merging nodes, keeping the tree height "
            "logarithmic. This structure ensures that lookups, "
            "insertions, and range queries all operate in O(log n) "
            "I/O operations."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain the CAP theorem with a distributed "
            "database example."
        ),
        "expected_answer": (
            "The CAP theorem states that a distributed system can "
            "guarantee at most two of three properties simultaneously: "
            "Consistency (every read returns the latest write), "
            "Availability (every request receives a response), and "
            "Partition tolerance (the system continues operating despite "
            "network splits). For example, during a network partition, "
            "a CP system like ZooKeeper may reject requests to maintain "
            "consistency, while an AP system like Cassandra continues "
            "serving potentially stale data to remain available."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain MVCC and how PostgreSQL uses it."
        ),
        "expected_answer": (
            "Multi-Version Concurrency Control (MVCC) allows multiple "
            "transactions to read and write concurrently without "
            "blocking each other by maintaining multiple versions of "
            "each row. PostgreSQL assigns each transaction an XID; "
            "when a row is updated, a new version is created with the "
            "new XID, and the old version remains visible to "
            "transactions that started earlier. A VACUUM process later "
            "reclaims dead row versions. This avoids read locks "
            "entirely but requires careful management of bloat."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Design a schema for a high-traffic e-commerce "
            "order system."
        ),
        "expected_answer": (
            "Core tables include users, products, orders, and "
            "order_items. The orders table holds order metadata (user "
            "reference, status, timestamps, total amount), while "
            "order_items captures each line item (product reference, "
            "quantity, unit price at purchase time). Indexes on "
            "user_id and created_at support common lookups. Separating "
            "the current price from the historical price-at-purchase "
            "prevents data corruption. For high traffic, partitioning "
            "orders by date, using read replicas for reporting, and "
            "caching product details are common scaling strategies."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain query execution plans and cost-based "
            "optimization."
        ),
        "expected_answer": (
            "A query execution plan is the sequence of physical "
            "operations (scans, joins, sorts, aggregations) the "
            "database chooses to execute a query. The cost-based "
            "optimizer evaluates multiple candidate plans by estimating "
            "the cost of each (based on table statistics like row "
            "counts, data distribution, and index selectivity) and "
            "selects the plan with the lowest estimated cost. EXPLAIN "
            "or EXPLAIN ANALYZE exposes the chosen plan and actual "
            "runtime statistics for tuning."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Sharding vs replication -- how do they solve "
            "different problems?"
        ),
        "expected_answer": (
            "Replication copies the entire dataset to multiple nodes "
            "to improve read scalability and fault tolerance but does "
            "not increase write capacity because every replica must "
            "apply every write. Sharding horizontally partitions data "
            "across nodes by a shard key so that each node holds a "
            "subset of the data, increasing both read and write "
            "capacity. Sharding adds complexity around cross-shard "
            "queries, rebalancing, and transactions. Most large systems "
            "use both: shard for scale and replicate each shard for "
            "availability."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you design a database for a multi-tenant "
            "SaaS application?"
        ),
        "expected_answer": (
            "Three main approaches exist. Shared database with a "
            "tenant_id column in every table is simplest and most "
            "cost-efficient but requires row-level security and careful "
            "index design. Schema-per-tenant uses separate schemas "
            "within one database, providing better isolation with "
            "moderate overhead. Database-per-tenant gives the strongest "
            "isolation and simplest backup and restore but is the most "
            "expensive to operate. The choice depends on the number of "
            "tenants, isolation requirements, and regulatory constraints."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain write-ahead logging (WAL) and crash recovery."
        ),
        "expected_answer": (
            "Write-ahead logging writes all changes to a sequential "
            "log file before they are applied to the actual data pages. "
            "If the system crashes, the WAL is replayed on recovery: "
            "committed transactions whose changes were not yet flushed "
            "to data files are redone, and uncommitted transactions are "
            "rolled back. This guarantees durability (the D in ACID) "
            "without requiring expensive synchronous writes to data "
            "pages on every commit."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How do distributed transactions work "
            "(2PC, Saga pattern)?"
        ),
        "expected_answer": (
            "Two-Phase Commit (2PC) uses a coordinator that first asks "
            "all participants to prepare (vote yes/no) and then issues "
            "a global commit or abort. 2PC guarantees atomicity but "
            "blocks participants if the coordinator fails. The Saga "
            "pattern breaks a distributed transaction into a sequence "
            "of local transactions, each with a compensating action "
            "that undoes its effect if a later step fails. Sagas avoid "
            "blocking but provide eventual consistency rather than "
            "strict atomicity."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how a database handles phantom reads and "
            "how serializable isolation prevents them."
        ),
        "expected_answer": (
            "A phantom read occurs when a transaction re-executes a "
            "query and finds new rows that were inserted by another "
            "committed transaction. Serializable isolation prevents "
            "phantoms by using techniques such as predicate locking or "
            "index-range (gap) locking, which lock not just existing "
            "rows but also the ranges between index values, blocking "
            "inserts that would satisfy the query's predicate. In "
            "MVCC-based systems, serializable may instead use "
            "serializable snapshot isolation (SSI) to detect and abort "
            "transactions involved in dangerous read-write dependencies."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Design a rate-limited, idempotent payments table schema."
        ),
        "expected_answer": (
            "The payments table includes an idempotency_key column "
            "with a UNIQUE constraint so duplicate submissions with "
            "the same key are rejected or return the existing result. "
            "Columns include user_id, amount, currency, status "
            "(pending, completed, failed), created_at, and updated_at. "
            "A rate_limit_window table or token-bucket metadata tracks "
            "per-user request counts within a time window. On each "
            "request, the application checks the idempotency key first, "
            "then verifies the rate limit before creating or updating "
            "the payment record."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain the trade-offs between eventual consistency "
            "and strong consistency in NoSQL."
        ),
        "expected_answer": (
            "Strong consistency ensures every read returns the latest "
            "write, simplifying application logic but requiring "
            "coordination across nodes (quorum writes/reads or leader "
            "forwarding), which increases latency and reduces "
            "availability during partitions. Eventual consistency "
            "allows replicas to diverge temporarily, providing lower "
            "latency and higher availability but requiring the "
            "application to handle stale reads, conflict resolution, "
            "and potential data divergence."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you migrate a large production table "
            "with zero downtime?"
        ),
        "expected_answer": (
            "A common approach is the expand-contract pattern. First, "
            "add the new column or table alongside the old one (expand). "
            "Backfill existing data in batches with rate limiting to "
            "avoid locking or overloading the database. Dual-write to "
            "both old and new structures during the migration. Once "
            "backfill completes and the new structure is verified, "
            "switch reads to the new structure. Finally, remove the "
            "old structure (contract). Tools like pt-online-schema-change "
            "or gh-ost automate this for MySQL."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how consistent hashing is used for "
            "database sharding."
        ),
        "expected_answer": (
            "Consistent hashing maps both shard nodes and data keys "
            "onto a hash ring. Each key is assigned to the first node "
            "encountered clockwise on the ring. When a node is added "
            "or removed, only the keys between the new node and its "
            "predecessor need to be remapped, minimizing data movement. "
            "Virtual nodes (multiple hash positions per physical node) "
            "improve balance. This contrasts with modular hashing, "
            "where adding a node reshuffles nearly all key assignments."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "What is a leader-follower replication lag issue, "
            "and how do you mitigate it?"
        ),
        "expected_answer": (
            "Replication lag is the delay between a write being applied "
            "on the leader and becoming visible on a follower. It "
            "causes stale reads when applications read from followers "
            "immediately after writing. Mitigation strategies include "
            "reading from the leader after a write (read-your-writes "
            "consistency), using semi-synchronous replication so at "
            "least one follower is always caught up, monitoring lag "
            "metrics and routing reads to up-to-date replicas, or "
            "using session-sticky routing."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how you'd design a database to support "
            "full-text search at scale."
        ),
        "expected_answer": (
            "For small to moderate scale, built-in features like "
            "PostgreSQL's tsvector/tsquery with GIN indexes work well. "
            "At large scale, an inverted index engine like Elasticsearch "
            "is typically used alongside the primary database. Data is "
            "synced to the search index via change data capture or "
            "event-driven pipelines. The search index tokenizes, stems, "
            "and scores documents for relevance. The trade-off is "
            "maintaining consistency between the primary store and "
            "the search index."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "What is the difference between a data warehouse "
            "and a data lake?"
        ),
        "expected_answer": (
            "A data warehouse stores structured, schema-on-write data "
            "that has been cleaned and transformed (ETL) for analytical "
            "queries, typically using columnar storage. A data lake "
            "stores raw data in its native format (structured, "
            "semi-structured, or unstructured) using schema-on-read, "
            "offering more flexibility but requiring consumers to "
            "handle data quality. Modern lakehouses combine both "
            "approaches with open table formats like Delta Lake or "
            "Apache Iceberg."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how vector clocks or version vectors help "
            "resolve conflicts in distributed data stores."
        ),
        "expected_answer": (
            "A vector clock is a list of (node, counter) pairs "
            "attached to each data item. Each node increments its own "
            "counter on every update. By comparing vector clocks, the "
            "system can determine causal ordering: if one clock "
            "dominates another, the update is a clear successor. If "
            "neither dominates, the updates are concurrent and a "
            "conflict exists. The application or system then resolves "
            "the conflict using a strategy like last-writer-wins, "
            "merge functions, or CRDTs."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "How would you design an audit-log/event-sourcing "
            "system on top of a relational database?"
        ),
        "expected_answer": (
            "Create an append-only events table with columns for "
            "event_id, aggregate_type, aggregate_id, event_type, "
            "payload (JSONB), timestamp, and actor_id. Every state "
            "change is recorded as a new event rather than an in-place "
            "update. Current state is derived by replaying events or "
            "maintained in a separate materialized projection table. "
            "Indexes on aggregate_id and timestamp support efficient "
            "retrieval. Partitioning by time keeps the table manageable. "
            "Snapshots can be stored periodically to avoid replaying "
            "the full event history."
        ),
    },
    {
        "difficulty": QuestionDifficulty.HARD,
        "question_text": (
            "Explain how connection pool exhaustion can cascade "
            "into a system-wide outage, and how you'd prevent it."
        ),
        "expected_answer": (
            "When a slow query or downstream service causes connections "
            "to be held longer than usual, the pool fills up. New "
            "requests block waiting for a connection, causing thread "
            "exhaustion and request timeouts that cascade to upstream "
            "services. Prevention includes setting aggressive connection "
            "and query timeouts, using circuit breakers to fail fast "
            "when the database is slow, monitoring pool utilization "
            "with alerts, sizing the pool to match the application's "
            "maximum concurrency, and isolating critical from "
            "non-critical workloads with separate pools."
        ),
    },
]


def seed_dbms_questions() -> None:
    db = SessionLocal()

    try:
        topic = (
            db.query(Topic)
            .filter(Topic.name == TOPIC_NAME)
            .first()
        )

        if not topic:
            topic = Topic(
                name=TOPIC_NAME,
                description=(
                    "Database Management Systems interview "
                    "questions covering fundamentals, "
                    "intermediate concepts, and advanced topics."
                ),
                is_active=True,
            )

            db.add(topic)
            db.commit()
            db.refresh(topic)

            print(
                f"Created topic: {topic.name} "
                f"(ID: {topic.id})"
            )

        else:
            print(
                f"Using existing topic: {topic.name} "
                f"(ID: {topic.id})"
            )

        existing_count = (
            db.query(Question)
            .filter(Question.topic_id == topic.id)
            .count()
        )

        if existing_count >= len(QUESTIONS):
            print(
                f"DBMS topic already contains "
                f"{existing_count} question(s)."
            )
            print(
                "No questions were inserted to avoid duplicates."
            )
            return

        questions = [
            Question(
                topic_id=topic.id,
                difficulty=item["difficulty"],
                question_text=item["question_text"],
                expected_answer=item["expected_answer"],
            )
            for item in QUESTIONS
        ]

        db.add_all(questions)
        db.commit()

        print()
        print("=" * 60)
        print("DBMS INTERVIEW QUESTION BANK CREATED")
        print("=" * 60)
        print(f"Topic ID       : {topic.id}")
        print(f"Topic          : {topic.name}")
        print(f"Total questions: {len(questions)}")
        print(
            "Easy           : "
            f"{sum(1 for q in questions if q.difficulty == QuestionDifficulty.EASY)}"
        )
        print(
            "Medium         : "
            f"{sum(1 for q in questions if q.difficulty == QuestionDifficulty.MEDIUM)}"
        )
        print(
            "Hard           : "
            f"{sum(1 for q in questions if q.difficulty == QuestionDifficulty.HARD)}"
        )
        print("=" * 60)

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_dbms_questions()
