import "./App.css";
import MapComponent from "./MapComponent";
import BarGraphContainer from "./BarGraphContainer.jsx";

function App() {
  return (
    <div className="app">
    <div className="map-section">
      <MapComponent/>
    </div>
    <div className="graph-section">
      <BarGraphContainer/>
    </div>
  </div>
  );
}

export default App;
