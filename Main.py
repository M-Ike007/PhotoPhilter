import Setup as Setup
import PhotoPhilter as Pp

# TODO technically it would make more sense if all JSON files are made in Main.py.
#  That would mean settings.json and future JSONs.





setup = Setup.App()
setup.mainloop()

app = Pp.App()
app.mainloop()
