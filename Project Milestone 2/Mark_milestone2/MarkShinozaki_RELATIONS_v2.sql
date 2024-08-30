-- MarkShinozaki_RELATIONS_v2.sql

CREATE TABLE business (
    business_id VARCHAR PRIMARY KEY,
    name VARCHAR,
    address VARCHAR,
    state VARCHAR,
    city VARCHAR,
    zipcode VARCHAR,
    latitude FLOAT,
    longitude FLOAT,
    stars FLOAT,
    reviewcount INT DEFAULT 0,
    numcheckins INT DEFAULT 0,
    openstatus BOOLEAN,
    reviewrating FLOAT DEFAULT 0.0
);

CREATE TABLE reviewtable (
    review_id VARCHAR PRIMARY KEY,
    user_id VARCHAR,
    business_id VARCHAR REFERENCES business(business_id),
    stars INT,
    date DATE,
    text TEXT,
    useful INT,
    funny INT,
    cool INT
);

CREATE TABLE usertable (
    user_id VARCHAR PRIMARY KEY,
    name VARCHAR,
    yelping_since DATE,
    review_count INT,
    fans INT,
    average_stars FLOAT,
    funny INT,
    useful INT,
    cool INT
);

CREATE TABLE checkintable (
    business_id VARCHAR REFERENCES business(business_id),
    dayofweek VARCHAR,
    hour VARCHAR,
    count INT,
    PRIMARY KEY (business_id, dayofweek, hour)
);
