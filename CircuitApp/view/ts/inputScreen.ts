var baseURL = 'http://localhost:5000/'
var regex = /[^0-9.knuMm]/g
var waitTime = 5000

function createBodyTemplate() {
    var circuit = getCircuit()

    buildTitle(circuit)
    buildCircuitFields(circuit)
}

function getCircuit() {
    var url = new URL(window.location.href);
    var circuit = url.searchParams.get("circuit");
    return circuit;
}

function goToMainPage() {
    window.location.assign('../index.html');
}

function sendToServer() {
    var circuit = getCircuit();
    var url=baseURL + 'circuitServer/'

    var peakVoltage = (<HTMLInputElement>document.getElementById("peakVoltage")).value;
    var frequency = (<HTMLInputElement>document.getElementById("frequency")).value;
    var resistor = (<HTMLInputElement>document.getElementById("resistor")).value;
    var initialTime = (<HTMLInputElement>document.getElementById("initialTime")).value;
    var finalTime = (<HTMLInputElement>document.getElementById("finalTime")).value;

    if(!resistor && !frequency && !peakVoltage && !initialTime && !finalTime) {
        addMessageEmptyFields()
        return;
    }
    
    var data;

    if(String(circuit).includes('C')) {
        url+='capacitor'
        var capacitor = (<HTMLInputElement>document.getElementById("capacitor")).value;
        if(!capacitor) {
            addMessageEmptyFields()
            return;
        }
        data = {
            "peakVoltage": peakVoltage,
            "frequency": frequency,
            "resistor": resistor,
            "capacitor": capacitor,
            "initialTime": initialTime,
            "finalTime": finalTime
        }
    } else {
        url+='inductor'
        var inductor = (<HTMLInputElement>document.getElementById("inductor")).value;
        if(!inductor) {
            addMessageEmptyFields()
            return;
        }
        data = {
            "peakVoltage": peakVoltage,
            "frequency": frequency,
            "resistor": resistor,
            "inductor": inductor,
            "initialTime": initialTime,
            "finalTime": finalTime
        }
    }

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    addLoader()

    setTimeout(function(){
        goToResultScreen()
    }, waitTime)

}

function addLoader() {
    document.getElementById("feedBackMessages").innerHTML=""

    var divCircuitLoader = 
                    `<div class="alert alert-info">
                        <strong>Info!</strong> Sending data to Server. Please Wait...
                    </div>
                    <br></br>`;
    
    var divCircuitLoaderTag = document.createElement("div");
    divCircuitLoaderTag.innerHTML = divCircuitLoader;
    document.getElementById("feedBackMessages").appendChild(divCircuitLoaderTag);
}

function validatePeakVoltageField(){
    var textInput = (<HTMLInputElement>document.getElementById("peakVoltage")).value;
    textInput = textInput.replace(regex, "");
    (<HTMLInputElement>document.getElementById("peakVoltage")).value = textInput;
}

function validateResistorField(){
    var textInput = (<HTMLInputElement>document.getElementById("resistor")).value;
    textInput = textInput.replace(regex, "");
    (<HTMLInputElement>document.getElementById("resistor")).value = textInput;
}

function validateFrequencyField(){
    var textInput = (<HTMLInputElement>document.getElementById("frequency")).value;
    textInput = textInput.replace(regex, "");
    (<HTMLInputElement>document.getElementById("frequency")).value = textInput;
}

function validateCapacitorField(){
    var textInput = (<HTMLInputElement>document.getElementById("capacitor")).value;
    textInput = textInput.replace(regex, "");
    (<HTMLInputElement>document.getElementById("capacitor")).value = textInput;
}

function validateInductorField(){
    var textInput = (<HTMLInputElement>document.getElementById("inductor")).value;
    textInput = textInput.replace(regex, "");
    (<HTMLInputElement>document.getElementById("inductor")).value = textInput;
}

function validateInitialTimeField() {
    var textInput = (<HTMLInputElement>document.getElementById("initialTime")).value;
    textInput = textInput.replace(regex, "");
    (<HTMLInputElement>document.getElementById("initialTime")).value = textInput;
}

function validateFinalTimeField() {
    var textInput = (<HTMLInputElement>document.getElementById("finalTime")).value;
    textInput = textInput.replace(regex, "");
    (<HTMLInputElement>document.getElementById("finalTime")).value = textInput;
}

function addMessageEmptyFields() {
    document.getElementById("feedBackMessages").innerHTML=""

    var divCircuitEmptyMessage = 
                    `<div class="alert alert-warning">
                        <strong>Warning!</strong> There are empty fields. Please fill them before send to server.
                    </div>
                    <br></br>`;
    
    var divCircuitEmptyMessageTag = document.createElement("div");
    divCircuitEmptyMessageTag.innerHTML = divCircuitEmptyMessage;
    document.getElementById("feedBackMessages").appendChild(divCircuitEmptyMessageTag);
}

function goToResultScreen(){
    window.location.assign('../html/resultScreen.html?circuit=' + getCircuit());
}

function buildTitle(circuit) {
    var divCircuitTitle = 
        `<div class="text-center">
            <h1>
                Circuit ${circuit}
            </h1>
        </div>`;
    
    var divCircuitTitleTag = document.createElement("div");
    divCircuitTitleTag.innerHTML = divCircuitTitle;
    document.getElementById("title").appendChild(divCircuitTitleTag);
}

function buildCircuitFields(circuit) {
    var circuitTypeTemplate;
    if(String(circuit).includes('C')) {
        circuitTypeTemplate=
        `<div class="form-group row">
            <label for="capacitor" class="col-sm-2 col-form-label">Capacitor (C)</label>
            <div class="col-sm-10">
            <input type="text" oninput="validateCapacitorField()" class="form-control" id="capacitor" placeholder="Capacitor (Faraday)">
            </div>
        </div>`
    } else {
        circuitTypeTemplate=
        `<div class="form-group row">
            <label for="inductor" class="col-sm-2 col-form-label">Inductor (L)</label>
            <div class="col-sm-10">
            <input type="text" oninput="validateInductorField()" class="form-control" id="inductor" placeholder="Inductor (Henry)">
            </div>
        </div>`
    }
    formTemplate+=circuitTypeTemplate

    var divCircuitImages = 
        `<div class="text-center">
            <img src="../img/${circuit}.png" class="img-fluid" alt="Responsive image">
        </div>`;

    formTemplate+=divCircuitImages
    
    var divCircuitFieldsTag = document.createElement("div");
    divCircuitFieldsTag.innerHTML = formTemplate;
    document.getElementById("circuitFields").appendChild(divCircuitFieldsTag);
}

var formTemplate = 
    `<form id="circuitFieldsForm">
        <div class="form-group row">
            <label for="peakVoltage" class="col-sm-2 col-form-label">Peak Voltage (Vp)</label>
            <div class="col-sm-10">
            <input type="text" oninput="validatePeakVoltageField()" class="form-control" id="peakVoltage" placeholder="Peak Voltage (Vp)">
            </div>
        </div>
        <div class="form-group row">
            <label for="frequency" class="col-sm-2 col-form-label">Frequency (f)</label>
            <div class="col-sm-10">
            <input type="text" oninput="validateFrequencyField()" class="form-control" id="frequency" placeholder="Frequency (Hz)">
            </div>
        </div>
        <div class="form-group row">
            <label for="resistor" class="col-sm-2 col-form-label">Resistor (R)</label>
            <div class="col-sm-10">
            <input type="text" oninput="validateResistorField()" class="form-control" id="resistor" placeholder="Resistor (Ohm)">
            </div>
        </div>
        <div class="form-group row">
            <label for="initialTime" class="col-sm-2 col-form-label">Initial Time (s)</label>
            <div class="col-sm-10">
            <input type="text" oninput="validateInitialTimeField()" class="form-control" id="initialTime" placeholder="Initial Time (s)">
            </div>
        </div>
        <div class="form-group row">
            <label for="finalTime" class="col-sm-2 col-form-label">Final Time (s)</label>
            <div class="col-sm-10">
            <input type="text" oninput="validateFinalTimeField()" class="form-control" id="finalTime" placeholder="Final Time (s)">
            </div>
        </div>
    </form>`