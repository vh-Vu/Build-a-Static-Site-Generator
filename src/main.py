from textnode import TextNode
from blocks import generate_page
import os
import shutil

dir_path = os.path.dirname(os.path.dirname(__file__))
template_path = os.path.join(dir_path,'template.html')
static_path = os.path.join(dir_path,'static')
public_path = os.path.join(dir_path,'public')
content_path = os.path.join(dir_path,'content')

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
   
    copy_static(static_path,public_path)
    generate_page(os.path.join(content_path,'index.md'),template_path,public_path)

    #print(source,destination)




if __name__ == "__main__":
    main()