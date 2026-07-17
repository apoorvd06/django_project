# InkOrbit - Django Blog Application

A full-featured, responsive blog web application built using the Django framework. This project provides a complete platform for users to create, manage, and share blog posts with a fully functioning authentication system and a clean, modern user interface. 

## ✨ Features

* **User Authentication & Management:** 
  * User registration and login functionality.
  * Profile management with custom profile pictures.
  * Secure password reset via email ("Forgot Password" feature).
* **Blog Post Operations (CRUD):** 
  * Users can create, read, update, and delete their own blog posts.
  * Rich media support for post attachments.
* **Pagination:** Seamless navigation through blog posts with built-in pagination.
* **Responsive UI:** Styled using Bootstrap 4 and `crispy-bootstrap4` for clean, responsive forms and layouts that work on both desktop and mobile devices.

## 🛠️ Technology Stack

* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 4
* **Database:** SQLite (Development)
* **Environment:** Virtualenv, PowerShell/Bash

## 📁 Project Structure

* `InkOrbit/` - Core project settings and configuration.
* `blog/` - Main application handling post creation, viewing, and pagination logic.
* `users/` - Handles user authentication, registration, profiles, and password resets.
* `media/` - Directory for user-uploaded files, such as profile pictures.
* `build.sh` & `runtime.txt` - Configuration files for cloud deployment.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need Python installed on your local machine. It is highly recommended to use a virtual environment.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/apoorvd06/InkOrbit.git
