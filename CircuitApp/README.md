# Circuit App

## Description

This is a Circuit Simulator which calculates High-Pass Filters and Low-Pass Filters. User will have four circuit options:

- Circuit RC;
- Circuit CR;
- Circuit RL;
- Circuit LR.

Each circuit will be calculated based on inputs that user will write on interface of application.

## Software Development Life Cycle Process

The steps followed for the software development was based on Waterfall life cycle.

1. First, some architecture drawing was made. This drawing can be found on path `charts/AppArchitecture.pdf`.

2. Then, interface design was made using _Figma_ software. The interface design can be found clicking on the link below:

- [Front-End Design](https://www.figma.com/file/mnsnZnp8nyn1JmprzjsGlL/Frequency-Filter-Calculator?node-id=0%3A1)

3. Finally, the development process could be accomplished.

## Software Modules

### Server

Server module consists in a Python application. _Flask_ and _Swagger_ frameworks were used in order to develop this server.

Basically *Flask* is the framework which permits that you can configure routes for your server and *Swagger* permits that you can access a
simple interface in order to test server using JSON files and where you can see models which server will use on GET and POST methods.

On this application, server will receive user inputs and will send this information to _Ngspice_ where the circuit will be simulated and, finally,
will generate results about this circuit simulation.

### Interface

The interface was developed in order to provide for users a simple and usual view where users can easily write values for each component
of the circuit analyzed.

Basically, user can choose what circuit he/she wants to analyze, provide values for the components and then ask to simulate circuits. On this final step
user will click on a button `Send to Server` which will get all the inputs and send to server in order to simulate the circuit.

Finally, the final results will be generate and the interface will be allowed to show the graph about circuit analyzed.

## References

- [Flask API](https://towardsdatascience.com/working-with-apis-using-flask-flask-restplus-and-swagger-ui-7cf447deda7f)
- [Flask on Visual Code](https://code.visualstudio.com/docs/python/tutorial-flask)

## Observations

- IDE used: VS Code;
- Next steps: deploy the application on a Heroku Container with proper environment for the application.
