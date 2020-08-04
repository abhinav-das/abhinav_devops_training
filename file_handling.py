# File Handling

import os
import random
from datetime import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))
new_file_path = os.path.join(current_dir, "file{}.txt".format("".join(str(datetime.now().timestamp()).split("."))))
random_file_size = random.randint(10240, 40960)
try:
    with open(new_file_path, "wb") as f:
        f.write(os.urandom(random_file_size))
    print("File Write complete")
except Exception as e:
    print("Error while writing to file : {}".format(e))

