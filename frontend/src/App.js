import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login/Login";
import Dashboard from "./pages/Dashboard/Dashboard";

function App() {
  const isTokenAvaialble = sessionStorage.getItem("accessToken");
  return (
    <BrowserRouter>
      <Routes>
        {!isTokenAvaialble ? (
          <Route path="*" element={<Login />} />
        ) : (
          <>
            <Route path="dashboard" element={<Dashboard />} />
            <Route path="*" element={<Dashboard />} />
          </>
        )}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
