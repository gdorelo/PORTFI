import React, { useState } from "react";
import "./Main.css";
import MouseOverPopover from "../Popover";
import { Donut } from "../donut_graph";
import InputField from "../Datatable/InputField";
import { LineGraph } from "../lineGraph";
import PerformanceTable from "../performanceTable"
import { PortfiContext } from "../context/portfiContext";
import { useContext } from "react";
import PuffLoader from "react-spinners/PuffLoader";
//new Main

const Main = () => {
  const [series, setSeries] = useState();
  const { loadingAnimation } = useContext(PortfiContext)

  return (
    <main >
      { loadingAnimation ?  (<div className="main__container_loading"><PuffLoader color={'#3F51B5'} loading={PuffLoader} size={150} /></div>) : (<div className="main__container">
        {/* <!-- CHARTS STARTS HERE --> */}
        <div className="charts">
          <div className="charts__left">
          <InputField />
          </div>
          <div className="charts__right">
            <div className="charts__right__title">
              <div>
                <h1>Portfolio Composition</h1>
              </div>
              <MouseOverPopover displayText="This chart represents the financial investments that your portfolio has at the moment"/>
            </div>
            <Donut series={series} />
          </div>

          <div className="charts__left">
            <div className="charts__left__title">
              <div>
                <h1>Historic Returns</h1>
              </div>
              <MouseOverPopover displayText="In this chart is displayed the historical performance of your portfolio in comparisson to an autogenerated benchmark portfolio"/>
            </div>
          <LineGraph />
          </div>

          <div className="charts__right">
          <PerformanceTable />
          </div>
        </div>
      </div>)  }

    </main>
  );
};

export default Main;
