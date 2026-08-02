import { useState } from "react";
import { createTestCase } from "../api/testcases";


export default function TestCaseForm({ requirementId, onCreated }) {

  const [form, setForm] = useState({
    title: "",
    description: "",
    steps: "",
    expected_result: ""
  });


  const handleChange = (e) => {

    setForm({
      ...form,
      [e.target.name]: e.target.value
    });

  };


  const handleSubmit = async (e) => {

    e.preventDefault();


    await createTestCase({
      requirement_id: requirementId,
      ...form
    });


    setForm({
      title: "",
      description: "",
      steps: "",
      expected_result: ""
    });


    onCreated();

  };


  return (
    <form onSubmit={handleSubmit}>

      <h3>
        Add Test Case
      </h3>


      <input
        name="title"
        placeholder="Title"
        value={form.title}
        onChange={handleChange}
      />


      <br />


      <textarea
        name="description"
        placeholder="Description"
        value={form.description}
        onChange={handleChange}
      />


      <br />


      <textarea
        name="steps"
        placeholder="Steps"
        value={form.steps}
        onChange={handleChange}
      />


      <br />


      <textarea
        name="expected_result"
        placeholder="Expected Result"
        value={form.expected_result}
        onChange={handleChange}
      />


      <br />


      <button type="submit">
        Save Test Case
      </button>


    </form>
  );
}