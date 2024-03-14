from task_package.create_task import create_task
from task_package.edit_task import edit_task
from task_package.categorize_task import categorize_task

#create a task
task1 = create_task("Complete Your Assignment","Finish TASK MANAGEMENT SYSTEM")

#Display the task
print("Task 1:",task1)

#edit the task
edit_task(task1,new_title="Updated Assignment",new_description="Review and submit to Rashmi Mam")

#Display the update task
print("Updated Task 1:",task1)

#categorize the task
categorize_task(task1,"Zappkode Academy")

#display the categorized task
print("Categorized Task 1:",task1)