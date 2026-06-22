import api from "./axios";

export const getDirectories = async () => {

  const token =
    localStorage.getItem("access");

  const response =
    await api.get(
      "/filesystem/directories/list/",
      {
        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }
    );

  return response.data;
};

export const getFiles = async () => {

  const token =
    localStorage.getItem("access");

  const response =
    await api.get(
      "/filesystem/files/list/",
      {
        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }
    );

  return response.data;
};

export const getFile = async (
  fileId
) => {

  const token =
    localStorage.getItem("access");

  const response =
    await api.get(
      `/filesystem/files/${fileId}/`,
      {
        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }
    );

  return response.data;
};

export const updateFile = async (
  fileId,
  content
) => {

  const token =
    localStorage.getItem("access");

  const response =
    await api.patch(
      `/filesystem/files/${fileId}/write/`,
      {
        content
      },
      {
        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }
    );

  return response.data;
};

export const getCurrentPath = async () => {

  const token =
    localStorage.getItem("access");

  const response =
    await api.get(
      "/filesystem/pwd/",
      {
        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }
    );

  return response.data;
};

export const changeDirectory = async (
  directory
) => {

  const token =
    localStorage.getItem("access");

  const response =
    await api.post(
      "/filesystem/cd/",
      {
        directory
      },
      {
        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }
    );

  return response.data;
};

export const createDirectory = async (
  name
) => {

  const token =
    localStorage.getItem("access");

  const response =
    await api.post(
      "/filesystem/directories/",
      {
        name
      },
      {
        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }
    );

  return response.data;
};

export const createFile = async (
  name
) => {

  const token =
    localStorage.getItem("access");

  const response =
    await api.post(
      "/filesystem/files/",
      {
        name
      },
      {
        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }
    );

  return response.data;
};

export const deleteFile = async (
  fileId
) => {

  const token =
    localStorage.getItem("access");

  const response =
    await api.delete(
      `/filesystem/files/${fileId}/delete/`,
      {
        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }
    );

  return response.data;
};

export const deleteDirectory = async (
  directoryId
) => {

  const token =
    localStorage.getItem("access");

  const response =
    await api.delete(
      `/filesystem/directories/${directoryId}/`,
      {
        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }
    );

  return response.data;
};

export const renameFile = async (
  fileId,
  name
) => {

  const response =
    await api.patch(
      `/filesystem/files/${fileId}/rename/`,
      {
        name
      }
    );

  return response.data;
};

export const renameDirectory = async (
  directoryId,
  name
) => {

  const response =
    await api.patch(
      `/filesystem/directories/${directoryId}/rename/`,
      {
        name
      }
    );

  return response.data;
};

export const copyFile = async (
  fileId,
  name
) => {

  const token =
    localStorage.getItem("access");

  const response =
    await api.post(
      `/filesystem/files/${fileId}/copy/`,
      {
        name
      },
      {
        headers: {
          Authorization:
            `Bearer ${token}`
        }
      }
    );

  return response.data;
};
