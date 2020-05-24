from flask import Flask, request
from flask_restplus import Api, Resource, fields
from flask_cors import CORS
import fillTemplate as templateFile
import runCircuit as runCircuit

flask_app = Flask(__name__)
CORS(flask_app)
app = Api(app = flask_app, 
		  version = "0.0.1", 
		  title = "Circuit Server API", 
		  description = "Manage circuit calculations input and output")

name_space = app.namespace('circuitServer', description='Manage Circuits')

modelCapacitor = app.model('CapacitorCircuit', 
		  			{'peakVoltage': fields.String(required = True, 
					description="Voltage Signal of the circuit", 
					help="Cannot be blank."),
					'frequency': fields.String(required = True, 
					description="Frequency value of the circuit", 
					help="Cannot be blank."),
					'resistor': fields.String(required = True, 
					description="Resistor component value", 
					help="Cannot be blank."),
					'capacitor': fields.String(required = True, 
					description="Capacitor component value", 
					help="Cannot be blank.")},
				)

modelInductor = app.model('InductorCircuit', 
		  			{'peakVoltage': fields.String(required = True, 
					description="Voltage Signal of the circuit", 
					help="Cannot be blank."),
					'frequency': fields.String(required = True, 
					description="Frequency value of the circuit", 
					help="Cannot be blank."),
					'resistor': fields.String(required = True, 
					description="Resistor component value", 
					help="Cannot be blank."),
					'inductor': fields.String(required = True, 
					description="Inductor component value", 
					help="Cannot be blank.")})

@name_space.route("/capacitor")
class CapacitorClass(Resource):
	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
	@app.expect(modelCapacitor)
	def post(self):
		try:
			voltageInput = request.json['peakVoltage']
			frequencyInput = request.json['frequency']
			resistorInput = request.json['resistor']
			capacitorInput = request.json['capacitor']

			templateFile.CRcircuit(voltageInput, frequencyInput, resistorInput, capacitorInput)
			templateFile.RCcircuit(voltageInput, frequencyInput, resistorInput, capacitorInput)

			runCircuit.CRcircuit()
			runCircuit.RCcircuit()
			return {
				"status": "New circuit added",
				"voltage": voltageInput,
				"frequency": frequencyInput,
				"resistor": resistorInput,
				"capacitor": capacitorInput
			}
		except KeyError as e:
			name_space.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")
		except Exception as e:
			name_space.abort(400, e.__doc__, status = "Could not save information", statusCode = "400")

@name_space.route("/inductor")
class InductorClass(Resource):
	@app.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
	@app.expect(modelInductor)
	def post(self):
		try:
			voltageInput = request.json['peakVoltage']
			frequencyInput = request.json['frequency']
			resistorInput = request.json['resistor']
			inductorInput = request.json['inductor']

			templateFile.LRcircuit(voltageInput, frequencyInput, resistorInput, inductorInput)
			templateFile.RLcircuit(voltageInput, frequencyInput, resistorInput, inductorInput)

			runCircuit.LRcircuit()
			runCircuit.RLcircuit()
			return {
				"status": "New circuit added",
				"voltage": voltageInput,
				"frequency": frequencyInput,
				"resistor": resistorInput,
				"inductor": inductorInput
			}
		except KeyError as e:
			name_space.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")
		except Exception as e:
			name_space.abort(400, e.__doc__, status = "Could not save information", statusCode = "400")