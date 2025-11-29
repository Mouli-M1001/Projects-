create schema hotel;
use hotel;



CREATE TABLE restaurant_reservations (
  reservation_id INT UNSIGNED NOT NULL AUTO_INCREMENT,    -- (2) auto-increment ID
  customer_name VARCHAR(100) NOT NULL,                    -- (3) required, min 3 chars checked below
  guests TINYINT UNSIGNED NOT NULL,                       -- (4) 1..20 enforced by CHECK
  reservation_datetime DATETIME NOT NULL,                 -- (5) mandatory date + time
  contact_number BIGINT UNSIGNED NOT NULL,                -- (6) exactly 10 digits, starts 6-9 (enforced by CHECK using numeric range)
  special_occasion BOOLEAN NOT NULL DEFAULT FALSE,        -- (7) Yes/No (true/false), default No
  table_number TINYINT UNSIGNED NOT NULL,                 -- (8) 1..50 enforced by CHECK
  status ENUM('Pending','Confirmed','Cancelled') NOT NULL DEFAULT 'Pending', -- (9)
  PRIMARY KEY (reservation_id),
  UNIQUE KEY uq_datetime_table (reservation_datetime, table_number), -- (10) no two reservations same datetime + table
  CHECK (CHAR_LENGTH(customer_name) >= 3),
  CHECK (guests BETWEEN 1 AND 20),
  CHECK (contact_number BETWEEN 6000000000 AND 9999999999), -- starts 6-9 and exactly 10 digits (numeric)
  CHECK (table_number BETWEEN 1 AND 50)
);
