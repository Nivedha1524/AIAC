DROP TABLE IF EXISTS Restaurannt;
DROP TABLE IF EXISTS Customeer; 
DROP TABLE IF EXISTS Menu_Iteem;    
DROP TABLE IF EXISTS Ordeer;
-- Create Restaurants table
CREATE TABLE IF NOT EXISTS Restaurannt(
    RestaurantID INT PRIMARY KEY,
    Name VARCHAR(100),
    Location VARCHAR(100),
    Rating DECIMAL(2, 1));
-- Create Customers table
CREATE TABLE IF NOT EXISTS Customeer(
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(15));
-- Create Menu_Items table
CREATE TABLE IF NOT EXISTS Menu_Iteem(
    MenuItemID INT PRIMARY KEY,
    RestaurantID INT,
    ItemName VARCHAR(100),
    Price DECIMAL(10, 2),
    FOREIGN KEY (RestaurantID) REFERENCES Restaurannt(RestaurantID));
-- Create Orders table
CREATE TABLE Ordeer(
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    MenuItemID INT,
    OrderDate DATETIME,
    FOREIGN KEY (CustomerID) REFERENCES Customeer(CustomerID),
    FOREIGN KEY (MenuItemID) REFERENCES Menu_Iteem(MenuItemID));
-- Insert random data into Restaurants
INSERT INTO Restaurannt(RestaurantID, Name, Location, Rating) VALUES
(1, 'Spicy Delights', 'New York', 4.5),
(2, 'Healthy Eats', 'Los Angeles', 4.0),
(3, 'Pizza Paradise', 'Chicago', 4.7);
-- Insert random data into Customers
INSERT INTO Customeer(CustomerID, Name, Email, Phone) VALUES
(1, 'John Doe', 'john@example.com', '1234567890'),
(2, 'Jane Smith', 'jane@example.com', '0987654321'),
(3, 'Alice Johnson', 'alice@example.com', '1122334455');
-- Insert random data into Menu_Items
INSERT INTO Menu_Iteem(MenuItemID, RestaurantID, ItemName, Price) VALUES
(1, 1, 'Spicy Chicken Curry', 600.00),
(2, 1, 'Vegetable Biryani', 450.00),
(3, 2, 'Quinoa Salad', 300.00),
(4, 3, 'Pepperoni Pizza', 700.00);
-- Insert random data into Orders
INSERT INTO Ordeer(OrderID, CustomerID, MenuItemID, OrderDate) VALUES
(1, 1, 1, '2023-10-01 12:00:00'),
(2, 2, 4, '2023-10-02 13:00:00'),
(3, 3, 2, '2023-10-03 14:00:00');
-- Query to list all customers who ordered items costing above ₹500
SELECT DISTINCT c.Name, c.Email
FROM Customeer c
JOIN Ordeer o ON c.CustomerID = o.CustomerID
JOIN Menu_Iteem m ON o.MenuItemID = m.MenuItemID
WHERE m.Price > 500;