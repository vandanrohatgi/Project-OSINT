import React, { useState } from "react";
import ParticleBackground from "../../components/Login/ParticleBackground";
import { Form, Button } from "react-bootstrap";
import styles from "./login.module.css";
import { MdOutlineSecurity } from "react-icons/md";
import AppInput from "../../components/AppInput/AppInput";
import { post } from "../../utils/axios";
import { useNavigate } from "react-router-dom";

function Login() {
  const navigate = useNavigate();

  const [credentials, setCredentials] = useState({
    username: "",
    password: "",
  });

  const [isSubmitting, setIsSubmitting] = useState(false);

  function handleChange(e) {
    setCredentials((creds) => ({ ...creds, [e.target.name]: e.target.value }));
  }
  async function handleSubmit(e) {
    e.preventDefault();
    setIsSubmitting(true);

    await post("/login", credentials)
      .then(({ data }) => {
        sessionStorage.setItem("accessToken", data.access_token);
        navigate(0);
      })
      .catch((err) => {
        console.log(err);
        alert(err.message);
      })
      .finally(() => {
        setIsSubmitting(false);
      });
  }
  return (
    <div className={styles.wrapper}>
      <div className={styles.title}>Project OSINT</div>
      <div className={styles.LoginFormContainer}>
        <div className={styles.AuthIcon}>
          <MdOutlineSecurity />
        </div>
        <Form onSubmit={handleSubmit}>
          <AppInput
            value={credentials.username}
            onChange={handleChange}
            placeholder={"Enter Username"}
            name="username"
            required
          />
          <AppInput
            value={credentials.password}
            onChange={handleChange}
            placeholder={"Enter Password"}
            name="password"
            type="password"
            required
          />

          <Button
            variant="success"
            type="submit"
            className="d-block mx-auto px-3"
            disabled={isSubmitting}
          >
            {isSubmitting ? "Submitting..." : "Submit"}
          </Button>
        </Form>
      </div>
      <ParticleBackground />
    </div>
  );
}

export default Login;
