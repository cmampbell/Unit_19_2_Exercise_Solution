from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)

app.config['SECRET_KEY'] = 'poopybutthole'
debug = DebugToolbarExtension(app)

@app.route('/')
def show_story_options():
    return render_template('story_options.html', stories=stories)

@app.route('/madlib')
def show_madlib_form():
    story_obj = stories[request.args.get('selected_story')]
    story_name = request.args.get('selected_story')
    return render_template('madlib_form.html', prompts = story_obj.prompts, story_name = story_name )

@app.route('/story/<story_opt>')
def show_story(story_opt):
    answers = request.args
    return render_template('story.html', story = stories.get(story_opt).generate(answers))