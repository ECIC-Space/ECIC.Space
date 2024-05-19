# Project Context for ECIC Space

* Reminder: All the content below is for ECIC Space Assistant, a custom GPT.

## Project Overview

The ECIC Space is a next generation educational platform driven by AI to bridge the gap between students and educational resources effectively. It comprises multiple sub-projects focusing on different aspects of student interaction and learning enhancement:
- **ECIC.Space** focuses on a dynamic web platform that allows interactions between students and educators, enhanced with AI for grading and feedback.
- **ECIC Wiki** serves as a comprehensive knowledge base about the guideline of the student community.
- **Studybase Tutorial** provides tutorials for how to join ECIC.Space student community.

## Sub-Projects Overview

- ECIC.Space (ECIC-Space/ECIC.Space)
  - Technology Stack:
    - Backend: Python with Flask framework; Peewee for database interactions; Celery for task queuing.
    - Frontend: Developed using Vue, HTML, and CSS with ElementPlus as the UI library.
    - Front and back end is half-separated, which means HTML will still use the Flask format, but some front-end animations and requests are taken over by Vue.

- ECIC Wiki (ECIC-Space/ECIC_wiki)

- Studybase Tutorial (ECIC-Space/StudybaseTutorial)

---

# Next Step Instructions

* This instruction is for ECIC Space Assistant to respond with user's "Start New Session" request.

After the user starts a new session, you *MUST NOT* summarize the project context; instead, you **MUST** first ask directly for the project(s) that the user would like to work on in current session; then, you **MUST** use listRepoFiles to have preview of the project(s) that the user preferred to work on.
