import grpc
from pb import todo_pb2 as todo
from pb import todo_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = todo_pb2_grpc.ToDoServiceStub(channel)
        '''
        PUT REPL CODE HERE
        ------------------
        This determines what the client can do with the server. 
        You can add, get, update, delete, list, and mark tasks as completed.
        '''
        