from collections import namedtuple
import python_func as p_f


ClassModel = namedtuple('ClassModel', 'name properties')

def clean_properties(property):
    to_remove_list = [
            "count",
            "destruct",
            "save",
            "undo"
            ]
    for to_remove in to_remove_list:
        del property[to_remove]
    name = property["name"]
    property["getter"] = p_f.getter_name(name)
    property["setter"] = p_f.setter_name(name)
    property["notify_name"] = p_f.notify_name(name)
    property["internal"] = p_f.internal_name(name)
    return property

def make_model(data):
    properties = list(map(clean_properties, data["ClassProp"]))
    classes = []
    for class_model in data["ClassModel"]:
        name = class_model["name"]
        class_properties_idx = class_model["properties"]
        class_properties = list(properties[i] for i in class_properties_idx)
        print (name, [property["name"] for property in class_properties])
        class_ = ClassModel(name=name, properties=class_properties)
        classes.append(class_)
    return classes

if __name__ == "__main__":
    import json
    data = json.load(open("../coder/project.json", "r"))
    model = make_model(data)

