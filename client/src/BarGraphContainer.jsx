import React, { useState } from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from "recharts";

const graphData = [
  {
    data: [
      { name: "Jan", value: 400 },
      { name: "Feb", value: 300 },
      { name: "Mar", value: 500 },
    ],
    label: "Graph 1",
  },
  {
    data: [
      { name: "Apr", value: 700 },
      { name: "May", value: 200 },
      { name: "Jun", value: 400 },
    ],
    label: "Graph 2",
  },
];

const BarGraphContainer = () => {
  const [currentGraph, setCurrentGraph] = useState(0);

  const handleNextGraph = () => {
    setCurrentGraph((prev) => (prev + 1) % graphData.length);
  };

  return (
    <div className="bar-graph-container">
      <ResponsiveContainer width="100%" height="50%">
        <BarChart data={graphData[currentGraph].data}>
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="value" fill="#82ca9d" />
        </BarChart>
      </ResponsiveContainer>
      <button className="next-button" onClick={handleNextGraph}>
        ➡️
      </button>
      <h3>{graphData[currentGraph].label}</h3>
    </div>
  );
};

export default BarGraphContainer;
