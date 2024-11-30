import React, { useState } from "react";
import { MapContainer, TileLayer, Marker, Popup, useMap } from "react-leaflet";

const MapComponent = () => {
  const [latitude, setLatitude] = useState("51.505"); // Default latitude
  const [longitude, setLongitude] = useState("-0.09"); // Default longitude
  const [position, setPosition] = useState([51.505, -0.09]); // Initial map center

  // Function to handle latitude and longitude input
  const handleSubmit = (e) => {
    e.preventDefault();
    // Convert the input values to numbers and update the map center
    const lat = parseFloat(latitude);
    const lon = parseFloat(longitude);
    if (!isNaN(lat) && !isNaN(lon)) {
      setPosition([lat, lon]); // Update map center
    }
  };

  // Custom hook to move the map to the new marker position
  function MoveMapView({ position }) {
    const map = useMap();
    map.setView(position, map.getZoom(), {
      animate: true, // Optional: adds smooth animation to the map view
    });
    return null; // No rendering needed, just a side-effect
  }

  return (
    <div>
      <h1>Jump to a Location</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Latitude:</label>
          <input
            type="number"
            value={latitude}
            onChange={(e) => setLatitude(e.target.value)}
            step="any"
            placeholder="Enter latitude"
          />
        </div>
        <div>
          <label>Longitude:</label>
          <input
            type="number"
            value={longitude}
            onChange={(e) => setLongitude(e.target.value)}
            step="any"
            placeholder="Enter longitude"
          />
        </div>
        <button type="submit">Go</button>
      </form>

      <MapContainer
        center={position}
        zoom={13}
        style={{ width: "100%", height: "400px" }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />

        {/* Move the map view when the position changes */}
        <MoveMapView position={position} />

        <Marker position={position}>
          <Popup>
            Latitude: {position[0]}
            <br />
            Longitude: {position[1]}
          </Popup>
        </Marker>
      </MapContainer>
    </div>
  );
};

export default MapComponent;
