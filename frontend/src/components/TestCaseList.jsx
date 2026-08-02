export default function TestCaseList({ testcases }) {
  return (
    <div>
      <h2>Test Cases</h2>

      {testcases.map((tc) => (
        <div
          key={tc.id}
          style={{
            border: "1px solid gray",
            margin: "10px",
            padding: "10px",
          }}
        >
          <h3>{tc.title}</h3>

          <p>{tc.description}</p>

          <strong>Steps</strong>

          <p>{tc.steps}</p>

          <strong>Expected Result</strong>

          <p>{tc.expected_result}</p>
        </div>
      ))}
    </div>
  );
}