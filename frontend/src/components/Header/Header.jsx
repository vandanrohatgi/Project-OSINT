import React from "react";
import { useEffect } from "react";
import { get } from "../../utils/axios";

function Header() {
  useEffect(() => {
    get("/")
      .then((data) => {
        console.log(data);
        alert(JSON.stringify(data));
      })
      .catch((err) => {
        console.log(err);
        alert(err.message);
      });
  }, []);
  return <h1 className="text-dark text-center">React With Bootstrap</h1>;
}

export default Header;
