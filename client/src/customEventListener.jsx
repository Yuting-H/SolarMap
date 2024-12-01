import React, { useEffect } from "react";
import eventBus from "./eventBus";

const CustomEventListener = () => {
  const handleCustomEvent = (event) => {
    console.log("Custom event received in CustomEventListener:", event.detail);
  };

  useEffect(() => {
    // Add event listener to the event bus
    eventBus.addEventListener("myCustomEvent", handleCustomEvent);

    // Cleanup on component unmount
    return () => {
      eventBus.removeEventListener("myCustomEvent", handleCustomEvent);
    };
  }, []);

  return <></>;
};

export default CustomEventListener;
