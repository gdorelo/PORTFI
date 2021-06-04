import { useState } from "react";
import React from 'react'
import "./App.css";
import Main from "./components/main/Main";
import Navbar from "./components/navbar/Navbar";
import Sidebar from "./components/sidebar/Sidebar";
import UserSettings from "./components/UserSettings/UserSettings.js"
import PortfolioA from "./components/Portfolios/PortfolioA.js"
import PortfolioB from "./components/Portfolios/PortfolioB.js"
import PortfolioC from "./components/Portfolios/PortfolioC.js"
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import SignUp from "./components/UserSettings/SignUp";
import SignIn from "./components/UserSettings/SignIn";


const App = () => {
  const [sidebarOpen, setsidebarOpen] = useState(false);
  const openSidebar = () => {
    setsidebarOpen(true);
  };
  const closeSidebar = () => {
    setsidebarOpen(false);
  };
  return (
      <div className="container">
        <Navbar sidebarOpen={sidebarOpen} openSidebar={openSidebar} />
        <Sidebar sidebarOpen={sidebarOpen} closeSidebar={closeSidebar} />
          <Switch>
            <Route path="/" exact component={Main} />
            <Route path="/portfolioa" component={PortfolioA} />
            <Route path="/portfoliob" component={PortfolioB} />
            <Route path="/portfolioc" component={PortfolioC} />
            <Route path="/usersettings" component={UserSettings} />
            <Route path="/signup" component={SignUp} />
            <Route path="/signin" component={SignIn} />
          </Switch>
      </div>
  );
};

export default App;
