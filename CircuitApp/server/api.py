from flask import Flask, request
from flask_restplus import Api, Resource, fields
import capacitorCircuit as capacitorCircuit
import inductorCircuit as inductorCircuit

flask_app = Flask(__name__)
app = Api(app = flask_app, 
		  version = "0.0.1", 
		  title = "Circuit Server API", 
		  description = "Manage circuit calculations input and output")

name_space = app.namespace('circuitServer', description='Manage Circuits')

modelCapacitor = app.model('CapacitorCircuit', 
		  			{'peakVoltage': fields.Float(required = True, 
					description="Voltage Signal of the circuit", 
					help="Cannot be blank."),
					'frequency': fields.Float(required = True, 
					description="Frequency value of the circuit", 
					help="Cannot be blank."),
					'resistor': fields.Float(required = True, 
					description="Resistor component value", 
					help="Cannot be blank."),
					'capacitor': fields.Float(required = True, 
					description="Capacitor component value", 
					help="Cannot be blank.")},
				)

modelInductor = app.model('InductorCircuit', 
		  			{'peakVoltage': fields.Float(required = True, 
					description="Voltage Signal of the circuit", 
					help="Cannot be blank."),
					'frequency': fields.Float(required = True, 
					description="Frequency value of the circuit", 
					help="Cannot be blank."),
					'resistor': fields.Float(required = True, 
					description="Resistor component value", 
					help="Cannot be blank."),
					'inductor': fields.Float(required = True, 
					description="Inductor component value", 
					help="Cannot be blank.")})

list_of_capacitor_circuits = {}
list_of_inductor_circuits = {}

capacitorType = 'capacitor'
inductorType = 'inductor'

@name_space.route("/<circuitType>/<int:id>")
class MainClass(Resource):

	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'id': 'Specify the Id associated with the circuit',
			 		  'circuitType': 'Specify the Circuit Type associated with the circuit' })
	def get(self, id, circuitType):
		try:
			if circuitType==capacitorType:
				circuit = list_of_capacitor_circuits[id]
				return {
					"status": "Circuit retrieved",
					"voltage" : circuit.peakVoltage,
					"frequency" : circuit.frequency,
					"resistor" : circuit.resistor,
					"capacitor" : circuit.capacitor
				}
			elif circuitType==inductorType:
				circuit = list_of_inductor_circuits[id]
				return {
					"status": "Circuit retrieved",
					"voltage" : circuit.peakVoltage,
					"frequency" : circuit.frequency,
					"resistor" : circuit.resistor,
					"inductor" : circuit.inductor
				}
			else:
				raise Exception("Circuit type not allowed")
		except KeyError as e:
			name_space.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
		except Exception as e:
			name_space.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

@name_space.route("/capacitor/<int:id>")
class CapacitorClass(Resource):
	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'id': 'Specify the Id associated with the circuit' })
	@app.expect(modelCapacitor)
	def post(self, id):
		try:
			voltageInput = request.json['peakVoltage']
			frequencyInput = request.json['frequency']
			resistorInput = request.json['resistor']
			capacitorInput = request.json['capacitor']
			list_of_capacitor_circuits[id] = capacitorCircuit.CapacitorCircuit(voltageInput, frequencyInput, resistorInput, capacitorInput)
			return {
				"status": "New circuit added",
				"voltage": list_of_capacitor_circuits[id].peakVoltage,
				"frequency": list_of_capacitor_circuits[id].frequency,
				"resistor": list_of_capacitor_circuits[id].resistor,
				"capacitor": list_of_capacitor_circuits[id].capacitor
			}
		except KeyError as e:
			name_space.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")
		except Exception as e:
			name_space.abort(400, e.__doc__, status = "Could not save information", statusCode = "400")

@name_space.route("/inductor/<int:id>")
class InductorClass(Resource):
	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'id': 'Specify the Id associated with the circuit' })
	@app.expect(modelInductor)
	def post(self, id):
		try:
			voltageInput = request.json['peakVoltage']
			frequencyInput = request.json['frequency']
			resistorInput = request.json['resistor']
			inductorInput = request.json['inductor']
			list_of_inductor_circuits[id] = inductorCircuit.InductorCircuit(voltageInput, frequencyInput, resistorInput, inductorInput)
			return {
				"status": "New circuit added",
				"voltage": list_of_inductor_circuits[id].peakVoltage,
				"frequency": list_of_inductor_circuits[id].frequency,
				"resistor": list_of_inductor_circuits[id].resistor,
				"inductor": list_of_inductor_circuits[id].inductor
			}
		except KeyError as e:
			name_space.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")
		except Exception as e:
			name_space.abort(400, e.__doc__, status = "Could not save information", statusCode = "400")