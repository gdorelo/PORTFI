import React, { useState, useEffect, createContext } from 'react'
import axios from 'axios';
export const PortfiContext = createContext();

export const PortfiProvider = ({children}) => {
    const [dataFromBackend, setDataFromBackend] = useState([])
    const [dataFiltrada, setDataFiltrada] = useState([]);
    const [loading, setLoading] = useState(false)
    const [loadingChart, setLoadingChart] = useState(false)
    
    const [loadingAnimation, setLoadingAnimation] = useState(false)
    const [listAssets, setListAssets] = useState([])
    const [compositionData, setCompositionData] = useState([])
    
      
    useEffect ( async () =>{
        if (loading) {
        const data = await fetch('/portfolio')
        const portfolio = await data.json()
        //DataForChart(portfolio)
        generateDataTable(portfolio)
        setCompositionData(portfolio)
        setListAssets(portfolio)
        setLoading(false)
    }
    }, [dataFiltrada, loading, compositionData])

    function generateDataTable(data) { 
        const list_assets = []
        let ticker = ""
        let weigth = 0
        let name = ""
        let asset = {}
        for (let i = 0; i < data.length; i++){
            ticker = data[i].ticker;
            weigth = data[i].weigth;
            name = data[i].name;
            asset = {ticker, name, weigth}
            list_assets.push(asset)
        }
        setDataFromBackend(list_assets || [])
    }

    // function DataForChart(data) {
    //     let ticker = ""
    //     let composition = {}
    //     let asset = {}
    //     for (let i = 0; i < data.length; i++){
    //         ticker = data[i].ticker;
    //         composition = data[i].composition;
    //         asset[ticker] = composition;
    //         //list_assets.push(asset)
    //         setListAssets(...listAssets, asset)
    //     };
    //     setCompositionData(listAssets)
    //     console.log("lista de assets", listAssets)
    //     console.log("Composition Data", compositionData)
    // };

    // useEffect(async () => {
    //     if (loadingChart) {
    //         const url = "/composition";
    //         const response = await fetch(url);
    //         const data = await response.json();
    //         let bonds = data['bonds']
    //         let stocks = data['stocks']
    //         let cash = data['cash']
    //         let array = [bonds, cash, stocks]
    //         setchartData({series:array})
    //         console.log(chartData)
    //         setLoadingChart(false)
    //     }
    // },[dataFiltrada, loadingChart])
    
    return (
        <PortfiContext.Provider value={{dataFromBackend, setDataFromBackend, dataFiltrada, setDataFiltrada, setLoading, setLoadingChart, listAssets, setListAssets, compositionData, setCompositionData, loading
        , setLoadingAnimation, loadingAnimation }}>
            {children}
        </PortfiContext.Provider>
        ) 
}