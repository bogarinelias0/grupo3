// document.addEventListener("DOMContentLoaded")

async function get_localidades(provincia){
    console.log(provincia);
    const url = `https://apis.datos.gob.ar/georef/api/localidades?provincia=${provincia}&aplanar=true&campos=estandar&max=100`
    let locs = await fetch(url)
    .then(response => response.json());
    return locs;
}

async function get_provincias(){
    let provs = await fetch("https://apis.datos.gob.ar/georef/api/provincias")
    .then(response => response.json())
    return provs;
}

function cargar_provincias(){
    let provincias = get_provincias();
    provincias.then(data => {
        const select_provincia = document.getElementById("provincia");
        for (prov of data.provincias.sort(
                function(a, b) {
                    var textA = a.nombre;
                    var textB = b.nombre;
                    return (textA < textB) ? -1 : (textA > textB) ? 1 : 0;}
                    )) {
            // console.log(prov);
            op = document.createElement("option");
            op.innerText = prov.nombre;
            op.value = prov.id + 1;
            select_provincia.appendChild(op);
        }
    })
}

function cargar_localidades(provincia){
    let localidades = get_localidades(provincia);
    localidades.then(data => {
        const select_localidad = document.getElementById("localidad");
        console.log(data);
        for (loc of data.localidades.sort(
            function(a, b) {
                var textA = a.nombre;
                var textB = b.nombre;
                return (textA < textB) ? -1 : (textA > textB) ? 1 : 0;}
        )) {
            op = document.createElement("option");
            op.innerText = loc.nombre;
            op.value = loc.id + 1;
            select_localidad.appendChild(op);
            // console.log('dfdf');
        }
    })
}

cargar_provincias();
function dinamic(){
    let select_provincia = document.getElementById('provincia');
    elegido = select_provincia.innerText;
    console.log(elegido.selectedOption);
}

let select_provincia = document.getElementById('provincia');
select_provincia.addEventListener("change", dinamic, false);
