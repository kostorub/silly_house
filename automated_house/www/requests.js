async function toogle(obj) {
    const body = {
        "pin": obj.id,
        "isActive": obj.checked ? 1 : 0
    };
    
    let response = await fetch('/relay', {
            method: 'POST',
            body: JSON.stringify(body),
            headers: {
                'Content-type': 'application/json; charset=UTF-8'
            }
        });
    if (!response.ok) {
        console.error("HTTP-Error: " + response.status + " " + response.text);
    }
}


var switches = [];
var checkboxes = document.getElementsByTagName("input");

for (x = 0; x < checkboxes.length; x++){
    id = checkboxes[x].getAttribute("id");
    if(id.startsWith("switch-")){
        switches.push(checkboxes[x]);
    }
}

async function getStatus() {
    switches.forEach(async (sw) => {
        let response = await fetch('/relay?pin=' + sw.id, {
                method: 'GET',
            });
        if (!response.ok) {
            console.error("HTTP-Error: " + response.status + " " + response.text);
        } else {
            data = await response.json();
            data.isActive ? sw.parentElement.MaterialSwitch.on() : sw.parentElement.MaterialSwitch.off();
        }
    });
}

setInterval(getStatus, 5000);

var dht11s = [];
var h2s = document.getElementsByTagName("h2");

for (x = 0; x < h2s.length; x++){
    id = h2s[x].getAttribute("id");
    if(id.startsWith("dht11-")){
        dht11s.push(h2s[x]);
    }
}

async function getDHT11() {
    dht11s.forEach(async (dht11) => {
        let response = await fetch('/dht11?pin=' + dht11.id, {
                method: 'GET',
            });
        if (!response.ok) {
            console.error("HTTP-Error: " + response.status + " " + response.text);
        } else {
            data = await response.json();
            if (data.temperature != -1) {
                dht11.innerHTML = "Температура: " + data.temperature + "°C \nВлажность: " + data.humidity + "%";
            }
        }
    });
}
setInterval(getDHT11, 10000);

async function get_current_frame(obj) {
    let response = await fetch('/camera/current_frame?id=' + obj.id, {
        method: 'GET',
    });
    if (!response.ok) {
        console.error("HTTP-Error: " + response.status + " " + response.text);
    } else {
        var imgs = document.getElementsByTagName("img");
        for (x = 0; x < imgs.length; x++){
            var id = imgs[x].getAttribute("id");
            if (id && id.startsWith(obj.id)) {
                blob = await response.blob();
                imgs[x].src = URL.createObjectURL(blob);
            }
        }
    }
}

function hexToBase64(str) {
    return btoa(String.fromCharCode.apply(null, str.replace(/\r|\n/g, "").replace(/([\da-fA-F]{2}) ?/g, "0x$1 ").replace(/ +$/, "").split(" ")));
}