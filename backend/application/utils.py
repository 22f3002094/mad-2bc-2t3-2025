from jinja2 import Template


def prepare_temp(html_file_name , data):
    with open(html_file_name , "r") as file:
        template = Template(file.read() )
        output_html = template.render( data = data)
        return output_html