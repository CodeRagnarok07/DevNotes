

wsl intall Ubuntu

```
docker run -t --name wsl_export alpine ls 

docker export wsl_export > ./alpine.tar
```


Add Alacritty

Add Nerd Fonts


## Open ports

netsh advfirewall firewall add rule name="Open Port 42102" dir=in action=allow protocol=TCP localport=42102
netsh advfirewall firewall show rule name="Open Port 42102"

check all ports `netstat -aon`

find a port open `netstat -aon | findstr :<port_number>`



