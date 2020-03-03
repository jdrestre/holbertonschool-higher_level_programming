-- Script that creates the table force_name on your MySQL server Database hbtn_0d_2.
CREATE TABLE IF NOT EXISTS unique_id (
       id    INT UNIQUE DEFAULT 1,
       name  VARCHAR(256)
);
