import os

savepath = "%localappdata%/Packages/Microsoft.BadgerWin10_8wekyb3d8bbwe/SystemAppData/wgs"
savepath = os.path.join(savepath, os.listdir(savepath)[0])

with open(os.path.join(savepath, "containers.index"), "rb") as index:

  index.read(4)

  count = int.from_bytes(index.read(1))

  index.read(7)

  index.read(int.from_bytes(index.read(1)) * 2 + 15)

  index.read(int.from_bytes(index.read(1)) * 2 + 11)

  for j in range(int(count)):
    containerStrings = []

    for i in range(3):
      stringLength = int.from_bytes(index.read(1))
      index.read(3)

      containerStrings.append(index.read(stringLength*2).decode())
    
    index.read(5)

    test = index.read(16)

    index.read(24)

    newpath = os.path.join(savepath, (test[0:4][::-1]+test[4:6][::-1]+test[6:8][::-1]+test[8:16]).hex().replace("\0",""))

    out = os.path.join("com.mojang", containerStrings[1].replace("\0",""))

    os.makedirs(os.path.dirname(out), exist_ok=True)

    with open(out, "wb") as i:
      with open(os.path.join(newpath, os.listdir(newpath)[len(os.listdir(newpath)[0])!=32]), "rb") as k:
        i.write(k.read())