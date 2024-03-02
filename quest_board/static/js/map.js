/*
The following code was obtained from https://developers.google.com/maps/documentation/javascript/examples/advanced-markers-html and has been modified.
*/

async function initMap() {
    // Request needed libraries.
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
    const center = { lat: 51.562179, lng: -3.47715 };
    const map = new Map(document.getElementById("map"), {
        zoom: 9,
        center,
        mapId: "97b0dc5f1a34eb32",
    });

    for (const location of locations) {
        const AdvancedMarkerElement = new google.maps.marker.AdvancedMarkerElement({
            map,
            content: buildContent(location),
            position: location.position,
            title: location.name,
        });

        AdvancedMarkerElement.addListener("click", () => {
            toggleHighlight(AdvancedMarkerElement, location);
        });
    }
}

function toggleHighlight(markerView, location) {
    if (markerView.content.classList.contains("highlight")) {
        markerView.content.classList.remove("highlight");
        markerView.zIndex = null;
    } else {
        markerView.content.classList.add("highlight");
        markerView.zIndex = 1;
    }
}

function buildContent(location) {
    const content = document.createElement("div");

    content.classList.add("location");
    content.innerHTML = `
    <div class="icon">
        <i aria-hidden="true" class="${location.icon}" title="${location.name}"></i>
        <span class="fa-sr-only">${location.type}</span>
    </div>
    <div class="details">
        <div class="name">${location.name}</div>
        <div class="address">${location.address}</div>
        <div class="phone"><i class="fa-solid fa-phone"></i> ${location.phone}</div>
        <div class="hours"><i class="fa-solid fa-clock"></i> Mon - Sun: 10am - 6pm</div>
    </div>
    `;
    return content;
}

const locations = [
    {
        address: "45, Castle Arcade, Cardiff CF10 1BW",
        name: "Castle Games",
        icon: "fa-brands fa-fort-awesome",
        type: "castle",
        phone: "02921 123 456",
        position: {
            lat: 51.4809315,
            lng: -3.1817093,
        },
    },
    {
        address: "1 Austin Friars, Newport NP20 1DQ",
        name: "Boarderlands",
        icon: "fa-solid fa-chess-board",
        type: "chessboard",
        phone: "01633 123 456",
        position: {
            lat: 51.5867805,
            lng: -2.996156,
        },
    },
    {
        address: "7 The Rhiw, Bridgend CF31 3BL",
        name: "Dungeons & Dice",
        icon: "fa-solid fa-dice",
        type: "dice",
        phone: "01656 123 456",
        position: {
            lat: 51.5053977,
            lng: -3.5864474,
        },
    },
    {
        address: "8 High St, Swansea SA1 1LE",
        name: "Checkmates",
        icon: "fa-solid fa-chess-king",
        type: "king",
        phone: "01792 123 456",
        position: {
            lat: 51.6212663,
            lng: -3.9459948,
        },
    }
];

initMap();