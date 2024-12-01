import React, { useState } from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import CustomEventListener from "./customEventListener";

var graphData = [
  {
    data: [
      { name: "Jan", value: 0 },
      { name: "Feb", value: 0 },
      { name: "Mar", value: 0 },
      { name: "Apr", value: 0 },
      { name: "May", value: 0 },
      { name: "Jun", value: 0 },
      { name: "Jul", value: 0 },
      { name: "Aug", value: 0 },
      { name: "Sep", value: 0 },
      { name: "Oct", value: 0 },
      { name: "Nov", value: 0 },
      { name: "Dec", value: 0 },
    ],
    label: "Wind Speed ",
  },
  {
    data: [
      { name: "Jan", value: 0 },
      { name: "Feb", value: 0 },
      { name: "Mar", value: 0 },
      { name: "Apr", value: 0 },
      { name: "May", value: 0 },
      { name: "Jun", value: 0 },
      { name: "Jul", value: 0 },
      { name: "Aug", value: 0 },
      { name: "Sep", value: 0 },
      { name: "Oct", value: 0 },
      { name: "Nov", value: 0 },
      { name: "Dec", value: 0 },
    ],
    label: "Sunshine (kWh/m^2/day)",
  },
];

const BarGraphContainer = () => {
  const [currentGraph, setCurrentGraph] = useState(0);

  const handleNextGraph = () => {
    setCurrentGraph((prev) => (prev + 1) % graphData.length);
  };

  return (
    <div className="bar-graph-container">
      <CustomEventListener />
      <ResponsiveContainer
        width="100%"
        height="50%">
        <BarChart data={graphData[currentGraph].data}>
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar
            dataKey="value"
            fill="#82ca9d"
          />
        </BarChart>
      </ResponsiveContainer>
      <button
        className="next-button"
        onClick={handleNextGraph}>
        ➡️
      </button>
      <h3>{graphData[currentGraph].label}</h3>
    </div>
  );
};

function myGlobalFunction() {
  graphData = [
    {
      data: [
        { name: "Jan", value: 8.23 },
        { name: "Feb", value: 9.47 },
        { name: "Mar", value: 8.02 },
        { name: "Apr", value: 7.09 },
        { name: "May", value: 6.12 },
        { name: "Jun", value: 6.2 },
        { name: "Jul", value: 5.7 },
        { name: "Aug", value: 5.24 },
        { name: "Sep", value: 5.81 },
        { name: "Oct", value: 6.69 },
        { name: "Nov", value: 7.88 },
        { name: "Dec", value: 9.35 },
      ],
      label: "Average Wind Speed at 50m Above ground (m/s)",
    },
    {
      data: [
        { name: "Jan", value: 1.6 },
        { name: "Feb", value: 2.71 },
        { name: "Mar", value: 3.31 },
        { name: "Apr", value: 4.66 },
        { name: "May", value: 5.66 },
        { name: "Jun", value: 6.45 },
        { name: "Jul", value: 6.12 },
        { name: "Aug", value: 5.36 },
        { name: "Sep", value: 4.06 },
        { name: "Oct", value: 2.99 },
        { name: "Nov", value: 1.85 },
        { name: "Dec", value: 1.2 },
      ],
      label: "Solar Radiation (kWh/m^2/day)",
    },
  ];
}

//attach global function
window.myGlobalFunction = myGlobalFunction;

export default BarGraphContainer;
