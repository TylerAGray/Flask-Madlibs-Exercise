from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

# Initialize the debug toolbar
debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    """Display the home page with a form to fill in the story prompts."""
    prompts = story.prompts
    return render_template('questions.html', prompts=prompts)

@app.route('/story')
def show_story():
    """Generate and display the story from the user's input."""
    answers = {prompt: request.args.get(prompt) for prompt in story.prompts}
    generated_story = story.generate(answers)
    return render_template('story.html', text=generated_story)

if __name__ == '__main__':
    app.run(debug=True)
