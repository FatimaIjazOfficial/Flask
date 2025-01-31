# Flask Projects 

This README provides an overview of various Flask applications and their functionalities. These projects demonstrate basic to advanced usage of Flask, including decorators, handling routes, integrating APIs, and more.

## 1. Basic Flask App
**File: `flask_use.py`**

This basic Flask application demonstrates how to set up routes and return simple text responses.

### Features:
- **Home Route (`/`):** Returns "Website_making".
- **Bye Route (`/bye`):** Returns "Bye".

### Usage:
Run the script and navigate to `http://127.0.0.1:5000/` for the home route and `http://127.0.0.1:5000/bye` for the bye route.

## 2. Advanced Flask Usage with Decorators
**File: `advance_flask_use.py`**

This example showcases how to use decorators to modify the appearance of text on a webpage and how to create variable paths.

### Features:
- **Home Route (`/`):** Returns HTML content including a styled heading and an image.
- **Bye Route (`/bye`):** Returns "Bye!" with bold, emphasized, and underlined text.
- **Username Route (`/username/<name>/<int:number>`):** Greets the user with their name and age.

### Usage:
Run the script and navigate to the respective routes to see the styled text and variable path handling.

## 3. Advanced Python Decorators
**File: `advance_python_decorator.py`**

This script illustrates advanced usage of Python decorators to control function execution based on user authentication status.

### Features:
- **User Authentication Decorator:** Checks if a user is logged in before allowing the creation of a blog post.

### Usage:
Run the script to see how the decorator controls access to the `create_blog_post` function based on user authentication status.

## 4. Guess Number App
**File: `guess_number_app.py`**

A simple Flask app that generates a random number and allows users to guess the number through URL routes.

### Features:
- **Home Route (`/`):** Displays a prompt to guess a number between 0 and 9.
- **Guess Route (`/<int:guess>`):** Provides feedback on whether the guess is too high, too low, or correct.

### Usage:
Run the script and navigate to the home route. Append a number (e.g., `http://127.0.0.1:5000/5`) to guess the random number.

## 5. Card Display
**File: `card.py`**

This Flask app renders a template to display a card.

### Features:
- **Home Route (`/`):** Renders `card_my.html`.

### Usage:
Run the script and ensure `card_my.html` is in the `templates` folder. Navigate to the home route to view the card.

## 6. Personal Site
**File: `personal_site.py`**

A simple Flask application to serve a personal site with HTML content.

### Features:
- **Home Route (`/`):** Renders `index.html`.

### Usage:
Run the script and ensure `index.html` is in the `templates` folder. Navigate to the home route to view the personal site.

## 7. Blog Post with APIs
**File: `blog_post.py`**

This application integrates APIs to generate random numbers and fetch data based on the user's name.

### Features:
- **Home Route (`/`):** Displays a random number and the current year.
- **Guess Route (`/guess/<name>`):** Fetches gender and age predictions based on the name.
- **Blog Route (`/blog`):** Fetches and displays blog posts from an API.

### Usage:
Run the script and navigate to the respective routes to view the random number, guess data, and blog posts.

## 8. My Blog Site
**File: `my_blog_site.py`**

A Flask application to display blog posts fetched from an API and render them using a template.

### Features:
- **Home Route (`/`):** Displays all blog posts.
- **Post Route (`/post/<int:index>`):** Displays a specific post based on its index.

### Usage:
Run the script and navigate to the home route to see all posts. Use the post route to view individual posts by their index.

### Conclusion
These examples demonstrate the versatility and simplicity of Flask for creating web applications. From basic routing to advanced usage with decorators and API integration, Flask provides a solid foundation for web development in Python. Customize these scripts as needed to fit your specific use cases.
