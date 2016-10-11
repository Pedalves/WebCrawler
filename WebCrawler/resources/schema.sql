----------------------------------
-- Web Crawler
----------------------------------

CREATE TABLE IF NOT EXISTS url(
    url_input      TEXT    PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS site(
    url_input   TEXT,
    site_name   TEXT,
    content     TEXT    DEFAULT NULL,
    parent      TEXT    DEFAULT NULL,
    PRIMARY KEY(url_input, site_name) ON CONFLICT REPLACE,
    FOREIGN KEY(url_input) REFERENCES url(url_input) ON DELETE CASCADE
);

