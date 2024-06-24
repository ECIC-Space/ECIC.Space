# celery_config.py
import sys
import json
import os

import anthropic
from celery import Celery
from openai import OpenAI

# 创建Celery应用
app = Celery('ai_tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
app.conf.broker_connection_retry_on_startup = True

# 增加更多的调试配置
app.conf.update(
    worker_prefetch_multiplier=1,
    task_acks_late=True,
)


def load_api_keys(file_path='secrets.json'):
    """
    从JSON文件中加载API密钥
    """
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建JSON文件的完整路径
    full_path = os.path.join(current_dir, file_path)

    try:
        with open(full_path, 'r') as file:
            keys = json.load(file)
        return keys
    except FileNotFoundError:
        print(f"错误: 无法找到文件 {full_path}")
        return None
    except json.JSONDecodeError:
        print(f"错误: {file_path} 不是有效的JSON文件")
        return None


# 使用示例
api_keys = load_api_keys()
if api_keys:
    pass
else:
    print("无法加载API密钥，请检查api_keys.json文件")

openai_key = api_keys['openai']['api_key']
anthropic_key = api_keys['anthropic']['api_key']
# OpenAI客户端初始化
openai_client = OpenAI()
# Anthropic客户端初始化
anthropic_client = anthropic.Anthropic(api_key=anthropic_key)


@app.task(name='ai_tasks.call_ai_api', bind=True)
def call_ai_api(self, model_name, system_prompt, user_request):
    print(f"Task {self.request.id} started: model={model_name}")
    try:
        if "gpt" in model_name.lower():
            result = call_openai_api(model_name, system_prompt, user_request)
        elif "claude" in model_name.lower():
            result = call_claude_api(model_name, system_prompt, user_request)
        else:
            raise ValueError(f"Unsupported model: {model_name}")
        print(f"Task {self.request.id} completed successfully")
        return result
    except Exception as e:
        error_msg = f"Error in call_ai_api: {str(e)}"
        print(error_msg, file=sys.stderr)
        self.update_state(state='FAILURE', meta={'error': error_msg})
        raise


def call_openai_api(model_name, system_prompt, user_request):
    print("开始调用OpenAI API")
    try:
        completion = openai_client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_request}
            ]
        )
        result = completion.choices[0].message.content
        print(f"OpenAI API调用完成，结果：{result}")
        return result
    except Exception as e:
        print(f"OpenAI API调用出错：{str(e)}")
        raise


def call_claude_api(model_name, system_prompt, user_request):
    print("开始调用Claude API")
    try:
        message = anthropic_client.messages.create(
            model=model_name,
            max_tokens=1024,
            system=system_prompt,  # 将系统提示作为单独的参数传递
            messages=[
                {"role": "user", "content": user_request}
            ]
        )
        result = message.content[0].text
        print(f"Claude API调用完成，结果：{result}")
        return result
    except anthropic.APIError as e:
        error_msg = f"Claude API调用出错：{str(e)}"
        print(error_msg, file=sys.stderr)
        raise ValueError(error_msg)
    except Exception as e:
        error_msg = f"Claude API调用出错：{str(e)}"
        print(error_msg, file=sys.stderr)
        raise ValueError(error_msg)


if __name__ == '__main__':
    # 当直接运行此脚本时，使用单进程模式和调试日志级别
    argv = [
        'worker',
        '--loglevel=info',
        '-P', 'solo',
    ]
    # argv = [
    #     'worker',
    #     '--loglevel=DEBUG',
    #     '-P', 'solo',
    # ]
    app.worker_main(argv)
