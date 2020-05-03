from flask import Flask, request
from flask_restplus import Api, Resource, fields
import circuitEntity as entity

flask_app = Flask(__name__)
app = Api(app = flask_app, 
		  version = "0.0.1", 
		  title = "Circuit Server API", 
		  description = "Manage circuit calculations input and output")

name_space = app.namespace('circuitServer', description='Manage Circuits')

model = app.model('Circuit', 
		  			{'voltage': fields.Float(required = True, 
					description="Voltage Signal of the circuit", 
					help="Cannot be blank."),
					'current': fields.Float(required = True, 
					description="Current Signal of the circuit", 
					help="Cannot be blank."),
					'frequency': fields.Float(required = True, 
					description="Frequency value of the circuit", 
					help="Cannot be blank.")})

list_of_circuits = {}

@name_space.route("/<int:id>")
class MainClass(Resource):

	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'id': 'Specify the Id associated with the circuit' })
	def get(self, id):
		try:
			circuit = list_of_circuits[id]
			return {
				"status": "Circuit retrieved",
				"voltage" : circuit.voltage,
				"current" : circuit.current,
				"frequency" : circuit.frequency
			}
		except KeyError as e:
			name_space.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
		except Exception as e:
			name_space.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'id': 'Specify the Id associated with the circuit' })
	@app.expect(model)		
	def post(self, id):
		try:
			voltageInput = request.json['voltage']
			currentInput = request.json['current']
			frequencyInput = request.json['frequency']
			list_of_circuits[id] = entity.Circuit(voltageInput, currentInput, frequencyInput)
			return {
				"status": "New circuit added",
				"voltage": list_of_circuits[id].voltage,
				"current": list_of_circuits[id].current,
				"frequency": list_of_circuits[id].frequency
			}
		except KeyError as e:
			name_space.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")
		except Exception as e:
			name_space.abort(400, e.__doc__, status = "Could not save information", statusCode = "400")