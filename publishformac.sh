rm -rf build
rm -rf dist
python3 ./Tools/generateversion.py
pyinstaller Program.py
cp -r ./Controllers ./dist/Program/
cp -r ./Library ./dist/Program/
cp -r ./Listener ./dist/Program/
cp -r ./Services ./dist/Program/
cp -r ./Views ./dist/Program/
mv ./dist/Program/Program ./dist/Program/kahla