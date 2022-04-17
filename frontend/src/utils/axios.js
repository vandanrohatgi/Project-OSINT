import axios from "axios/index";
import { BASE_URL } from "../config";

const axiosInstance = axios.create({});

export const get = (path, params = {}) =>
  axiosInstance.get(BASE_URL + path, params, {
    params,
  });

export const post = (path, params = {}) =>
  axiosInstance.post(BASE_URL + path, params);

export const put = (path, params = {}) =>
  axiosInstance.put(BASE_URL + path, params);