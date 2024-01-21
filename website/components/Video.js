import { useEffect, useState } from "react";

import ReactPlayer from "react-player/youtube";

export default function HowToUse() {
  const [hasWindow, setWindow] = useState(false);
  const [video, setVideo] = useState("");
  useEffect(() => {
    if (typeof window !== "undefined") setWindow(true);

  }, []);
  return hasWindow ? (
    <ReactPlayer playing
      url={`https://youtu.be/FRCo-tXEguM`}
      width={720}
      style={{
        marginRight: "auto",
        marginLeft: "auto",
        justifyContent: "center",
      }}
    />
  ) : (
    <h1>"Loading..."</h1>
  );
}
