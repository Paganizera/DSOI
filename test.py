import sys
#import Image
#im1 = Image.open(sys.argv[1])

from pathlib import Path

path = Path("source/users.pkl")
path.mkdir(parents=True, exist_ok=True)
print(path)