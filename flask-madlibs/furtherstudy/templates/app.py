from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

# Initialize the debug toolbar
debug = DebugToolbarExtension(app)

@app.route('/')
def select_story():
    """Display the home page to select a story."""
    story_titles = stories.keys()
    return render_template('select-story.html', story_titles=story_titles)

@app.route('/questions')
def ask_questions():
    """Display the form to fill in the story prompts."""
    story_id = request.args.get("story")
    story = stories[story_id]
    prompts = story.prompts
    return render_template('questions.html', story_id=story_id, prompts=prompts)

@app.route('/story')
def show_story():
    """Generate and display the story from the user's input."""
    story_id = request.args.get("story")
    story = stories[story_id]
    answers = {prompt: request.args.get(prompt) for prompt in story.prompts}
    generated_story = story.generate(answers)
    return render_template('story.html', story=generated_story)

if __name__ == '__main__':
    app.run(debug=True)
