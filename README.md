## Flask Application Design for Mandarin Learning Website with Images

### HTML Files
- **index.html**:
    - Main landing page for the website.
    - Will include a brief introduction to the website and the offered Mandarin learning content.
    - It will provide navigation options to access different learning categories or lessons.

- **lessons.html**:
    - A dynamic HTML page that will display the Mandarin lessons.
    - Each lesson will be divided into sections, with images to support the learning content.
    - Users can navigate through different lessons and sections from this page.

### Routes
- **@app.route('/')**:
    - This route will handle the main landing page of the website and display the content defined in **index.html**.

- **@app.route('/lessons')**:
    - This route will display the list of Mandarin lessons available for learning.

- **@app.route('/lessons/<lesson_id>')**:
    - This route will display the specific Mandarin lesson based on the provided lesson ID. It will render the content defined in **lessons.html**, populating it with the relevant lesson data.