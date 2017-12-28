#Names for variables
getter_name = lambda name: name
setter_name = lambda name: "set{}".format(name.title())
internal_name = lambda name: "m_{}".format(name)
notify_name = lambda name: "{}Changed".format(name)
