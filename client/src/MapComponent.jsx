import React, { useEffect, useState } from "react";
import mapboxgl from "mapbox-gl";
import "mapbox-gl/dist/mapbox-gl.css";
import axios from "axios";
import eventBus from "./eventBus";

// Set your Mapbox access token here
mapboxgl.accessToken =
  "pk.eyJ1IjoiamhhNTgiLCJhIjoiY200NGw3azJxMDA1dTJqcHpvczVhanRmOSJ9.efEjDtitrtESy5oLFc5J8w"; // Replace with your actual token

const MapComponent = () => {
  const [map, setMap] = useState(null); // State to hold the map instance
  const [containerReady, setContainerReady] = useState(false); // State to track if the container is ready
  const [markers, setMarkers] = useState([]); // State to store active markers

  // Wait for the container to be rendered
  useEffect(() => {
    // Mark the container as ready after the component mounts
    setContainerReady(true);
  }, []);

  useEffect(() => {
    if (containerReady) {
      const mapContainer = document.getElementById("map");
      if (mapContainer) {
        const mapInstance = new mapboxgl.Map({
          container: "map", // ID of the map container
          style: "mapbox://styles/mapbox/streets-v11",
          center: [-98.5795, 39.8283], // Default center (US center)
          zoom: 3,
        });

        setMap(mapInstance);

        // Cleanup map when the component is unmounted
        return () => mapInstance.remove();
      } else {
        console.error("Map container not found!");
      }
    }
  }, [containerReady]); // Only run this when the container is ready

  // Function to remove all previous markers
  const removeMarkers = () => {
    markers.forEach((marker) => marker.remove());
    setMarkers([]);
  };

  // Function to search location by ZIP code or city name
  const searchLocation = async () => {
    const locationInput = document.getElementById("location").value;
    if (!locationInput) {
      alert("Please enter a ZIP Code or City.");
      return;
    }

    try {
      // Use Mapbox's Geocoding API to get coordinates for the entered location
      const response = await fetch(
        `https://api.mapbox.com/geocoding/v5/mapbox.places/${encodeURIComponent(
          locationInput
        )}.json?access_token=${mapboxgl.accessToken}`
      );
      const data = await response.json();
      if (data.features.length === 0) {
        alert("Location not found!");
        return;
      }

      // Remove previous markers
      removeMarkers();

      // Extract coordinates and place name
      const [longitude, latitude] = data.features[0].geometry.coordinates;
      const placeName = data.features[0].place_name;

      //try api call
      try {
        const response = await axios.post(
          "http://127.0.0.1:5000/api/initialize",
          { lat: latitude, lon: longitude }
        );
        if (response.data) {
          console.log(response);
        } else {
        }
      } catch (error) {
        console.error("error fetching data", error);
      }

      // Update the map
      map.flyTo({
        center: [longitude, latitude],
        zoom: 12,
      });

      window.myGlobalFunction();

      // Add a new marker
      const marker = new mapboxgl.Marker()
        .setLngLat([longitude, latitude])
        .setPopup(new mapboxgl.Popup().setText(placeName))
        .addTo(map);

      // Update state with the new marker
      setMarkers([marker]);
    } catch (error) {
      console.error("Error fetching location:", error);
      alert("An error occurred. Please try again.");
    }
  };

  return (
    <div>
      <div
        id="map"
        style={{
          width: "100%",
          height: "100vh", // Set height to fill the entire viewport
        }}>
        <div id="controls">
          <input
            id="location"
            type="text"
            placeholder="Enter ZIP Code or City"
          />
          <button onClick={searchLocation}>Search</button>
        </div>
      </div>
    </div>
  );
};

export default MapComponent;
