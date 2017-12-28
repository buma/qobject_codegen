<%def name="getter(getter_name, internal_name, type)">
${type} ${getter_name}() const { return ${internal_name}; } \
</%def>
<%def name="setter(setter_name, internal_name, notify_name, name, type)">
void ${setter_name}(${type} ${name}) {
    if (${name} != ${internal_name}) {
    	${internal_name} = ${name};
	emit ${notify_name}();
    }
}\
</%def>
<%def name="property(property)">
  Q_PROPERTY(${property["type"]} ${property["name"]} \
% if property["read"]:
READ ${property["getter"]} \
% endif
% if property["write"]:
WRITE ${property["setter"]} \
% endif
% if property["notify"]:
NOTIFY ${property["notify_name"]} \
% endif
) \
</%def>


