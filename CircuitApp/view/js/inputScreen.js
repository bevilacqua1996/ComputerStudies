function createBodyTemplate() {
    var url = new URL(window.location.href);
    var circuit = url.searchParams.get("circuit");
    buildTitle(circuit);
    buildCircuitFields(circuit);
}
function buildTitle(circuit) {
    var divCircuitTitle = `<h1>
            Circuit ${circuit}
        </h1>`;
    var divCircuitTitleTag = document.createElement("div");
    divCircuitTitleTag.innerHTML = divCircuitTitle;
    document.getElementById("title").appendChild(divCircuitTitleTag);
}
function buildCircuitFields(circuit) {
    var divCircuitImage = `<img src="../img/${circuit}.png" class="img-fluid" alt="Responsive image">`;
    var divCircuitFieldsTag = document.createElement("div");
    divCircuitFieldsTag.innerHTML = divCircuitImage;
    document.getElementById("circuitFields").appendChild(divCircuitFieldsTag);
}
