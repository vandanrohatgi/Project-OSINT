import React, { useState } from "react";
import { useEffect } from "react";
import { BsGlobe, BsBoxArrowUpRight } from "react-icons/bs";
import { get } from "../../utils/axios";
import styles from "./scan.module.css";
import { Row, Col } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import Heading from "../../components/Heading/Heading";

function Scans() {
  const [previousScans, setPreviousScans] = useState();
  useEffect(() => {
    get("/getScanInfo")
      .then((result) => {
        console.log(result);
        const modifiedResult = Object.entries(result.data).reduce(
          (agg, index) => {
            agg.push({ ...index[1], id: index[0] });
            return agg;
          },
          []
        );
        // console.log({ modifiedResult });
        setPreviousScans(modifiedResult.reverse());
      })
      .catch(alert);
  }, []);
  return (
    <div>
      <Heading title="Previous Scans" className="text-success" />
      {previousScans ? (
        previousScans.map((scan) => <ListItem {...scan} />)
      ) : (
        <div className="text-center text-secondary ">Fetching...</div>
      )}
    </div>
  );
}

function ListItem(props) {
  const navigate = useNavigate();
  const { id, name, target, modules, date } = props;
  return (
    <Row className={styles.listItem} onClick={() => navigate(id)}>
      <Col sm="10">
        <Row>
          <Col>
            <div>
              <strong>{name.toString().toUpperCase()}</strong>
            </div>
            <div>{new Date(date).toString()?.slice(0, 16)}</div>
          </Col>
          <Col className="text-end">
            <div>
              <BsGlobe /> {target}
            </div>
            <div>{modules.length} module/s</div>
          </Col>
        </Row>
      </Col>
      <Col sm="2" className={styles.link}>
        <BsBoxArrowUpRight />
      </Col>
    </Row>
  );
}
export default Scans;
