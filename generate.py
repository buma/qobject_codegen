import logging
import os

from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions

lp = TemplateLookup(directories=["./templates"],
        module_directory='/tmp/mako_modules')

log = logging.getLogger(__name__)

logging.basicConfig(level="DEBUG")


def serve_template(templatename, **kwargs):
    try:
        mytemplate = lp.get_template(templatename)
        return mytemplate.render(**kwargs)
    except:
        log.error(exceptions.text_error_template().render(), exc_info=True)
    return None

setter_f = "set{}"
getter_f = "{}"
notify_f = "{}Changed"

def generate_code(path, classes):
    log.debug("Generating code in %s" % path)
    for class_ in classes:
        generate_header(path, class_)
        generate_implementation(path, class_)
        break


#def make_constructors(class_):


def generate_header(path, class_):
    fname = "{}.hpp".format(class_.name.lower())
    log.debug("Making %s" % fname)
    data = {}
    data["guard"] = "{}_HPP".format(class_.name.upper())
    data["class_name"] = class_.name

    ignored_includes = set(["bool", "int", "double"])

    includes = []
    includes.append("<QObject>")
    for property in class_.properties:
        log.debug("Looking property:%s" % property)
        if property["type"] in ignored_includes:
            continue
        if property["type"].startswith("Q"):
            property_type = "<{}>".format(property["type"])
        else:
            property_type = '"{}"'.format(property["type"])
        if property_type not in includes:
            includes.append(property_type)

    data["includes"] = includes
#TODO: set if all are needed, set by reference/value/pointer
    data["constructor_props"] = ("{} {}".format(prop["type"], prop["name"]) for prop in class_.properties)
    data["properties"] = class_.properties

#Make getters
    

    out = serve_template("header.mako",**data)
    if out:
        with open(os.path.join(path, fname), "w") as f:
            f.write(out)

def generate_implementation(path, class_):
    fname = "{}.cpp".format(class_.name.lower())
    log.debug("Making %s" % fname)
    data = {}
    data["class_name"] = class_.name
#TODO: set if all are needed, set by reference/value/pointer
    data["constructor_props"] = ("{} {}".format(prop["type"], prop["name"]) for prop in class_.properties)
    data["properties"] = class_.properties
    data["includes"] = ["\"{}.hpp\"".format(class_.name.lower())]
    out = serve_template("class.mako",**data)
    if out:
        with open(os.path.join(path, fname), "w") as f:
            f.write(out)

if __name__ == "__main__":
    from read import make_model
    import json
    data = json.load(open("../coder/project.json", "r"))
    model = make_model(data)
    generate_code("./out", model)
    #print (serve_template("header_func.mako", name="nekaj"))
