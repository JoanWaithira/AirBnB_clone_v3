from models import storage
from models.state import State

print(storage.get(State, 'dec5b901-7ead-4417-a229-d523e7505b34').name)
