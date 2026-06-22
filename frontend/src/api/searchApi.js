import api from "./axios";

export const searchItems = async (
  query
) => {

  const token =
    localStorage.getItem("access");

  const response =
    await api.get(
      `/search/?q=${query}`,
      {
        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }
    );

  return response.data;
};