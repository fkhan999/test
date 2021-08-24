import pathlib
for path in pathlib.Path("d:\\GITHUB\\test\\honey").iterdir():
	if path.is_file():
		with open(path, "r") as f:
			contents = f.readlines()
		contents.insert(3, "\nharshjot edit\n          farrukh edit111")
		with open(path, "w") as f:
			contents = "".join(contents)
			f.write(contents)
