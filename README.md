# FlightData

This program is designed to retrieve and visualize flight data for a specific plane based on the plane's call number. The program uses the OpenSky API, which is a free and open-source API that provides real-time and historical flight data for civil aircrafts. When the program is run, it prompts the user to input a plane's call sign and then uses this information to make a request to the OpenSky API. The API returns the flight data in JSON format, which the program parses into a pandas DataFrame.

The program then filters the flight data for the specific plane using its call sign and plots the latitude and longitude data using the matplotlib library. This allows the user to see the flight path of the plane on a map, which can be useful for understanding the plane's movements and routes.

One of the main benefits of this program is that it allows users to retrieve and visualize flight data in real-time, which can be useful for a variety of applications such as aviation, logistics, transportation, and security. For example, airline companies could use this program to track their fleet and monitor the performance of their aircrafts. Additionally, this program may be useful to security forces, to monitor the flight of certain planes over a certain area.

It's important to note that, since this is an open-source API, the flight data might be incomplete or have a latency, and it might be limited by number of request and usage, check the documentation and usage limitation before using it.
