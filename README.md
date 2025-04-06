# Twitter Clone

![Twitter Clone](https://raw.githubusercontent.com/Ussingh47/twitter/main/static/img/twitter-clone-preview.png)

A full-featured Twitter clone built with Django, featuring user authentication, tweets, likes, comments, and follows. This project demonstrates the implementation of a social media platform with core Twitter functionalities.

## Features

### User Management
- User registration and authentication system
- Password reset functionality
- User profiles with customizable information (bio, location, website, profile picture)
- Follow/unfollow system with follower/following lists

### Content Features
- Create, edit, and delete tweets (280 character limit)
- Upload images with tweets
- Like/unlike tweets
- Comment on tweets
- Delete comments

### Feed and Navigation
- Home timeline showing tweets from followed users
- Explore page showing all tweets
- User profile pages showing user's tweets
- Search functionality for finding users and tweets
- Responsive design for mobile and desktop

## Technologies Used

### Backend
- Django 5.2 - Python web framework
- SQLite - Database
- Pillow - Image processing

### Frontend
- Bootstrap 5 - CSS framework
- HTML5 & CSS3
- JavaScript
- Font Awesome - Icons

### Development Tools
- Git - Version control
- GitHub - Code repository
- Django Debug Toolbar (development only)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Ussingh47/twitter.git
   cd twitter
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Open your browser and go to http://localhost:8000

## Usage

### Authentication
- Register a new account or login with the admin account (username: admin, password: 123)
- Update your profile information and profile picture

### Creating Content
- Create tweets from the home page (up to 280 characters)
- Optionally attach images to your tweets
- Edit or delete your own tweets

### Interacting with Content
- Like tweets by clicking the heart icon
- Comment on tweets by clicking on a tweet and using the comment form
- Delete your own comments

### Social Features
- Follow other users by visiting their profile and clicking "Follow"
- Unfollow users by clicking "Unfollow" on their profile
- View lists of followers and following users

### Navigation
- Home: View tweets from users you follow
- Explore: Discover tweets from all users
- Profile: View and edit your profile, see your tweets
- Search: Find users and tweets using the search bar

## Admin Interface

The Django admin interface provides powerful tools for managing the application:

1. Access the admin panel at http://localhost:8000/admin/
2. Login with admin credentials (username: admin, password: 123)
3. Manage users, profiles, tweets, comments, likes, and follows

## Deployment

This application can be deployed to various platforms:

### PythonAnywhere
1. Create a PythonAnywhere account
2. Upload your code or clone from GitHub
3. Set up a virtual environment and install dependencies
4. Configure the WSGI file to point to your Django application
5. Set up static and media files


## License

This project is licensed under the MIT License - see the LICENSE file for details.


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
