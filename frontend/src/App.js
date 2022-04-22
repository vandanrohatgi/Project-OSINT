// import Header from "./components/Header/Header";

// function App() {
//   return (
//     <div>
//       <Header />
//     </div>
//   );
// }

// export default App;


import "./App.css";
import Header from "./components/Header/Header";
import SideBar from "./components/SideBar/SideBar";

function App() {
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

export default App;
