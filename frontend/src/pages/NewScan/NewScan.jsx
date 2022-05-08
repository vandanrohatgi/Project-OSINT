import React, { useState } from "react";
import AppInput from "../../components/AppInput/AppInput";
import { Row, Col } from "react-bootstrap";
import AppButton from "../../components/AppButton/AppButton";
import Modules from "../../components/NewScan/Modules";

function NewScan() {
  const [fields, setFields] = useState({ scanName: "", targetName: "" });
  const [selectedModules, setSelectedModules] = useState([]);

  function handleChange(e) {
    setFields((field) => ({ ...field, [e.target.name]: e.target.value }));
  }
  function handleSelectModule(module, isSelected) {
    if (isSelected) {
      setSelectedModules((items) => items.filter((mod) => mod !== module));
    } else setSelectedModules((items) => [...items, module]);
  }

  function handleSubmit(e) {
    e.preventDefault();
    if (selectedModules.length == 0) {
      alert("Please Select Atleast One Module");
      return;
    }

    console.log({ fields, selectedModules });
  }
  return (
    <div>
      <h4>
        <strong>Start A New Scan</strong>
      </h4>
      <form className="mt-4" onSubmit={handleSubmit}>
        <Row>
          <Col>
            <AppInput
              name="scanName"
              value={fields.scanName}
              onChange={handleChange}
              placeholder="Name your scan"
              required
            />
          </Col>
          <Col>
            <AppInput
              name="targetName"
              value={fields.targetName}
              onChange={handleChange}
              placeholder="Target IP/Domain Name"
              required
            />
          </Col>
        </Row>
        <Modules
          selectedModules={selectedModules}
          handleSelectModule={handleSelectModule}
        />
        <div className="d-flex justify-content-center mt-3">
          <AppButton label="Scan" className="px-5" type="submit" />
        </div>
      </form>
    </div>
  );
}

export default NewScan;
