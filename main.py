
# Import necessary modules
from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Define the routes
@app.route('/')
def index():
    """
    Renders the main landing page of the website.
    """
    return render_template('index.html')


@app.route('/lessons')
def lessons():
    """
    Renders the page displaying the list of Mandarin lessons available for learning.
    """
    return render_template('lessons.html')


@app.route('/lessons/<lesson_id>')
def lesson(lesson_id):
    """
    Renders the page displaying the specific Mandarin lesson based on the provided lesson ID.
    """
    return render_template('lessons.html', lesson_id=lesson_id)

# Sample data for lessons
lessons = [
    {
        'id': 1,
        'title': 'Lesson 1: Basics',
        'sections': [
            {
                'title': 'Section 1: Greetings',
                'content': 'Learn how to greet people in Mandarin.',
                'image': 'images/greetings.jpg'
            },
            {
                'title': 'Section 2: Numbers',
                'content': 'Learn how to count numbers in Mandarin.',
                'image': 'images/numbers.jpg'
            }
        ]
    },
    {
        'id': 2,
        'title': 'Lesson 2: Food',
        'sections': [
            {
                'title': 'Section 1: Ordering food',
                'content': 'Learn how to order food in Mandarin.',
                'image': 'images/food_ordering.jpg'
            },
            {
                'title': 'Section 2: Food vocabulary',
                'content': 'Learn vocabulary related to food in Mandarin.',
                'image': 'images/food_vocabulary.jpg'
            }
        ]
    }
]

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
