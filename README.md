# CAPSTONEDE

#  DE-C24-12 Capstone Project: Cloud-Based Data System for E-Commerce

##  **Zonique Browne**  
Project Title: **Sales & Customer Insights for Zora (Demo Fashion Brand)**  
Capstone Track: Data Engineering — DE-C24-12

---

##  Business Overview

**Zora**, a fashion-focused e-commerce brand, aims to better understand customer behavior, product performance, and regional sales patterns. This project builds a scalable cloud-based data system to ingest, process, and analyze e-commerce data.

---

## Problem Statement

Stakeholders lack centralized access to insights like:
- Which products generate the most revenue?
- Which regions are most profitable?
- What are the monthly sales trends?

---

## Technology Stack

| Component              | Tech Used                    |
|------------------------|------------------------------|
| Cloud Provider         | Google Cloud Platform (GCP)  |
| Data Storage           | Cloud SQL (PostgreSQL)       |
| Data Processing        | Python (ETL Script)          |
| Infrastructure         | Cloud Shell, Cloud SDK       |
| Querying               | Cloud SQL Query Editor / Shell |
| Version Control        | GitHub                       |

---

## ETL Pipeline Summary

- Source: Local CSV files (customers, orders, order_items)
- Script: Python ETL (`local_etl.py`)
- Target: Cloud SQL instance `sales-data-zora`  
- Transformation: Type casting, joins, inserts  
- Outcome: Tables populated in PostgreSQL for querying

---

##  Database Schema

### `customers`
| Field        | Type      |
|--------------|-----------|
| customer_id  | SERIAL    |
| full_name    | VARCHAR   |
| email        | VARCHAR   |
| signup_date  | DATE      |
| region       | VARCHAR   |

### `orders`
| Field        | Type      |
|--------------|-----------|
| order_id     | SERIAL    |
| customer_id  | INT (FK)  |
| order_date   | TIMESTAMP |
| total_amount | NUMERIC   |

### `order_items`
| Field         | Type      |
|---------------|-----------|
| order_item_id | SERIAL    |
| order_id      | INT (FK)  |
| product_name  | VARCHAR   |
| quantity      | INT       |
| unit_price    | NUMERIC   |
| total_price   | NUMERIC   |

---

## Sample SQL Insights

### 1 Top 5 Best-Selling Products

```sql
SELECT product_name, SUM(total_price) AS total_revenue
FROM order_items
GROUP BY product_name
ORDER BY total_revenue DESC
LIMIT 5;
```

### 2 Total Sales by Region

```sql
SELECT c.region, SUM(o.total_amount) AS total_sales
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.region
ORDER BY total_sales DESC;
```

 Screenshots of the query results and ERD included in `/screenshots/ folder`.

---

## Outcomes

- Functional ETL pipeline with cloud deployment
- Cloud-based relational database with referential integrity
- Insightful SQL queries produced
- Basic performance considerations were applied, including indexed keys, aggregation filters, and LIMIT usage for efficient querying

---

## Repository Structure

```
├── local_etl.py
├── customers.csv
├── orders.csv
├── order_items.csv
├── CAPSTONE sql queries.sql
└── /screenshots/
