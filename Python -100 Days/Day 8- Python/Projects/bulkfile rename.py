import os 


def index():
    i = 0  # files count in folder
    path = "/Users/ajeetmacbookm2/Desktop/demo"


    for filename in os.listdir(path):
      my_files = "img" + str(i)+ ".jpeg"
      my_source = os.path.join(path, filename)         # old file path
      my_target = os.path.join(path, f"img{i}.jpeg")  # new file path
      os.rename(my_source,my_files)

    i = i+1

if __name__ == "__main__":
 index()





