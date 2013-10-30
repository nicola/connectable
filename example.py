from droidable.droid import Droid
a = Droid()
a.add_input("a", "b")
c =  a.inputs()
c["z"] = "q";
print a.inputs()