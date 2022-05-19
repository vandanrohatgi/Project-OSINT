import axios from "axios/index";
import { BASE_URL } from "../config";

const axiosInstance = axios.create({});

function getHeaders() {
  return {
    headers: {
      Authorization: "Bearer " + sessionStorage.getItem("accessToken"),
    },
  };
}

export const get = (path, params = {}) =>
  axiosInstance.get(BASE_URL + path, params, {
    params,
  });

export const post = (path, body = {}) =>
  axiosInstance.post(BASE_URL + path, body, getHeaders());

export const put = (path, params = {}) =>
  axiosInstance.put(BASE_URL + path, params);
