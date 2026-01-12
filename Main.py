import Setup as Setup
import PhotoPhilter as Pp
import FinalSort as Fs
# TODO technically it would make more sense if all JSON files are made in Main.py.
#  That would mean settings.json and future JSONs.

# TODO extract a class that allows for easier communication with JSON files.
#  There's a lot of redundant code with the JSON Files
setup = Setup.App()
setup.mainloop()

app = Pp.App()
app.mainloop()

final_sort = Fs.App()
final_sort.mainloop()
