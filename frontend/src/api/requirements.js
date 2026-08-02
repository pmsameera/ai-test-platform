import client from "./client";

export const getRequirements = async () => {
  const response = await client.get("/requirements/");
  console.log("Requirements API:", response.data);
  return response.data;
};

export const createRequirement = async (data) => {
  const response = await client.post("/requirements/", data);
  return response.data;
};

export const deleteRequirement = async (id) => {
  await client.delete(`/requirements/${id}`);
};