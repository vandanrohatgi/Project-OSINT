import React from "react";
import { useState } from "react";
import { useEffect } from "react";
import { useParams } from "react-router-dom";
import { get } from "../../utils/axios";

function ScanOverview() {
  const [scanData, setScanData] = useState();
  const { id } = useParams();
  useEffect(() => {
    get("/getScanInfo?id=" + id)
      .then((result) => {
        console.log(result);
        setScanData(result.data[id]);
      })
      .catch(alert);
  });
  return (
    <div>
      {scanData && (
        <>
          <h2>{scanData.name.toString().toUpperCase()}</h2>
        </>
      )}
    </div>
  );
}

export default ScanOverview;
