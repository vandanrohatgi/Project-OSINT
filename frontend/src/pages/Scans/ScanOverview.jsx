import React from "react";
import { useEffect, useState } from "react";
import { get } from "../../utils/axios";
import { Bar, Polar, Doughnut } from "react-chartjs-2";
import styles from "./ScanOverview.module.css";
import { useParams } from "react-router-dom";
import { GrTarget } from "react-icons/gr";
import { GoPrimitiveDot } from "react-icons/go";

function ScanOverview() {
  const [scanData, setScanData] = useState();
  const { id } = useParams();
  function fetchScanInfo() {
    get("/getScanInfo?id=" + id)
      .then((result) => {
        console.log(result.data);
        setScanData(result.data[id]);
        // setScanData(result.data);
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
        <>
          <MetaInfomation data={scanData} />
          <Chart data={scanData} />
        </>
      ) : (
        <div className="text-center text-secondary">Fetching...</div>
      )}
    </div>
  );
}

function MetaInfomation({ data }) {
  const { name, target, modules, result, date, time } = data;
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
        <div>{date + " " + time}</div>
      </div>
      <div>
        {result.map((module) => (
          <p>
            {Object.entries(module).map(([name, res]) => (
              <>
                {name}
                {JSON.stringify(Object.keys(res).length)}
              </>
            ))}
          </p>
        ))}
      </div>
    </div>
  );
}

function Chart({ data }) {
  const doughOptions = {
    legend: {
      position: "right",
    },
    elements: {
      arc: {
        borderWidth: 4,
      },
    },
  };

  return (
    <>
      {data.result.length !== 0 && (
        <>
          <div key={Math.random()} className={styles.mapContainer}>
            <div className={styles.map}>
              <p>
                {data.name} {data.target}
              </p>
              <Polar
                data={{
                  labels: Object.entries(data.result).map(
                    (item) => Object.entries(item[1])[0][0]
                  ),
                  datasets: [
                    {
                      data: Object.entries(data.result).map(
                        (item) =>
                          Object.keys(Object.entries(item[1])[0][1]).length
                      ),
                      backgroundColor: [
                        "rgb(255, 99, 132)",
                        "rgb(75, 192, 192)",
                        "rgb(255, 205, 86)",
                        "rgb(201, 203, 207)",
                        "rgb(54, 162, 235)",
                        "purple",
                        "yellow",
                      ],
                    },
                  ],
                }}
              />
            </div>
            <div className={styles.map}>
              <p>
                {data.name} {data.target}
              </p>
              <Doughnut
                options={doughOptions}
                data={{
                  labels: Object.entries(data.result).map(
                    (item) => Object.entries(item[1])[0][0]
                  ),
                  datasets: [
                    {
                      data: Object.entries(data.result).map(
                        (item) =>
                          Object.keys(Object.entries(item[1])[0][1]).length
                      ),
                      backgroundColor: [
                        "rgb(255, 99, 132)",
                        "rgb(75, 192, 192)",
                        "rgb(255, 205, 86)",
                        "rgb(201, 203, 207)",
                        "rgb(54, 162, 235)",
                        "purple",
                        "yellow",
                      ],
                    },
                  ],
                }}
              />
            </div>
            {console.log(
              Object.entries(data.result).map(
                (item) => Object.entries(item[1])[0][0]
              ),
              Object.entries(data.result).map(
                (item) => Object.keys(Object.entries(item[1])[0][1]).length
              )
            )}
          </div>
        </>
      )}
    </>
  );
}
export default ScanOverview;
