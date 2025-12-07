from flask import Flask, render_template, request
import importlib
import io
from contextlib import redirect_stdout
import os
import re

app = Flask(__name__)

def get_available_days():
    """Scans the directory for Day_X.py files and returns a list of available days."""
    days = []
    for f in os.listdir('.'):
        match = re.match(r'Day_(\d+)\.py', f)
        if match:
            days.append(int(match.group(1)))
    return sorted(days)

@app.route('/', methods=['GET', 'POST'])
def index():
    available_days = get_available_days()
    result = None
    error = None
    # Set default day to the first available day or 1
    default_day = available_days[0] if available_days else 1
    selected_day = request.form.get('day', default_day, type=int)
    selected_part = request.form.get('part', 'One')
    input_data = request.form.get('input_data', '')

    if request.method == 'POST':
        try:
            day = request.form['day']
            part = request.form['part'] # 'One' or 'Two'
            input_data = request.form['input_data']

            # Write the pasted input to a temporary file
            with open('/tmp/flask_input.txt', 'w') as f:
                f.write(input_data)

            # Dynamically import the module and class
            module_name = f'Day_{day}'
            class_name = f'Part{part}'

            # Ensure the module is fresh for every run
            if module_name in locals():
                importlib.reload(locals()[module_name])

            module = importlib.import_module(module_name)
            SolverClass = getattr(module, class_name)
            solver_instance = SolverClass()

            # Capture the output of the solve() method
            f = io.StringIO()
            with redirect_stdout(f):
                # Call solve(), assuming it can take a filename argument
                # Based on previous days, this is a safe assumption.
                solver_instance.solve(filename='flask_input.txt')
            result = f.getvalue()

        except ImportError:
            error = f"Error: Could not find solution module for Day {day} (expected '{module_name}.py')."
        except AttributeError:
            error = f"Error: Could not find class '{class_name}' for Day {day}."
        except Exception as e:
            error = f"An unexpected error occurred: {e}"
        
        if error:
            result = error

    return render_template('index.html',
                           result=result,
                           available_days=available_days,
                           selected_day=selected_day,
                           selected_part=selected_part,
                           input_data=input_data)