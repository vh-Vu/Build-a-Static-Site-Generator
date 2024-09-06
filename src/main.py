from textnode import TextNode
import os
import shutil

def copy_static(source,destination):
    delete_item =lambda path_dir: os.remove(path_dir) if os.path.isfile(path_dir) else shutil.rmtree(path_dir)
    list(map(lambda x: delete_item(os.path.join(destination,x)),os.listdir(destination)))
    def copy_and_paste(source,destination):
        lists = os.listdir(source)
        if lists:
            for name in lists:
                path_dir = os.path.join(source,name)
                if os.path.isfile(path_dir):
                    shutil.copy(path_dir,destination)
                    print(f'Copy [{path_dir}] to [{destination}]')
                else:
                    new_dir = os.path.join(destination,name)
                    os.mkdir(new_dir)
                    print(f'Create new folder {name} in {destination}')
                    copy_and_paste(path_dir,new_dir)
        return
    copy_and_paste(source,destination)
    print("Copy Sucessfully!")

def main():
    dir_path = os.path.dirname(os.path.dirname(__file__))
    source = os.path.join(dir_path,'static')
    destination = os.path.join(dir_path,'public')
    copy_static(source,destination)
    #print(source,destination)




if __name__ == "__main__":
    main()