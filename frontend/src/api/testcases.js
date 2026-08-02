import client from "./client";

export const getTestCases = async () => {
  const response = await client.get("/testcases/");
  return response.data;
};

export const getTestCasesByRequirement = async (requirementId) => {
  const response = await client.get(
    `/testcases/?requirement_id=${requirementId}`
  );
  return response.data;
};

export const createTestCase = async (data) => {
  const response = await client.post("/testcases/", data);
  return response.data;
};

export const updateTestCase = async (id, data) => {
  const response = await client.patch(
    `/testcases/${id}`,
    data
  );
  return response.data;
};

export const deleteTestCase = async (id) => {
  await client.delete(`/testcases/${id}`);
};