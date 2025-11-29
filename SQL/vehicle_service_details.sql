 create schema vehicle;
 use vehicle;
 
CREATE TABLE vehicle_service_booking (
  booking_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  customer_name VARCHAR(100) NOT NULL,
  CHECK (CHAR_LENGTH(customer_name) >= 3),
  vehicle_type ENUM('Car','Bike','Scooter','Truck') NOT NULL,
  vehicle_number VARCHAR(20) NOT NULL UNIQUE,
  service_date DATE NOT NULL DEFAULT (CURRENT_DATE),
  preferred_slot ENUM('Morning','Afternoon','Evening') NOT NULL,
  service_cost DECIMAL(10,2) NOT NULL,
  pickup_required BOOLEAN NOT NULL DEFAULT FALSE,
  status ENUM('Requested','In Progress','Completed','Cancelled') NOT NULL DEFAULT 'Requested'
);
