import api from "./axios";

export const getRecycleBin = async () => {

  const token =
    localStorage.getItem("access");

  const response =
    await api.get(
      "/recyclebin/",
      {
        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }
    );

  return response.data;
};

export const restoreFile = async (
  recycleId
) => {

  const token =
    localStorage.getItem("access");

  const response =
    await api.post(
      `/recyclebin/${recycleId}/restore/`,
      {},
      {
        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }
    );

  return response.data;
};

export const emptyRecycleBin =
  async () => {

    const token =
      localStorage.getItem("access");

    const response =
      await api.delete(
        "/recyclebin/empty/",
        {
          headers: {
            Authorization:
              `Bearer ${token}`
          }
        }
      );

    return response.data;
};