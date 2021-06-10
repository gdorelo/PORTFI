import React, { useContext, useEffect, useState } from 'react';
import Chart from 'react-apexcharts'
import { PortfiContext } from './context/portfiContext';

export const Donut = () => {
  const { compositionData } = useContext(PortfiContext)
  const [ charData, setChartData] = useState([])
  let [bonds, setBonds] = useState(parseFloat(0.0))
  let [stocks, setStocks] = useState(parseFloat(0.0))
  let [cash, setCash] = useState(parseFloat(0.0))

  useEffect ( () => {
    let rawChartData = []
    let ticker = ""
    let composition = {}
    let asset = {}
    for (let i = 0; i < compositionData.length; i++){
        ticker = compositionData[i].ticker;
        composition = compositionData[i].composition;
        asset[ticker] = composition;
        rawChartData.push(asset[ticker])
        //console.log("raw",rawChartData)
      };
    setChartData(rawChartData)
    //console.log("Chart Data", charData)
    charData.map( (data) => {
      setBonds(bonds += data.bonds);
      setStocks(stocks += data.stocks);
    })
    let cash_ = Math.abs((bonds + stocks) -1 )
    setCash(cash_)
    setEstado({...estado, series:[parseFloat(bonds), parseFloat(cash_), parseFloat(stocks)]})
    //console.log(estado)
  }, [compositionData]);

  
  const [estado, setEstado] = useState(
    {
      options: {
        labels: ['Bonds', 'Cash', 'Stocks']
      },
      series: [bonds ,cash, stocks]
    })
    
    const { options, series } = estado
    
  

  return (
  <Chart 
  options={options}
  series={series? series:series} 
  type="donut" 
  width="380" />
  )
}
