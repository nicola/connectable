from connectable.connector import Connector
a = Connector()
a.add_input("a", "b")
c =  a.inputs()
c["z"] = "q";
print a.inputs()