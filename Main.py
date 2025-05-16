import Setup as Setup
import PhotoPhilter as Pp
import FinalSort as Fs
# TODO technically it would make more sense if all JSON files are made in Main.py.
#  That would mean settings.json and future JSONs.

setup = Setup.App()
setup.mainloop()

app = Pp.App()
app.mainloop()

final_sort = Fs.App()
final_sort.mainloop()
