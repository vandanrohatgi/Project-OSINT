import React from "react";
import { Button } from "react-bootstrap";

function AppButton(props) {
  const { label = "Click", handleClick, disabled, ...rest } = props;
  return (
    <Button onClick={handleClick} disabled={disabled} {...rest}>
      {label}
    </Button>
  );
}

export default AppButton;
