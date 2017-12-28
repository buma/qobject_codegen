<%namespace name="util" file="header.mako"/>
<%
  from python_func import internal_name
  params = []
  set_params = []
  for property in properties:
    params.append("{0}(other.{0})".format(internal_name(property["name"])))
    set_params.append("{}={};".format(internal_name(property["name"]), property["name"]))
%>
${util.renderIncludes(includes)}
${class_name}::${class_name}(QObject *parent) : QObject(parent)
{

}
${class_name}::${class_name}(const ${class_name} &other) :
    QObject(0),
    ${",\n    ".join(params)}
{

}
% if constructor_props:
${class_name}::${class_name}(QObject *parent, ${", ".join(constructor_props)}) :
   QObject(parent)
% endif
{
    ${"\n    ".join(set_params)}
}


## for property in filter(lambda prop: prop["read"], properties):
##  {func.getter(property["name"], property["type"])}
## endfor

