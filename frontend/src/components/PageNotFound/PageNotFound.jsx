import React from "react";
import { Button } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

function PageNotFound() {
  const navigate = useNavigate();
  return (
    <div className="mt-4 text-center">
      <h4 className="my-4">Oops! Page Not Found</h4>
      <Button onClick={() => navigate("/")}>Go to home</Button>
    </div>
  );
}

export default PageNotFound;
