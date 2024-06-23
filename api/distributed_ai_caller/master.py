# master.py
from flask import Flask, request, jsonify
from celery_config import call_ai_api
from celery.result import AsyncResult
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


@app.route('/call_ai', methods=['POST'])
def call_ai():
    data = request.json
    model_name = data.get('model_name')
    system_prompt = data.get('system_prompt')
    user_request = data.get('user_request')

    app.logger.info(f"Received request for model: {model_name}")
    task = call_ai_api.delay(model_name, system_prompt, user_request)
    app.logger.info(f"Task created with id: {task.id}")
    return jsonify({"task_id": task.id}), 202


@app.route('/get_result/<task_id>', methods=['GET'])
def get_result(task_id):
    app.logger.info(f"Checking result for task: {task_id}")
    task = AsyncResult(task_id, app=call_ai_api.app)
    if task.ready():
        app.logger.info(f"Task {task_id} is ready")
        if task.successful():
            result = task.result
            app.logger.info(f"Task {task_id} completed successfully: {result}")
            return jsonify({"status": "completed", "result": result})
        else:
            error = str(task.result)
            app.logger.error(f"Task {task_id} failed: {error}")
            return jsonify({"status": "error", "message": error}), 500
    else:
        app.logger.info(f"Task {task_id} is still pending")
        return jsonify({"status": "pending"}), 202


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)