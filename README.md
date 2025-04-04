# Twitter Clone

A Twitter clone built with Django, featuring user authentication, tweets, likes, comments, and follows.

## Features

- User registration and authentication
- User profiles with customizable information
- Posting, editing, and deleting tweets
- Liking and commenting on tweets
- Following/unfollowing users
- Timeline showing tweets from followed users
- Explore page showing all tweets
- Search functionality for users and tweets

## Technologies Used

- Django
- Bootstrap
- SQLite
- HTML/CSS/JavaScript

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/twitter-clone.git
   cd twitter-clone
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

- Register a new account or login with the superuser account
- Create tweets from the home page
- Explore all tweets on the explore page
- View and edit your profile
- Follow other users to see their tweets in your timeline
- Like and comment on tweets

## License

This project is licensed under the MIT License - see the LICENSE file for details.
