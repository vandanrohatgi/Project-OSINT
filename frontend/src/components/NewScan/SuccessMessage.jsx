import React from "react";
import { useNavigate } from "react-router-dom";
import AppButton from "../AppButton/AppButton";

function SuccessMessage() {
  const navigate = useNavigate();
  return (
    <div className="text-center">
      <h5>Scan Started</h5>
      <img
        src={
          "https://cdn.dribbble.com/users/1751799/screenshots/5512482/media/1cbd3594bb5e8d90924a105d4aae924c.gif"
        }
        alt="tick"
      />
      <AppButton
        label="View"
        handleClick={() => navigate("/scans")}
        variant="outline-info"
        size="sm"
        className="d-block mx-auto position-relative"
        style={{ top: "-80px" }}
      />
    </div>
  );
}

export default SuccessMessage;
