import React from "react";
import Header from "../Header/Header";
import SideBar from "../SideBar/SideBar";
import styles from "./layout.module.css";

function Layout({ children }) {
  return (
    <div className={styles.wrapper}>
      <div className={styles.sidebar}>
        <SideBar />
      </div>
      <div className={styles.contentWrapper}>
        <Header />
        <div className={styles.content}>{children}</div>
      </div>
    </div>
  );
}

export default Layout;
