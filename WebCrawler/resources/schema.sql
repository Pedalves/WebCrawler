----------------------------------
-- Web Crawler
----------------------------------

CREATE TABLE IF NOT EXISTS site(
    site_name   TEXT    PRIMARY KEY,
    content     TEXT    DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS parent_site(
    site_name   TEXT    PRIMARY KEY,
    parent      TEXT    PRIMARY KEY,
    content     TEXT    DEFAULT NULL,
    FOREIGN KEY (parent) REFERENCES site(site_name) ON DELETE CASCADE
);