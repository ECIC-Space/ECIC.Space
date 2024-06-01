# Next-Generation Teacher-Student Platform

<div align="center">
  
[**🔣 中文简体**](./README_zh.md)

</div>

## Introduction
This project aims to develop a next-generation platform for teachers and students, integrating AI to enhance accessibility and efficiency in education. The core mission is to bridge the information gap between students and teachers, and to optimize campus efficiency using data-driven insights.

## Features
1. **Dashboard Interface**: A control-panel-like interface that displays past learning data and pending assignments.
2. **Assignment Submission**: Users can submit assignments or create writings directly on the platform, with features like AI scoring, automate saving, grammar checking, and more.
3. **AI-driven Feedback**: Written assignments are graded by cutting-edged LLMs, which provides detailed improvement suggestions.
4. **Progress Tracking**: All user submissions are summarized and tracked by AI, offering detailed progress reports.

## Advantages
- **Modern Technology**: Built with modern technologies, fully encompassing features from legacy platforms.
- **Exclusive AI Automation**: Offers instant feedback on user inputs through automatic AI grading.
- **Personalized Reports**: Strong database support enables detailed analyses and improvement suggestions for each individual.
- **Automated Assessment**: Automated grading for fill-in-the-blank and short answer questions, reducing teachers' workload.

## Technology Stack
- **Backend**: Python with Flask framework; Peewee for database interactions; Celery for task queuing.
- **Frontend**: Developed using Vue.js with ElementPlus as the UI library.

## Repository Structure
This section outlines the structure and purpose of various files within the repository to provide a clearer understanding of the project's architecture.

- **GitHub Actions Workflows**:
  - `.github/workflows/BasicPyStyle.yml`: This workflow is responsible for checking the code style of Python files upon push and pull requests to the main branch.
  - `.github/workflows/PythonStyleCheck.yml`: This workflow performs a comprehensive style check on Python files using wemake-python-styleguide, ensuring adherence to best practices.

- **Backend Application**:
  - `api/user.py`: Defines the user model and handles user-related operations such as authentication and data management.
  - `app.py`: The main Flask application file that configures and runs the web server.

- **CSS Stylesheets**:
  - `static/css/style.css`: The primary CSS stylesheet for the web application, defining the look and feel of the platform.
  - `static/css/test.css`: An additional CSS file used for testing and experimental styles.

- **HTML Template**:
  - `templates/index.html`: The main HTML template for the web application, serving as the entry point for the user interface.

- **Python Package Dependencies**:
  - `requirements.txt`: Lists all Python packages required for the project, facilitating easy installation and management of dependencies.

## Enhanced Frontend Design
We've made significant improvements to the frontend design of our platform to ensure a more fluent and beautiful user experience. Here are some highlights:
- **Responsive Design**: Our website now adapts seamlessly to any screen size, ensuring a great experience on both desktop and mobile devices.
- **Dynamic Content**: With the integration of Vue.js, our website now offers more interactive and dynamic content, making navigation and user engagement more intuitive.
- **Aesthetic Improvements**: We've revamped the visual design, incorporating a modern color scheme and typography that make the platform more inviting and easier to read.

For a closer look, check out the [live demo](#) and explore the new features firsthand.

## Words from core members

Perhaps we need a platform to store the common learning materials of students, to create a study base... In this way, we can **save the time of students and teachers**, and **better spread experience**...  

*-- YuXiao She, Head of ECIC Learning Department 2024, Official Project Initiator, Senior Year*

since march 2023, with the launch of gpt-4, i've seen the immense potential ai holds. in august, i crafted a prototype for the toefl writing tutor. looking back, it seems rudimentary, yet it was quite beneficial, boosting my writing score from 22 to 25. it also aided friends like sam and alan in enhancing their writing abilities. **i aim for widespread access to this tutor, hoping it will simplify the process of improving writing skills and enhance teaching efficiency**. furthermore, my goal is to make the latest models accessible to everyone at ecic. the project is continuously evolving, and soon, you'll experience **a more personalized ai tutor** that remembers your writing style and preferences.

*-- Richards Tu, LLM Developer, Junior Year*

Unexpectedly, from the very beginning relying on open source project learning materials, we finally embarked on the road of independent development. I have always thought that the existing learning website tools are **not easy to use** ~~(especially Zhixuewang and Menkou)~~, but I hope we can change this... Maybe we can't do it very well, but I hope these attempts can change the form of the existing "education system" - from a combination of multiple independent functions, to **a integrated, truly efficiency-improving modern platform**.  

*-- Yao Xiao, Main Developer, Junior Year*
