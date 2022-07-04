# modbus-mqtt-plotserver
Build and deploy three deb packages to read modbus data and send it to a local plot server with mqtt in between.
![](architecture.png?raw=true "Architecture of Modbus visualization")

* `modbus4mqtt`: system service based on the [modbus4mqtt Python library](https://github.com/tjhowse/modbus4mqtt)
* `plotserver`: system service based on the [http-plot-server Python library](https://pypi.org/project/http-plot-server/)
* `mqtt2plotserver`: system service as interface between the other two services
