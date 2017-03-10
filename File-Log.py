
import os

#Used to recursively print folders and subfolders
def print_subfolders( start_location,text_file,index):
    
    folders = os.listdir(start_location)

    out = "<ul style='list-style-type:none'>"
    text_file.write(out)
    
    for name in folders:
        next_folder = os.path.join(start_location,name)
        if os.path.isdir(next_folder):
            text_file.write("<li>"+name)
            print_subfolders( next_folder,text_file,index+1)
            text_file.write("</li>")
        else:
            pass
    text_file.write("</ul>")
    
#Used to print the content above to a file
def create_html_file(directory):
    start_location = directory
    start_location = os.path.realpath(start_location)

    path,folder_name = os.path.split(start_location)
    filename = folder_name+".html"

    #Used to include the jquery library in the html file
    top_html = "<html><body><h2>"+"""<head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    </head>"""+folder_name+" Items"+"</h2>"

    #Used to create and include jquery functionality on the list items
    bottom_html = """<script>$('li').children().hide();$('li').click(function(){
    $(this).children().toggle();event.stopPropagation();});
    </script></body></html>"""

    with open(filename,"w") as text_file:
        text_file.write(top_html)
        print_subfolders(start_location,text_file,0)
        text_file.write(bottom_html)

create_html_fiile(".")
