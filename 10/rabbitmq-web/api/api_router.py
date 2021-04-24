from fastapi import APIRouter
from api.api_models import Data
from api.backend.rpc_client import FibonacciRpcClient

router = APIRouter()

@router.get('/')
def test():
    return 'API is running'

@router.post('/calculate')
def calculate_fibonacci(inputData:Data):
    fibonacci_rpc = FibonacciRpcClient()

    print(" [x] Requesting fib(%s)" % inputData.fibNumber)
    response = fibonacci_rpc.call(inputData.fibNumber)
    print(" [.] Got %r" % response)

    return response