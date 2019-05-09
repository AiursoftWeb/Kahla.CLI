rm -rf build
rm -rf dist
pyinstaller -F Program.py
cp -r ./Controllers ./dist/Program/
cp -r ./Library ./dist/Program/
cp -r ./Listener ./dist/Program/
cp -r ./Services ./dist/Psrogram/
cp -r ./Views ./dist/Program/
mv ./dist/Program/Program ./dist/Program/kahla
