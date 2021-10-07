# First Assignment
import uuid
from datetime import datetime

Id = uuid.uuid1().int 
Name = input("Enter your name: ")
datetime = datetime.now()

print(f"Hello, {Name}\n Your Id number: {Id}\n Current date and time: {datetime}")