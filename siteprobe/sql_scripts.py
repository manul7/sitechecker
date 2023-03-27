availability_table_script = """
-- Create the table for storing the content checks results
CREATE TABLE IF NOT EXISTS availability_checks (
    id SERIAL PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    response_time FLOAT NOT NULL,
    status_code INTEGER NOT NULL,
--    check_timestamp TIMESTAMP NOT NULL DEFAULT NOW()
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
"""

content_table_script = """
-- Create the table for storing the content checks results
CREATE TABLE IF NOT EXISTS content_checks (
    id SERIAL PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    regex_matched BOOLEAN NOT NULL,
--    regex_pattern VARCHAR(255) NOT NULL,
--    check_timestamp TIMESTAMP NOT NULL,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
"""

insert_availability_row = """
INSERT INTO availability_checks (url, response_time, status_code)
VALUES (%s, %s, %s);
"""

insert_content_row = """
INSERT INTO content_checks (url, regex_matched)
VALUES (%s, %s);
"""
