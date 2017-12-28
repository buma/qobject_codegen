<%namespace name="func" file="header_func.mako"/>
#ifndef ${guard}
#define ${guard}
<%def name="renderIncludes(includes)">
% for include in includes:
#include ${include}
% endfor
</%def>

${renderIncludes(includes)}

class ${class_name} : public QObject {
  Q_OBJECT
% for property in properties:
  ${func.property(property)}\
% endfor

public:
  explicit ${class_name}(QObject *parent = 0);
  ${class_name}(const ${class_name} &other);
% if constructor_props:
  ${class_name}(QObject *parent, ${", ".join(constructor_props)});
% endif
## Getters
% for property in filter(lambda prop: prop["read"], properties):
${func.getter(property["getter"], property["internal"], property["type"])}\
% endfor
## setters
% for property in filter(lambda prop: prop["write"], properties):
${func.setter(property["setter"], property["internal"], property["notify_name"], property["name"], property["type"])}
% endfor
signals:
% for property in filter(lambda prop: prop["notify"], properties):
  void ${property["notify_name"]}();
% endfor
public slots:
private:
% for property in properties:
  ${property["type"]} ${property["internal"]};
% endfor

};

#endif // ${guard}
