CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE CHECK(length(username) >= 5 AND username LIKE '%.%'),
    password TEXT NOT NULL CHECK(length(password) >= 8),
    email TEXT UNIQUE CHECK(email LIKE '%@%.com'),
    role TEXT NOT NULL CHECK(role IN ('admin','professor','student')),
    last_login_timestamp DATETIME,
    avatar_path TEXT,
    nickname TEXT,
    first_name TEXT,
    last_name TEXT
);

CREATE TABLE IF NOT EXISTS computer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tag_name TEXT NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('ON', 'OFF', 'EXM', 'WAI', 'WRN', 'MIS')),
    location TEXT NOT NULL CHECK(location LIKE '%.%'),
    branch TEXT,
    ip TEXT CHECK(ip LIKE '%.%.%.%'),
    serial_number TEXT UNIQUE,
    last_maintenance_date DATETIME,
    last_login_timestamp DATETIME,

    UNIQUE(tag_name, location),  -- Restricción para tag_name único por location
    UNIQUE(ip, location),        -- Restricción para ip único por location
    FOREIGN KEY(location) REFERENCES computers(location)  -- Restricción para asegurar que la location exista en la misma tabla
);

CREATE TABLE IF NOT EXISTS access (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES user(id),
    computer_id INTEGER REFERENCES computer(id),
    login_timestamp DATETIME,
    logout_timestamp DATETIME
);
