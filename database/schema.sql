-- ============================================
-- TASKLYTICS DATABASE SCHEMA
-- Version 1.0
-- ============================================

CREATE DATABASE IF NOT EXISTS tasklytics_db;

USE tasklytics_db;

-- ============================================
-- USERS TABLE
-- ============================================

CREATE TABLE IF NOT EXISTS users (

    user_id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(100) NOT NULL,

    email VARCHAR(100) NOT NULL UNIQUE,

    password_hash VARCHAR(255) NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

-- ============================================
-- USER PROGRESS
-- ============================================

CREATE TABLE IF NOT EXISTS user_progress (

    progress_id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL UNIQUE,

    xp INT DEFAULT 0,

    level INT DEFAULT 1,

    streak INT DEFAULT 0,

    productivity_score DECIMAL(5,2) DEFAULT 0.00,

    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE

);

-- ============================================
-- USER SETTINGS
-- ============================================

CREATE TABLE IF NOT EXISTS user_settings (

    settings_id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL UNIQUE,

    dark_mode BOOLEAN DEFAULT TRUE,

    notifications BOOLEAN DEFAULT TRUE,

    default_task_view ENUM('Card','Table')
        DEFAULT 'Card',

    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE

);

-- ============================================
-- TASKS
-- ============================================

CREATE TABLE IF NOT EXISTS tasks (

    task_id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL,

    title VARCHAR(150) NOT NULL,

    description TEXT,

    category VARCHAR(50),

    priority ENUM('Low','Medium','High')
        DEFAULT 'Medium',

    status ENUM('Pending','Completed')
        DEFAULT 'Pending',

    due_date DATE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    completed_at TIMESTAMP NULL,

    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE

);

