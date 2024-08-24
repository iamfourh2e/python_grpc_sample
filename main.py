import os
import sys
from concurrent import futures

import grpc

sys.path.append(os.path.join(os.path.dirname(__file__), 'pb'))

from pb import greeter_pb2_grpc
from repo import greet_repo


def serve():
    server = grpc.server(thread_pool=futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(greet_repo.GreeterServicer(), server)
    server.add_insecure_port('[::]:50051')
    print('Server started on port 50051')
    server.start()
    server.wait_for_termination()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    serve()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
