import grpc
from pb import todo_pb2
from pb import todo_pb2_grpc

class ToDoService(todo_pb2_grpc.ToDoServiceServicer):

    def __init__(self):
        # Simple Task Storage (In-memory)
        self.tasks = {}
        self.TaskID = 0
        self.OldTaskIDPool = []

    def AddTask(self, request, context):
        if self.OldTaskIDPool:
            self.TaskID = self.OldTaskIDPool.pop(0)
        else:
            self.TaskID += 1

        new_task = todo_pb2.Task(id=self.TaskID, title=request.title, description=request.description)
        self.tasks[self.TaskID] = new_task
        return new_task

    def GetTask(self, request, context):
        task = self.tasks.get(request.id)
        if task is None:
            context.abort(grpc.StatusCode.NOT_FOUND, f"Task with id {request.id} not found")
        return task

    def UpdateTask(self, request, context):
        update_task = self.tasks.get(request.id)
        if not update_task:
            context.abort(grpc.StatusCode.NOT_FOUND, f"Task with id {request.id} not found")

        # Update the task fields
        if not request.title and not request.description:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "At least one field (title or description) must be provided")

        if request.title:
            update_task.title = request.title
        if request.description:
            update_task.description = request.description

        return update_task

    def DeleteTask(self, request, context):
        removed_task = self.tasks.pop(request.id, None)
        if removed_task is None:
            context.abort(grpc.StatusCode.NOT_FOUND, f"Task with id {request.id} not found")
        return removed_task

    def ListTasks(self, request, context):
        return todo_pb2.TaskList(tasks=list(self.tasks.values()))
    
    def MarkTaskCompleted(self, request, context):
        task = self.tasks.get(request.id)
        if task is None:
            context.abort(grpc.StatusCode.NOT_FOUND, f"Task with id {request.id} not found")
        task.completed = True
        return task