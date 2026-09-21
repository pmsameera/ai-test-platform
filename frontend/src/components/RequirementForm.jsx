import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { getRequirements } from "../api/requirements";
import RequirementList from "../components/RequirementList";
import RequirementForm from "../components/RequirementForm";

export default function Requirements() {
  const [requirements, setRequirements] = useState([]);
  const navigate = useNavigate();

  const loadRequirements = async () => {
    const data = await getRequirements();
    setRequirements(data);
  };

  useEffect(() => {
    loadRequirements();
  }, []);

  const handleSelect = (requirement) => {
    navigate(`/requirements/${requirement.id}/testcases`);
  };

  return (
    <div className="page">
      <h1 className="page-title">AI Test Platform</h1>

      <RequirementForm onCreated={loadRequirements} />

      <RequirementList
        requirements={requirements}
        onSelect={handleSelect}
      />
    </div>
  );
}