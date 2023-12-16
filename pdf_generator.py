import pdfkit
from main import get_by_bin_stat_egov
from jinja2 import Environment, FileSystemLoader


def pdf_generator(bin: str):
    stat_egov = get_by_bin_stat_egov(bin)

    content_to_draw = stat_egov['obj'].get('fio', '')
    file_name = f"{content_to_draw}_StatEgov.pdf"
    env = Environment(
        loader=FileSystemLoader(searchpath="./"))
    template = env.get_template('template.html')

    html_content = template.render(stat_egov['obj'])

    configuration = pdfkit.configuration(wkhtmltopdf='C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe')

    pdfkit.from_string(html_content, file_name, configuration=configuration)


pdf_generator('201040000013'
