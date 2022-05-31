import { useEffect, useState } from "react";
import { get } from "../../utils/axios";
import {Bar, Polar, Doughnut} from "react-chartjs-2";
import styles from "./ScanOverview.module.css";
import {useParams} from "react-router-dom";

const ScanOverview = () => {

  const [mess, setMess] = useState();
  const {id} = useParams();
  
  const data_token = sessionStorage.getItem("accessToken");

  useEffect(()=>{
    const config = {
      headers:{
        Authorization:`Bearer ${data_token}`
      },
    }
    get(`/getScanInfo?id=${id}`,config)
    .then((result)=>result.data)
    .then((data)=>setMess(data))
    .catch((err)=>console.log(err.message))
  },[data_token, id])


var options = {
    responsive:true,
    scales: {
        xAxes: [{
            gridLines: {
                display:false,
            },
            ticks:{
              fontColor:"rgba(0,0,0)",
              fontSize:"12"
            },
        }],
        yAxes: [{
          gridLines: {
              color: "rgba(0, 0, 0, 0.3)",
            },
            ticks: {
              beginAtZero: true
          }
        }]
    },
    legend:{display:false}
}

const doughOptions = {
  legend: {
    position: "right",
  },
  elements: {
    arc: {
      borderWidth:4
    }
  },
};

  return (
    <div>
    {mess ? (
      <>
        {Object.entries(mess)?.map((data)=>(
            data[1].result.length !== 0 && (
                <>
                  <p className={styles.Map__date}>{data[1].date}</p>
                  <div key={Math.random()} className={styles.mapContainer}>
                    {/* {data[1].result.map((item)=>(
                        <div key={Math.random()}>
                            <p  className={styles.Map__information}>{data[1].target}, {Object.entries(item)[0][0]}, {Object.keys(Object.entries(item)[0][1])?.length}</p>
                            <div>
                                <Bar options={options} data={{labels:[Object.entries(item)[0][0]],datasets:[{label:[Object.entries(item)[0][0]],barThickness:48,backgroundColor:"green",data:[Object.keys(Object.entries(item)[0][1])?.length]}]}} />
                            </div>
                        </div>
                    ))} */}
                    {/* <div>
                      <p>{data[1].name} {data[1].target}</p>
                      <Bar options={options} data={{
                        labels:Object.entries(data[1].result).map((item)=>(Object.entries(item[1])[0][0])),
                        datasets:[{
                          data:Object.entries(data[1].result).map(item=>Object.keys(Object.entries(item[1])[0][1]).length),
                          backgroundColor:["green","orange","pink","black","red","purple","yellow"],
                          barThickness:48,
                        }],
                      }} />
                    </div> */}
                    <div className={styles.map}>
                      <p>{data[1].name} {data[1].target}</p>
                      <Polar data={{
                          labels:Object.entries(data[1].result).map((item)=>(Object.entries(item[1])[0][0])),
                          datasets:[{
                            data:Object.entries(data[1].result).map(item=>Object.keys(Object.entries(item[1])[0][1]).length),
                            backgroundColor:['rgb(255, 99, 132)','rgb(75, 192, 192)','rgb(255, 205, 86)','rgb(201, 203, 207)','rgb(54, 162, 235)',"purple","yellow"],
                            
                          }],
                        }}/>
                    </div>
                    <div className={styles.map}>
                      <p>{data[1].name} {data[1].target}</p>
                      <Doughnut options={doughOptions} data={{
                        labels:Object.entries(data[1].result).map((item)=>(Object.entries(item[1])[0][0])),
                        datasets:[{
                          data:Object.entries(data[1].result).map(item=>Object.keys(Object.entries(item[1])[0][1]).length),
                          backgroundColor:['rgb(255, 99, 132)','rgb(75, 192, 192)','rgb(255, 205, 86)','rgb(201, 203, 207)','rgb(54, 162, 235)',"purple","yellow"],
                          
                        }],
                      }}/>
                    </div>
                    {console.log(Object.entries(data[1].result).map((item)=>(Object.entries(item[1])[0][0])),Object.entries(data[1].result).map(item=>Object.keys(Object.entries(item[1])[0][1]).length))}
                  </div>
                </>
            )
        ))}
      </>
    ):(
      <p>Loading...</p>
    )}
    </div>
  )
}

export default ScanOverview