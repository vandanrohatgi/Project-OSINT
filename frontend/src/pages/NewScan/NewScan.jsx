import React, { useState } from "react";
import AppInput from "../../components/AppInput/AppInput";
import { Row, Col } from "react-bootstrap";
import AppButton from "../../components/AppButton/AppButton";
import Modules from "../../components/NewScan/Modules";
import { post } from "../../utils/axios";
import { useNavigate } from "react-router-dom";
import Heading from "../../components/Heading/Heading";

function NewScan() {
  const [fields, setFields] = useState({ name: "", target: "" });
  const [selectedModules, setSelectedModules] = useState([]);
  const navigate = useNavigate();
  function handleChange(e) {
    setFields((field) => ({ ...field, [e.target.name]: e.target.value }));
  }
  function handleSelectModule(module, isSelected) {
    if (isSelected) {
      setSelectedModules((items) => items.filter((mod) => mod !== module));
    } else setSelectedModules((items) => [...items, module]);
  }

  async function handleSubmit(e) {
    e.preventDefault();
    if (selectedModules.length === 0) {
      alert("Please Select Atleast One Module");
      return;
    }

    console.log({ fields, selectedModules });
    await post("/start", { ...fields, modules: selectedModules })
      .then((result) => {
        console.log(result);
        navigate("/new-scan/success");
      })
      .catch((err) => {
        alert(err.message);
      });
  }
  return (
    <div>
      <Heading title="Start A New Scan" className="text-primary" />
      <form className="mt-4" onSubmit={handleSubmit}>
        <Row>
          <Col>
            <AppInput
              name="name"
              value={fields.name}
              onChange={handleChange}
              placeholder="Name your scan"
              required
            />
          </Col>
          <Col>
            <AppInput
              name="target"
              value={fields.target}
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
