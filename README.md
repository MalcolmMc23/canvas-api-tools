# Canvas API Tools

A Python-based toolkit for interacting with the Canvas LMS API. This project provides easy-to-use functions for students to access their Canvas courses, assignments, grades, and more.

## Features

- Get course information and enrollment terms
- View detailed assignment information
- Check announcements
- View calendar events
- Check submission details
- View course grades
- And more!

## Installation

1. Clone this repository:
```bash
git clone https://github.com/MalcolmMc23/canvas-api-tools.git
cd canvas-api-tools
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:
```bash
cp .env.example .env
```

4. Configure your Canvas API token:
   - Go to your Canvas account settings
   - Click on "New Access Token"
   - Copy the token and paste it in your `.env` file

## Usage

Run the test script to try out all functions:
```bash
python test_canvas_api.py
```

### Available Functions

1. `get_courses()`: List all your courses
2. `get_assignments(course_id)`: Get detailed assignment information
3. `get_announcements(course_id)`: View course announcements
4. `get_calendar_events(start_date, end_date)`: View calendar events
5. `get_submission_details(course_id, assignment_id)`: Check assignment submissions
6. `get_course_grades()`: View your grades
7. `get_enrollment_terms()`: List available terms

## Security Notes

- Never commit your `.env` file or share your API token
- The `.gitignore` file is set up to prevent accidental commits of sensitive information
- Regularly rotate your Canvas API token for security

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.