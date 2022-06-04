import React from "react";
import { useEffect, useState } from "react";
import { get } from "../../utils/axios";
import { Polar, Doughnut } from "react-chartjs-2";
import styles from "./ScanOverview.module.css";
import { useParams } from "react-router-dom";
import { GrTarget } from "react-icons/gr";
import { GoPrimitiveDot } from "react-icons/go";
import { Row, Col } from "react-bootstrap";

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
    const INTERVAL = 1000 * 1000; //10 seconds
    const interval = setInterval(fetchScanInfo, INTERVAL);

    return () => {
      console.log("cleaing");
      clearInterval(interval);
    };
  }, []);
  return (
    <div className="p-3">
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
    <>
      <div className={styles.boxShadowInfo}>
        <div className="d-flex justify-content-between">
          <h2>
            <strong>{name.toString().toUpperCase()}</strong>
          </h2>
          <div className={!isComplete ? "text-warning" : "text-success"}>
            <strong>
              <GoPrimitiveDot />
              {isComplete ? "Completed" : "Pending"}
            </strong>
          </div>
        </div>
        <div className="d-flex justify-content-between">
          <div>
            <GrTarget />{" "}
            <a href={"https:" + target} target="_blank" rel="noreferrer">
              {target}
            </a>
          </div>
          <div>{date + " " + time}</div>
        </div>
        <div>Total Modules: {modules.length}</div>
      </div>
      <div className="my-4">
        <h5>Scanned Result:</h5>
        <Row>
          {result.map((module) => (
            <Col sm={6}>
              {Object.entries(module).map(([name, res]) => (
                <>
                  {" "}
                  <div className={styles.moduleCard}>
                    <strong>
                      {name} : {JSON.stringify(Object.keys(res).length)}
                    </strong>
                    <div className={styles.moduleResult}>
                      {Object.keys(res).map((item) => (
                        <div className="rounded p-1 m-1 border d-inline-block">
                          {item}
                        </div>
                      ))}
                    </div>
                  </div>
                </>
              ))}
            </Col>
          ))}
        </Row>
      </div>
    </>
  );
}

function Chart({ data }) {
  const doughOptions = {
    // maintainAspectRatio: false,
    // responsive: true,
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
    <div className="mt-5">
      <h5>Analysis</h5>
      {data.result.length !== 0 && (
        <>
          <div key={Math.random()} className={styles.mapContainer}>
            <div className={"d-flex justify-content-center"}>
              <Doughnut
                // width={"30%"}
                height={"70px"}
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
          </div>
        </>
      )}
    </div>
  );
}
export default ScanOverview;
