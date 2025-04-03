import asyncio
from app import (
    get_courses,
    get_assignments,
    get_announcements,
    get_calendar_events,
    get_submission_details,
    get_course_grades,
    get_enrollment_terms
)
from datetime import datetime

async def test_canvas_api():
    print("\n=== Testing Canvas API Functions ===\n")

    print("1. Testing get_enrollment_terms()")
    print("-" * 50)
    terms = await get_enrollment_terms()
    print(terms)
    print("\nPress Enter to continue...")
    input()

    print("\n2. Testing get_courses()")
    print("-" * 50)
    courses = await get_courses()
    print(courses)
    print("\nPress Enter to continue...")
    input()

    # After getting courses, we can test functions that need course_id
    print("\nPlease enter a course_id from the list above to test other functions.")
    print("Format example: If you see 'Course Name (ID: 12345)', enter '12345'")
    course_id = input("Course ID: ").strip()

    print("\n3. Testing get_assignments()")
    print("=" * 50)
    print("Fetching detailed assignment information...")
    print("=" * 50)
    assignments = await get_assignments(course_id)
    
    # Process and display assignments
    if assignments.startswith("Error:"):
        print(assignments)
    else:
        # Split assignments by the separator we used (50 dashes)
        individual_assignments = assignments.split("-" * 50)
        
        # Store assignment information for later use
        assignment_info = []
        
        # Display assignments with better formatting
        for assignment in individual_assignments:
            if assignment.strip():  # Skip empty sections
                print(assignment.strip())
                print("=" * 50)
                
                # Extract assignment name and ID
                assignment_name = ""
                assignment_id = ""
                due_date = ""
                
                for line in assignment.split('\n'):
                    if line.startswith("Assignment: "):
                        assignment_name = line.replace("Assignment: ", "").strip()
                    elif line.startswith("ID: "):
                        assignment_id = line.replace("ID: ", "").strip()
                    elif line.startswith("Due Date: "):
                        due_date = line.replace("Due Date: ", "").strip()
                
                if assignment_name and assignment_id:
                    assignment_info.append((assignment_name, assignment_id, due_date))
        
        # Display available assignments in a clean summary format
        if assignment_info:
            print("\nAssignment Summary:")
            print("-" * 100)
            print(f"{'Assignment Name':<50} {'ID':<15} {'Due Date':<30}")
            print("-" * 100)
            
            # Sort assignments by due date if possible
            assignment_info.sort(key=lambda x: x[2] if x[2] != 'No due date' else '9999')
            
            for name, aid, due in assignment_info:
                # Truncate long names but keep them readable
                display_name = name[:47] + "..." if len(name) > 47 else name
                print(f"{display_name:<50} {aid:<15} {due:<30}")
            
            print("-" * 100)
            print("\nNote: You can use any of these IDs when testing submission details.")
    
    print("\nPress Enter to continue...")
    input()

    print("\n4. Testing get_announcements()")
    print("-" * 50)
    announcements = await get_announcements(course_id)
    print(announcements)
    print("\nPress Enter to continue...")
    input()

    # For calendar events, let's test with a date range
    print("\n5. Testing get_calendar_events()")
    print("(Showing events for the entire year 2024)")
    print("-" * 50)
    calendar_events = await get_calendar_events("2024-01-01", "2024-12-31")
    print(calendar_events)
    print("\nPress Enter to continue...")
    input()

    # For submission details, we need both course_id and assignment_id
    print("\nPlease enter an assignment_id from the list above.")
    print("Format example: If you see 'Assignment ID: 67890', enter '67890'")
    assignment_id = input("Assignment ID: ").strip()

    if assignment_id:
        print("\n6. Testing get_submission_details()")
        print("-" * 50)
        submission = await get_submission_details(course_id, assignment_id)
        print(submission)
    else:
        print("\nSkipping submission details test (no assignment ID provided)")
    
    print("\nPress Enter to continue...")
    input()

    print("\n7. Testing get_course_grades()")
    print("-" * 50)
    grades = await get_course_grades()
    print(grades)

    print("\n=== Testing Complete ===")
    print("\nNote: If you encountered any permission errors, please verify your API token has the necessary permissions.")
    print("Required permissions include: read courses, read announcements, read assignments, read submissions, read calendar")

if __name__ == "__main__":
    asyncio.run(test_canvas_api())