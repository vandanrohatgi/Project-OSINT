import React from "react";
import { useState } from "react";
import { useEffect } from "react";
import { useParams } from "react-router-dom";
import { get } from "../../utils/axios";
import { GrTarget } from "react-icons/gr";
import { GoPrimitiveDot } from "react-icons/go";

function ScanOverview() {
  const [scanData, setScanData] = useState();
  const { id } = useParams();
  function fetchScanInfo() {
    get("/getScanInfo?id=" + id)
      .then((result) => {
        // console.log(result);
        setScanData(result.data[id]);
      })
      .catch(alert);
  }
  useEffect(() => {
    fetchScanInfo();
    const INTERVAL = 10 * 1000; //10 seconds
    const interval = setInterval(fetchScanInfo, INTERVAL);

    return () => {
      console.log("cleaing");
      clearInterval(interval);
    };
  }, []);
  return (
    <div>
      {scanData ? (
        <MetaInfomation data={scanData} />
      ) : (
        <div className="text-center text-secondary">Fetching...</div>
      )}
    </div>
  );
}

function MetaInfomation({ data }) {
  const { name, target, modules, result } = data;
  const isComplete = modules.length == result.length;

  return (
    <div className="p-3">
      <div className="d-flex justify-content-between">
        <h2>{name.toString().toUpperCase()}</h2>
        <div className={!isComplete ? "text-warning" : "text-success"}>
          <strong>
            <GoPrimitiveDot />
            {isComplete ? "Completed" : "Pending"}
          </strong>
        </div>
      </div>
      <div className="d-flex justify-content-between">
        <div>
          <GrTarget /> {target}
        </div>
        <div>{modules?.length || "NA"} modules</div>
      </div>
    </div>
  );
}
export default ScanOverview;
