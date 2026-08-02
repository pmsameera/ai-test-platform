export default function RequirementList({
  requirements,
  onSelect,
}) {
  return (
    <div>
      <h2>Requirements</h2>

      {requirements.map((req) => (
        <div
          key={req.id}
          onClick={() => onSelect(req)}
          style={{
            cursor: "pointer",
            padding: "10px",
            border: "1px solid #ccc",
            marginBottom: "10px",
          }}
        >
          <h3>{req.title}</h3>
          <p>{req.description}</p>
        </div>
      ))}
    </div>
  );
}