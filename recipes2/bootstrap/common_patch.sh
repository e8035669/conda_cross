

sed -i 's/linux-gnu-/linux-gnueabihf-/g' $@
sed -i 's/linux-gnu"/linux-gnueabihf"/g' $@
sed -i "s/linux-gnu\//linux-gnueabihf\//g" $@

