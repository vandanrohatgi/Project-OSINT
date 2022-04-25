import React from "react";
import Header from "../../components/Header/Header";
import SideBar from "../../components/SideBar/SideBar";

function Dashboard() {
  return (
    <div className="App">
      <div className="SideBar">
        <SideBar />
      </div>
      <div className="Header">
        <Header />
      </div>
    </div>
  );
}

export default Dashboard;
