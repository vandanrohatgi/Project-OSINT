import {CDBSidebar, CDBSidebarContent, CDBSidebarHeader, CDBSidebarMenu, CDBSidebarMenuItem} from 'cdbreact'; 

const Sidebar=()=>{
    return (
        <div style={{display:'flex',}}>
            <CDBSidebar textColor="#000000" backgroundColor="#f8f8f8">
                <CDBSidebarHeader prefix={<i className="fa fa-bars fa-large"></i>} style={{height:"55px"}}>
                    Dashboard
                </CDBSidebarHeader>
                <CDBSidebarContent className="sidebar-content">
                    <CDBSidebarMenu>
                            <CDBSidebarMenuItem icon="search">
                                New Scan
                            </CDBSidebarMenuItem>
                            <CDBSidebarMenuItem icon="history">
                                History
                            </CDBSidebarMenuItem>
                            <CDBSidebarMenuItem icon="columns">
                                Overview
                            </CDBSidebarMenuItem>
                             <CDBSidebarMenuItem icon="user">
                                LogOut
                            </CDBSidebarMenuItem>
                    </CDBSidebarMenu>
                </CDBSidebarContent>
            </CDBSidebar>
        </div>
    )
}

export default Sidebar;