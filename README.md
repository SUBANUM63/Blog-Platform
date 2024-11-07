# Blog Platform

A full-stack blog platform where users can create, edit, and delete blog posts. The platform allows users to track posts they've read and offers a responsive design for optimal viewing on different devices. Additional features include a markdown editor and the ability to upload header images for blog posts.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## Features
- User authentication (signup, login, logout)
- Create, edit, delete blog posts
- Track the list of posts users have read
- Responsive design for mobile and desktop devices
- Markdown editor for content creation
- Optional: Upload header images for blog posts

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript (with Bootstrap framework)
- **Backend:** Python Flask
- **Database:** MySQL
- **Other Services:**
  - JSON Web Tokens (JWT) for user authentication
  - PILLOW (optional) for image uploads
  - Markdown libraries for post creation

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Blog-Platform.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd Blog-Platform
   ```
3. **Install backend dependencies:**
   ```bash
   # Create and activate a virtual environment
   python3 -m venv venv
   source venv/bin/activate
   source  set_env.sh
   
   # Install Flask and other dependencies
   pip install -r requirements.txt
   ```
4. **Set up MySQL database:**
   - Ensure MySQL is installed and running.
   - Create a database and update the database URL in the configuration file.
   - Run the Application:
   - initialize the database
   ```bash
   python3 init_db.py
   ```
5. **RUN THE THE FLASK SERVER**
   ```bash
   python3 run.py
   ```

## Usage
   - Register a new account or log in with an existing account.
   - Create, edit, and delete blog posts.
   - View the list of blog posts and track the ones you’ve read.
   - Use markdown to format your posts and optionally upload a header image for each post.
## Roadmap
   **Version 1.0:**
   - Basic CRUD functionality for blog posts
   - User authentication
   - Responsive design using Bootstrap
   - Markdown editor for posts

   **Future Enhancements:**
   - Image upload for blog post headers
   - Advanced user profiles
   - Commenting system
   - Post categories and tags

## Contributing
- Contributions are welcome! Please follow these steps:

  - 1, Fork the repository.
  - 2, Create a new branch (git checkout -b feature-branch).
  - 3, Make your changes and commit them (git commit -m 'Add feature').
  - 4, Push to the branch (git push origin feature-branch).
  - 5, Open a pull request.

## License
 - This project is licensed under the MIT License. See the LICENSE file for details.

