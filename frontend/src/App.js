import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./pages/Login/Login";
import NewScan from "./pages/NewScan/NewScan";
import Layout from "./components/Layout/Layout";
import SuccessMessage from "./components/NewScan/SuccessMessage";
import Scans from "./pages/Scans/Scans";
import ScanOverview from "./pages/Scans/ScanOverview";
import PageNotFound from "./components/PageNotFound/PageNotFound";

function App() {
  const isTokenAvailable = sessionStorage.getItem("accessToken");
  function WithLayout(Component) {
    return <Layout>{<Component />}</Layout>;
  }
  return (
    <BrowserRouter>
      <Routes>
        {!isTokenAvailable ? (
          <Route path="*" element={<Login />} />
        ) : (
          <>
            <Route path="" element={WithLayout(NewScan)} />
            <Route path="new-scan" element={WithLayout(NewScan)} />
            <Route
              path="new-scan/success"
              element={WithLayout(SuccessMessage)}
            />
            <Route path="scans" element={WithLayout(Scans)} />
            <Route path="scans/:id" element={WithLayout(ScanOverview)} />
            <Route path="*" element={WithLayout(PageNotFound)} />
          </>
        )}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
