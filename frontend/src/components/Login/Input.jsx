import React from "react";
import { Form } from "react-bootstrap";

function Input(props) {
  const { value, onChange, placeholder, type, label, ...rest } = props;
  return (
    <Form.Group className="mb-3">
      {label && <Form.Label>{label}</Form.Label>}
      <Form.Control
        value={value}
        onChange={onChange}
        type={type}
        placeholder={placeholder}
        {...rest}
      />
    </Form.Group>
  );
}

export default Input;
