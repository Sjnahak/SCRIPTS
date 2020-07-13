from pathlib import Path

path = Path("D:\Hello_world")
print(path.exists())

### to create dir print(path.mkdir())

path1 = Path()
for file in (path1.glob('*.py')):## to iterate over a dir
    print (file)
#print(path.glob('*.txt'))
