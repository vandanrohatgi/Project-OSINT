import React from "react";
import { Row, Col } from "react-bootstrap";
import styles from "./scan.module.css";

const MODULE_LIST = [
  {
    label: "Port Scan",
    description: "Scan the target for open ports",
    name: "portScanModule",
  },
  {
    label: "Sub-Domains",
    description: "Scan the target for sub-domains",
    name: "subDomainModule",
  },
  {
    label: "SSL Information",
    description: "Collect information about the ssl certificate used by target",
    name: "sslModule",
  },
  {
    label: "Public IP",
    description: "Collect public IPs assigned to the target",
    name: "PublicIPsModule",
  },
  {
    label: "Email",
    description: "Collect email addresses associated with the target",
    name: "emailModule",
  },
  {
    label: "All Port Scan",
    description: "Scan all the 65535 ports",
    name: "allPortScanModule",
  },
  {
    label: "Scan Github",
    description:
      "Search Github for secrets. (Enter just the keyword in target to perform keyword scan) ",
    name: "gitHubModule",
  },
];

function Modules({ selectedModules, handleSelectModule }) {
  return (
    <Row className="mt-4">
      <h6>Select modules</h6>
      {MODULE_LIST.map((item) => (
        <Col sm={6} md={4} className="p-3" key={item.name}>
          <Card
            data={item}
            handleClick={handleSelectModule}
            selectedModules={selectedModules}
          />
        </Col>
      ))}
    </Row>
  );
}

function Card({ data, handleClick, selectedModules }) {
  const isSelected = selectedModules.find((item) => item === data.name);
  return (
    <div
      className={styles.cardWrapper + " " + (isSelected ? styles.selected : "")}
      onClick={() => handleClick(data.name, isSelected)}
    >
      <strong>{data.label}</strong>
      <p className="text-text-secondary">{data.description}</p>
    </div>
  );
}
export default Modules;
