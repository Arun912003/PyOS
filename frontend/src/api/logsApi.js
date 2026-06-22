import api from "./axios";

export const getLogs = async () => {

  const token =
    localStorage.getItem("access");

  const response =
    await api.get(
      "/logs/",
      {
        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }
    );

  return response.data;
};