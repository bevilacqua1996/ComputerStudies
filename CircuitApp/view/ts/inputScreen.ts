function createBodyTemplate() {
    var url = new URL(window.location.href);
    var circuit = url.searchParams.get("circuit");

    buildTitle(circuit)
    buildCircuitFields(circuit)
}

function goToMainPage() {
    window.location.assign('../index.html');
}

function sendToServer() {
    // TODO: send POST request to server
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
            <input type="number" class="form-control" id="capacitor" placeholder="Capacitor (Faraday)">
            </div>
        </div>`
    } else {
        circuitTypeTemplate=
        `<div class="form-group row">
            <label for="inductor" class="col-sm-2 col-form-label">Inductor (L)</label>
            <div class="col-sm-10">
            <input type="number" class="form-control" id="inductor" placeholder="Inductor (Henry)">
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
            <input type="number" class="form-control" id="peakVoltage" placeholder="Peak Voltage (Vp)">
            </div>
        </div>
        <div class="form-group row">
            <label for="frequency" class="col-sm-2 col-form-label">Frequency (f)</label>
            <div class="col-sm-10">
            <input type="number" class="form-control" id="frequency" placeholder="Frequency (Hz)">
            </div>
        </div>
        <div class="form-group row">
            <label for="resistor" class="col-sm-2 col-form-label">Resistor (R)</label>
            <div class="col-sm-10">
            <input type="number" class="form-control" id="resistor" placeholder="Resistor (Ohm)">
            </div>
        </div>
    </form>`