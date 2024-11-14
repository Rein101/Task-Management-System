# Task Management System

## Overview
The Task Management System is a command-line interface (CLI) application that helps users organize and track both personal and work-related tasks. The system allows users to create, view, delete, and manage tasks with features like priority settings, team member assignments, and due date tracking.

### Key Features
- Create and manage both personal and work tasks
- Track task priorities and team members
- Monitor pending and overdue tasks
- Save and load tasks from CSV files
- Filter tasks by type (personal/work)

## Setup Instructions

### Prerequisites
- Python 3
- Visual Studio and Kaggle Notebook
- CSV module (included in Python standard library)
- datetime module (included in Python standard library)

### Installation
1. Clone or download the repository containing the following files:
   - `task.py`
   - `task_manager.py`
   - `interface.py`
     
2. No additional package installation is required as the system uses Python standard libraries.

### Running the Program
```bash
python interface.py
```

## System Architecture

### 1. Interface Module (`interface.py`)
The main interaction point for users, providing a Console Interface Menu with the following options:

#### Main Menu Functions
1. **Create Task** (`create_task`)
   - Prompts for task type (personal/work)
   - Collects task details (title, due date, description)
   - For personal tasks: Sets priority level at either high,medium or low
   - For work tasks: Assigns team members
   ```python
   # Example usage
   
   task = create_task(task_manager)
   ```

2. **View Tasks** (`view_tasks`)
   - Displays all tasks in the system
   - Shows task details including Task ID, description, due date, and status

3. **Filter Tasks** (`get_tasks`)
   - Filters tasks by type (personal/work)
   - Displays filtered task list with details

4. **Delete Task** (`delete_task`)
   - Removes task by ID
   - Provides confirmation of deletion

5. **Save/Load Tasks** (`save_tasks_to_csv`/`load_tasks_from_csv`)
   - Persists tasks to CSV file
   - Loads tasks from existing CSV file. If there are no tasks, an error is printed

6. **View Pending/Overdue Tasks** (`view_pending_and_overdue_tasks`)
   - Shows tasks categorized by status
   - Identifies overdue tasks based on current date

### 2. Task Module (`task.py`)
Defines the base Task class and its subclasses:

#### Classes
- **Task**: Base class with common task properties
- **PersonalTask**: Extends Task with priority settings
- **WorkTask**: Extends Task with team member management

### 3. Task Manager Module (`task_manager.py`)
Handles task operations and storage:

#### Key Methods
- `add_task`: Adds new tasks to the system
- `get_tasks`: Retrieves filtered task lists
- `delete_task`: Removes tasks by ID
- `save_task`/`load_task`: Handles CSV file operations
- `get_pending_tasks`/`get_overdue_tasks`: Creates lists of filtered objects based on whether they are pending or overdue respectively, from `datatime.now().date()`

## Error Handling

The system implements error handling throughout:

1. **Input Validation**
   - Task type validation (personal/work)
   - Date format validation (YYYY-MM-DD)
   - Priority level validation (high/medium/low)

2. **File Operations**
   ```python
   # error handling in the task_manager.py
   try:
       with open(filename, 'r', newline='\n') as file:
           # File operations
   
   except FileNotFoundError:
       print(f"Error: The file '{filename}' does not exist.")
   except (ValueError, IndexError):
       print("Error: Invalid data format in the CSV file.")
    except Exception as e:
            print(f"An unexpected error occurred: {e}")
   
   ```

3. **Data Validation**
   - Task ID verification before deletion
   - Team member format validation
   - Description length validation (max 15 characters)

## Usage Examples

### Creating a Personal Task
```python
Enter your choice (1-8): 1
Enter task type (personal/work): personal
Enter task title: Buy groceries
Enter due date (YYYY-MM-DD): 2024-11-20
Enter task description: Weekly shopping
Enter priority (high/medium/low): high
```

### Creating a Work Task
```python
Enter your choice (1-8): 1
Enter task type (personal/work): work
Enter task title: Project meeting
Enter due date (YYYY-MM-DD): 2024-11-15
Enter task description: Team sync
Enter team members (comma-separated): John, Alice, Bob
```

### Viewing Filtered Tasks
```python
Enter your choice (1-8): 2
Enter task type to filter by (personal/work): personal
Task ID: 1, Task: Buy groceries, Due Date: 20-11-2024, Status: Pending, Priority: high
```

#### Managing Tasks
```python
# Viewing All Tasks
Enter task type (personal/work/all): all
Task ID: 1, Task: Dentist Appointment, Due Date: 20-11-2024, Status: Pending, Priority: high
Task ID: 2, Task: Client Presentation, Due Date: 15-11-2024, Status: Pending, Team: John, Alice, Bob, Sarah

# Filtering Personal Tasks
Enter task type to filter by (personal/work): personal
Task ID: 1, Task: Dentist Appointment, Due Date: 20-11-2024, Status: Pending, Priority: high

# Filtering Work Tasks
Enter task type to filter by (personal/work): work
Task ID: 2, Task: Client Presentation, Due Date: 15-11-2024, Status: Pending, Team: John, Alice, Bob, Sarah
```

### 2. Task Priority Management

#### High Priority Personal Tasks
```python
Enter task type (personal/work): personal
Enter task title: Tax Return
Enter due date (YYYY-MM-DD): 2024-12-31
Enter task description: File taxes
Enter priority (high/medium/low): high

# Later viewing high priority tasks
Task ID: 3, Task: Tax Return, Due Date: 31-12-2024, Status: Pending, Priority: high
```

#### Team Task Management
```python
Enter your choice (1-8): 1
# Creating a team project task
Enter task type (personal/work): work
Enter task title: Sprint Planning
Enter due date (YYYY-MM-DD): 2024-11-18
Enter task description: Q4 Goals
Enter team members (comma-separated): Dev Team, Product Owner, Scrum Master

# Creating a subtask
Enter task type (personal/work): work
Enter task title: User Stories
Enter due date (YYYY-MM-DD): 2024-11-16
Enter task description: Story points
Enter team members (comma-separated): Dev Team
```

### 3. Task Status and Timeline Management

#### Checking Pending Tasks
```python
# View Pending Tasks
Enter your choice (1-8): 6
Pending Tasks:
Task ID: 1, Task: Dentist Appointment, Due Date: 20-11-2024, Status: Pending, Priority: high
Task ID: 2, Task: Client Presentation, Due Date: 15-11-2024, Status: Pending, Team: John, Alice, Bob, Sarah
```

#### Checking Overdue Tasks
```python
# View Overdue Tasks
Enter your choice (1-8): 7
Overdue Tasks:
Task ID: 4, Task: Weekly Report, Due Date: 13-11-2024, Status: Pending, Team: Manager, Analyst
```

### 4. File Operations

#### Saving Tasks to CSV
```python
# Save current tasks
Enter your choice (1-8): 4
Tasks saved to task_list.csv.

# CSV Format Example:
Task_ID,Description,Due Date,Type,Priority
1,Dentist Appointment,2024-11-20,personal,high
2,Client Presentation,2024-11-15,work,"John, Alice, Bob, Sarah"
```

#### Loading Tasks from CSV
```python
# Load tasks from file
Enter your choice (1-8): 5
Tasks loaded from task_list.csv.
```

### 5. Error Handling Examples

#### Invalid Date Format
```python
Enter task type (personal/work): personal
Enter task title: Gym Session
Enter due date (YYYY-MM-DD): 20-11-2024
Error: Invalid date format. Please use YYYY-MM-DD format.
```

#### Invalid Priority Level
```python
Enter task type (personal/work): personal
Enter task title: Reading
Enter due date (YYYY-MM-DD): 2024-11-20
Enter priority (high/medium/low): urgent
Error: Not a Valid Priority!
```

#### Invalid Task ID for Deletion
```python
Enter task ID to delete: 999
No task found with ID 999.
```

## Best Practices

1. **Regular Saving**
   - Save tasks regularly using the save option
   - Load from CSV when restarting the application

2. **Task Organization**
   - Use clear descriptions
   - Set appropriate priorities for personal tasks
   - Include all relevant team members for work tasks
     
3. **Grammatical errors in Priority and Task Type**
    -Write the commands correctly for optimum output

## Troubleshooting

Common issues and solutions:

1. **File Not Found Error**
   - Ensure CSV file exists in the correct directory
   - Check file permissions

2. **Invalid Date Format**
   - Use YYYY-MM-DD format
   - Ensure dates are valid

3. **Task Not Found**
   - Verify task ID exists
   - Refresh task list if recently modified

