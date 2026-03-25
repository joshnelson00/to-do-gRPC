import grpc
from pb import todo_pb2 as todo
from pb import todo_pb2_grpc


def print_header(title):
    line = "=" * 64
    print(f"\n{line}")
    print(f"{title:^64}")
    print(line)


def print_menu():
    print_header("To-Do gRPC Client")
    print("[1] List Tasks")
    print("[2] Add Task")
    print("[3] Update Task")
    print("[4] Delete Task")
    print("[5] Mark Task As Completed")
    print("[6] Exit")
    print("-" * 64)


def print_task_list(tasks):
    print_header("Task List")
    if not tasks:
        print("No tasks found.")
        print("-" * 64)
        return

    print(f"{'ID':<6}{'Status':<12}{'Title':<22}Description")
    print("-" * 64)
    for task in tasks:
        status = "DONE" if task.completed else "PENDING"
        print(f"{task.id:<6}{status:<12}{task.title:<22}{task.description}")
    print("-" * 64)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = todo_pb2_grpc.ToDoServiceStub(channel)
        
        while True:
            print_menu()
            choice = input("Select an option [1-6]: ").strip()
            if not choice.isdigit():
                print("Invalid input. Enter a number from 1 to 6.")
                continue
            choice = int(choice)
            match choice:
                case 1:
                    response = stub.ListTasks(todo.Empty())
                    print_task_list(response.tasks)
                case 2:
                    title = input("Enter task title: ")
                    description = input("Enter task description: ")
                    new_task = todo.Task(title=title, description=description)
                    response = stub.AddTask(new_task)
                    print(f"Added task #{response.id}: {response.title}")
                case 3:
                    task_id = int(input("Enter task ID to update: ").strip())
                    title = input("Enter new task title: ")
                    description = input("Enter new task description: ")
                    updated_task = todo.Task(id=task_id, title=title, description=description)
                    response = stub.UpdateTask(updated_task)
                    print(f"Updated task #{response.id}: {response.title}")
                case 4:
                    task_id = int(input("Enter task ID to delete: ").strip())
                    response = stub.DeleteTask(todo.TaskId(id=task_id))
                    print(f"Deleted task #{response.id}: {response.title}")
                case 5:
                    task_id = int(input("Enter task ID to mark as completed: ").strip())
                    response = stub.MarkTaskCompleted(todo.TaskId(id=task_id))
                    print(f"Marked task #{response.id} as completed")
                case 6:
                    print_header("Goodbye")
                    break

if __name__ == '__main__':
    run()

