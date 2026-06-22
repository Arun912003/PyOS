import api from "./axios";

export const registerUser = async (
  username,
  email,
  password
) => {

  const response =
    await api.post(
      "/users/register/",
      {
        username,
        email,
        password
      }
    );

  return response.data;
};

export const loginUser = async (
  username,
  password
) => {

  const response = await api.post(
    "/users/login/",
    {
      username,
      password,
    }
  );

  return response.data;
};