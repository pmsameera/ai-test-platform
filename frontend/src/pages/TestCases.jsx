import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import { getTestCasesByRequirement } from "../api/testcases";
import TestCaseList from "../components/TestCaseList";
import TestCaseForm from "../components/TestCaseForm";


export default function TestCases() {

  const { requirementId } = useParams();

  const [testcases, setTestcases] = useState([]);


  const loadTestCases = async () => {

    const data =
      await getTestCasesByRequirement(requirementId);

    setTestcases(data);

  };


  useEffect(() => {

    if (requirementId) {
      loadTestCases();
    }

  }, [requirementId]);


  return (
    <div>

      <h1>
        Test Cases
      </h1>


      <TestCaseForm
        requirementId={requirementId}
        onCreated={loadTestCases}
      />


      <TestCaseList
        testcases={testcases}
      />

    </div>
  );

}