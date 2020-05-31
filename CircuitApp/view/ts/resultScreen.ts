function goToInputScreenPage() {
    window.location.assign('../html/inputScreen.html?circuit=' + getCircuitType());
}

function getCircuitType() {
    var url = new URL(window.location.href);
    var circuit = url.searchParams.get("circuit");
    return circuit;
}

function buildResults(){
    buildResultTitle(getCircuitType())

    document.getElementById("graphResult").innerHTML = "";

    var divGraphResult = 
        `<img src="../../circuitSimulations/circuitResults/${getCircuitType()}circuit.png" id="resultImage" class="img-fluid" onError="failLoadImage()" alt="Responsive image">`;
    
    var divGraphResultTag = document.createElement("div");
    divGraphResultTag.innerHTML = divGraphResult;
    document.getElementById("graphResult").appendChild(divGraphResultTag);

}

function buildResultTitle(circuit) {
    var divCircuitTitle = 
        `<div class="text-center">
            <h1>
                Circuit ${circuit} Results
            </h1>
        </div>`;
    
    var divCircuitTitleTag = document.createElement("div");
    divCircuitTitleTag.innerHTML = divCircuitTitle;
    document.getElementById("title").appendChild(divCircuitTitleTag);
}

function failLoadImage() {
    document.getElementById("feedBackMessages").innerHTML=""
    document.getElementById("reloadButton").innerHTML=""
    document.getElementById("title").innerHTML=""
    document.getElementById("graphResult").innerHTML=""

    var divCircuitLoader = 
                    `<div class="alert alert-danger">
                        <strong>Error!</strong> Something goes wrong and server could not retrieve information in time.
                    </div>
                    <br></br>`;
    
    var divCircuitLoaderTag = document.createElement("div");
    divCircuitLoaderTag.innerHTML = divCircuitLoader;
    document.getElementById("feedBackMessages").appendChild(divCircuitLoaderTag);

    var divReloadButton = 
                    `<div id="reloadButtonAction" class="container">
                        <button type="button" class="btn btn-primary btn-lg btn-block" onclick="reloadPage()">Reload Page</button>
                    </div>
                    <br></br>`;
    
    var divReloadButtonTag = document.createElement("div");
    divReloadButtonTag.innerHTML = divReloadButton;
    document.getElementById("reloadButton").appendChild(divReloadButtonTag);
}

function reloadPage(){
    location.reload();
}