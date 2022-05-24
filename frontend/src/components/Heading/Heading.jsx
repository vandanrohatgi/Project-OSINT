import React from "react";

function Heading(props) {
  const { element = "h4", title, ...rest } = props;
  return React.createElement(element, rest, [<strong>{title}</strong>]);
}

export default Heading;
