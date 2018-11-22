touch compile.py
printf "import py_compile\npy_compile.compile(\"main.py\")" > compile.py
python3 compile.py
rm compile.py
cd __pycache__
mv * ../sleeptimer
cd ..
rm -rf __pycache__
chmod +x sleeptimer
sudo mv sleeptimer /usr/bin
printf "Done!\nType \"sleeptimer\" in your Bash terminal to launch.\n"
