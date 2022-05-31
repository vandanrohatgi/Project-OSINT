import { useState, useEffect } from "react";
import { get } from "../../utils/axios";
import {Link} from "react-router-dom";

const Scans = () => {

  const [mess, setMess] = useState();
  
  const data_token = sessionStorage.getItem("accessToken");

  useEffect(()=>{
    const config = {
      headers:{
        Authorization:`Bearer ${data_token}`
      },
    }
    get("/getScanInfo",config)
    .then((result)=>result.data)
    .then((data)=>setMess(data))
    .catch((err)=>console.log(err.message))
  },[data_token])

  return (
    <>
      {mess ? (
      <>
        {Object.entries(mess)?.map((data)=>(
          data[1].result.length !== 0 && (
            <>
                  <p>{data[1].date} {data[1].target}</p>
                  <Link to={`/scans/${data[0]}`}>Visit</Link>
                </>
            )
        ))}
      </>
    ):(
      <p>Loading...</p>
    )}
    </>
  )
}

export default Scans