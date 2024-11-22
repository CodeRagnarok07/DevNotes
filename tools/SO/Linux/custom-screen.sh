##https://ubuntuhandbook.org/index.php/2017/04/custom-screen-resolution-ubuntu-desktop/
##cvt 1680 1050
##sudo xrandr --newmode "1680x1050_60.00"  146.25  1680 1784 1960 2240  1050 1053 1059 1089 -hsync +vsync
##sudo xrandr --addmode VGA-1 "1680x1050_60.00"


script='xrandr --newmode "1680x1050_60.00"  146.25  1680 1784 1960 2240  1050 1053 1059 1089 -hsync +vsync && xrandr --addmode VGA-1 "1680x1050_60.00" && xrandr --output VGA-1 --mode "1680x1050_60.00"'

echo $script > ~/.config/screem.sh
chmod +x ~/.config/screem.sh
echo ~/.config/screem.sh >> .profile


