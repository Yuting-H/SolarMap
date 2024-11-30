// src/MapComponent.jsx
import React from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import { GeoJSON } from "react-leaflet";

const MapComponent = () => {
  const position = [51.505, -0.09]; // Latitude and Longitude for the initial position

  const geojsonData = {
    type: "FeatureCollection",
    features: [
      {
        type: "Feature",
        properties: {
          name: "Sample Polygon",
        },
        geometry: {
          type: "Polygon",
          coordinates: [
            [
              [-0.09, 51.505],
              [-0.08, 51.51],
              [-0.08, 51.506],
              [-0.09, 51.506],
              [-0.09, 51.505],
            ],
          ],
        },
      },
    ],
  };

  return (
    <MapContainer
      center={position}
      zoom={13}
      style={{ width: "1000px", height: "400px" }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />

      <GeoJSON data={geojsonData} />
      <Marker position={position}>
        <Popup>
          A pretty CSS3 popup. <br /> Easily customizable.
        </Popup>
      </Marker>
    </MapContainer>
  );
};

export default MapComponent;
