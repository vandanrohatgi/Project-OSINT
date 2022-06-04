import React from "react";
import { Row, Col } from "react-bootstrap";
import Header from "../Header/Header";
import SideBar from "../SideBar/SideBar";
import styles from "./layout.module.css";

function Layout({ children }) {
  return (
    <Row className={styles.wrapper}>
      <Col xs={1} className={styles.sidebar}>
        <SideBar />
      </Col>
      <Col  xs={11} className={styles.contentWrapper}>
        <Header />
        <div className={styles.content}>{children}</div>
      </Col>
    </Row>
  );
}

export default Layout;
