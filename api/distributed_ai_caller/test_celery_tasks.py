# test_celery_tasks.py
import unittest
from unittest.mock import patch, MagicMock
from celery_config import call_ai_api, call_openai_api, call_claude_api


class TestCeleryTasks(unittest.TestCase):

    @patch('celery_config.call_openai_api')
    def test_call_ai_api_gpt(self, mock_openai):
        mock_openai.return_value = "OpenAI response"
        result = call_ai_api("gpt-3.5-turbo", "System prompt", "User request")
        self.assertEqual(result, "OpenAI response")
        mock_openai.assert_called_once_with("gpt-3.5-turbo", "System prompt", "User request")

    @patch('celery_config.call_claude_api')
    def test_call_ai_api_claude(self, mock_claude):
        mock_claude.return_value = "Claude response"
        result = call_ai_api("claude-2", "System prompt", "User request")
        self.assertEqual(result, "Claude response")
        mock_claude.assert_called_once_with("claude-2", "System prompt", "User request")

    def test_call_ai_api_unsupported_model(self):
        with self.assertRaises(ValueError):
            call_ai_api("unsupported-model", "System prompt", "User request")

    @patch('celery_config.openai.ChatCompletion.create')
    def test_call_openai_api(self, mock_create):
        mock_response = MagicMock()
        mock_response.choices[0].message = {'content': 'OpenAI response'}
        mock_create.return_value = mock_response

        result = call_openai_api("gpt-3.5-turbo", "System prompt", "User request")
        self.assertEqual(result, "OpenAI response")
        mock_create.assert_called_once()

    @patch('celery_config.anthropic.completions.create')
    def test_call_claude_api(self, mock_create):
        mock_response = MagicMock()
        mock_response.completion = 'Claude response'
        mock_create.return_value = mock_response

        result = call_claude_api("claude-2", "System prompt", "User request")
        self.assertEqual(result, "Claude response")
        mock_create.assert_called_once()


if __name__ == '__main__':
    unittest.main()