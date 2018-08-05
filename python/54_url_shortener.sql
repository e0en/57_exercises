DROP TABLE IF EXISTS urls;
DROP TABLE IF EXISTS logs;
CREATE TABLE urls (url TEXT, short_id TEXT);
CREATE TABLE logs (short_id TEXT, host_json TEXT, created_at REAL);
