import {
  CDBSidebar,
  CDBSidebarContent,
  CDBSidebarHeader,
  CDBSidebarMenu,
  CDBSidebarMenuItem,
} from "cdbreact";
import { useNavigate } from "react-router-dom";

const Sidebar = () => {
  const navigate = useNavigate();
  function handleNavigation(path) {
    navigate(path);
  }
  function handleLogout() {
    sessionStorage.removeItem("accessToken");
    navigate(0);
  }
  return (
    <div style={{ display: "flex" }}>
      <CDBSidebar textColor="#000000" backgroundColor="#f8f8f8">
        <CDBSidebarHeader
          prefix={<i className="fa fa-bars fa-large"></i>}
          style={{ height: "55px" }}
        >
          Dashboard
        </CDBSidebarHeader>
        <CDBSidebarContent className="sidebar-content">
          <CDBSidebarMenu>
            <CDBSidebarMenuItem
              icon="plus"
              onClick={() => handleNavigation("/new-scan")}
            >
              New Scan
            </CDBSidebarMenuItem>
            <CDBSidebarMenuItem
              icon="history"
              onClick={() => handleNavigation("/scans")}
            >
              History
            </CDBSidebarMenuItem>
            {/* <CDBSidebarMenuItem icon="columns">Overview</CDBSidebarMenuItem> */}
            <CDBSidebarMenuItem icon="user" onClick={handleLogout}>
              LogOut
            </CDBSidebarMenuItem>
          </CDBSidebarMenu>
        </CDBSidebarContent>
      </CDBSidebar>
    </div>
  );
};

export default Sidebar;
