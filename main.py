from jinja2 import Environment, FileSystemLoader
import pandas as pd
import datetime
import pytz

def main():
    quotes = pd.read_csv("template/facts.csv").sample(n=1)['Quotes'].values[0]
    template_vars = {
            "quotes" : quotes
        }
    env = Environment(loader=FileSystemLoader("template"))
    template = env.get_template("template.html")
    output_from_parsed_template = template.render(template_vars)
    with open("index.html", "w+") as fh:
        fh.write(output_from_parsed_template)

    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    format_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    template_vars = {
            "timestamp" : format_time,
            "fact" : quotes
        }
    
    env = Environment(loader=FileSystemLoader("template"))
    template = env.get_template("readme.html")
    output_from_parsed_template = template.render(template_vars)
    with open("README.md", "w+") as fh:
        fh.write(output_from_parsed_template)


    return

if __name__ == "__main__":
    main()