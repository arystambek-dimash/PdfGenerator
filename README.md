# PDF Generator using Python

This Python script generates a PDF document based on data retrieved using the `get_by_bin_stat_egov` function from the `main` module. The generated PDF contains information related to the specified Business Identification Number (BIN).

## Prerequisites
- Install the required libraries:
  ```bash
  pip install pdfkit
  pip install Jinja2
  ```

- Ensure [wkhtmltopdf](https://wkhtmltopdf.org/) is installed on your system and set the correct path in the `configuration` variable.

## Usage

```python
import pdfkit
from main import get_by_bin_stat_egov
from jinja2 import Environment, FileSystemLoader

def pdf_generator(bin: str):
    # Retrieve data using the get_by_bin_stat_egov function
    stat_egov = get_by_bin_stat_egov(bin)

    # Extract content for the PDF
    content_to_draw = stat_egov['obj'].get('fio', '')
    file_name = f"{content_to_draw}_StatEgov.pdf"

    # Configure Jinja2 environment
    env = Environment(loader=FileSystemLoader(searchpath="./"))
    template = env.get_template('template.html')

    # Render HTML content using the retrieved data
    html_content = template.render(stat_egov['obj'])

    # Configure PDF generation with wkhtmltopdf path
    configuration = pdfkit.configuration(wkhtmltopdf='C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe')

    # Generate PDF from HTML content
    pdfkit.from_string(html_content, file_name, configuration=configuration)

# Example usage
pdf_generator('201040000013')
```

Make sure to replace the example BIN (`'201040000013'`) with the desired Business Identification Number for which you want to generate the PDF.

Note: Adjust the path to the `wkhtmltopdf.exe` executable in the `configuration` variable based on your system configuration.
