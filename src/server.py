import grpc
from pb import todo_pb2
from pb import todo_pb2_grpc

class ToDoService(todo_pb2_grpc.ToDoServiceServicer):

    def __init__(self):
        # Initialize your data storage here (e.g., a list or a database connection)
        self.tasks = {}
        self.TaskID = 0

    def AddTask(self, request, context):
        self.TaskID += 1
        new_task = todo_pb2.Task(id=self.TaskID, title=request.title, description=request.description)
        self.tasks[self.TaskID] = new_task
        return new_task

    def GetTask(self, request, context):
        return self.tasks.get(request.id, todo_pb2.Task(id=-1, title="Phony Task", description="No task was found. Sending dummy task."))

    def UpdateTask(self, request, context):
        update_task = self.tasks.get(request.id)
        if not update_task:
            return todo_pb2.Task(id=-1, title="Phony Task", description="No task was found. Sending dummy task.")

        # Update the task fields
        update_task.title = request.title
        update_task.description = request.description

        return update_task
                l = mid + 1
            else:
                r = mid - 1
        
        return todo_pb2.Task(id=-1, title="Phony Task", description="No task was found. Sending dummy task.")

    def UpdateTask(self, request, context):
        update_task

        return todo_pb2.Task(id=request.id, title=request.title, description=request.description)

    def DeleteTask(self, request, context):
        # Implement your logic to delete a task here
        return todo_pb2.Task(id=request.id)
    
    def ListTasks(self, request, context):
        # Implement your logic to list 
        return todo_pb2.TaskList(tasks)
    
    def MarkTaskCompleted(self, request, context):
        # Implement your logic to mark a task as completed here
        # Task.Completed = True
        return todo_pb2.Task(id=request.id, title="Sample Task", description="This is a sample task.", completed=True)