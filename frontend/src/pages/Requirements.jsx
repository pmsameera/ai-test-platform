import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import { getRequirements } from "../api/requirements";
import RequirementList from "../components/RequirementList";


export default function Requirements() {

  const [requirements, setRequirements] = useState([]);

  const navigate = useNavigate();


  useEffect(() => {

    const loadRequirements = async () => {

      const data = await getRequirements();

      setRequirements(data);

    };


    loadRequirements();

  }, []);


  const handleSelect = (requirement) => {

    navigate(
      `/requirements/${requirement.id}/testcases`
    );

  };


  return (
    <div>

      <h1>
        AI Test Platform
      </h1>


      <RequirementList
        requirements={requirements}
        onSelect={handleSelect}
      />

    </div>
  );

}