import api from "./axios";

export const getDiskInfo = async () => {

  const token =
    localStorage.getItem("access");

  const response =
    await api.get(
      "/filesystem/diskinfo/",
      {
        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }
    );

  return response.data;
};