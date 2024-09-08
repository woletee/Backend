from flask import Flask, jsonify, send_from_directory, abort
import os

app = Flask(__name__)

# Define the path to your dataset directory
DATASET_DIR = os.path.join(os.getcwd(), 'Data', 'ARC_dataset', 'abstraction_and_reasoning_challenge', 'training')

@app.route('/api/tasks/<task_number>', methods=['GET'])
def get_task(task_number):
    try:
        # Costruct the file path
        file_path = os.path.join(DATASET_DIR, f'{task_number}.json')

        # Serve the file as a JSON response
        with open(file_path, 'r') as file:
            task_data = file.read()
        return jsonify(eval(task_data))
    except FileNotFoundError:
        abort(404, description="Task not found")

if __name__ == '__main__':
    app.run(debug=True, port=5001)
#
