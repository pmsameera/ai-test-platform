import { useState } from "react";
import { createTestCase } from "../api/testcases";
import "./TestCaseForm.css";

export default function TestCaseForm({ requirementId, onCreated }) {
  const [form, setForm] = useState({
    title: "",
    description: "",
    steps: "",
    expected_result: "",
  });

  const [error, setError] = useState("");
  const [saving, setSaving] = useState(false);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    const fields = Object.values(form);

    if (fields.some((value) => !value.trim())) {
      setError("All fields are required.");
      return;
    }

    try {
      setSaving(true);

      await createTestCase({
        requirement_id: Number(requirementId),
        ...form,
      });

      setForm({
        title: "",
        description: "",
        steps: "",
        expected_result: "",
      });

      if (onCreated) {
        await onCreated();
      }
    } catch (err) {
      console.error(err);
      setError("Unable to create test case.");
    } finally {
      setSaving(false);
    }
  };

  return (
    <div className="test-case-form">
      <h2>Add Test Case</h2>

      <form onSubmit={handleSubmit}>
        <label>
          Test Case Title <span>*</span>
        </label>

        <input
          name="title"
          value={form.title}
          onChange={handleChange}
          placeholder="Enter test case title"
        />

        <label>
          Description <span>*</span>
        </label>

        <textarea
          name="description"
          value={form.description}
          onChange={handleChange}
          placeholder="Describe the test case"
          rows="3"
        />

        <label>
          Steps <span>*</span>
        </label>

        <textarea
          name="steps"
          value={form.steps}
          onChange={handleChange}
          placeholder="1. Open login page&#10;2. Enter username&#10;3. Click Login"
          rows="5"
        />

        <label>
          Expected Result <span>*</span>
        </label>

        <textarea
          name="expected_result"
          value={form.expected_result}
          onChange={handleChange}
          placeholder="Describe the expected result"
          rows="3"
        />

        {error && <p className="form-error">{error}</p>}

        <button type="submit" disabled={saving}>
          {saving ? "Saving..." : "Save Test Case"}
        </button>
      </form>
    </div>
  );
}