import {
useEffect,
useState
} from "react";


import {
Requirement,
getRequirements
} from "./api/requirements";


import {
TestCase,
getTestCases
} from "./api/testcases";


import RequirementList
from "./components/RequirementList";


import TestCaseList
from "./components/TestCaseList";



function App(){


const [
requirements,
setRequirements
]=useState<Requirement[]>([]);



const [
selectedRequirement,
setSelectedRequirement
]=useState<Requirement|null>(null);



const [
testcases,
setTestcases
]=useState<TestCase[]>([]);



useEffect(()=>{

loadRequirements();

},[]);



async function loadRequirements(){

const data =
await getRequirements();

setRequirements(data);

}



async function selectRequirement(
req:Requirement
){

setSelectedRequirement(req);


const all =
await getTestCases();


const filtered =
all.filter(
tc=>tc.requirement_id===req.id
);


setTestcases(filtered);

}



return (

<div
style={{
display:"flex",
gap:"30px",
padding:"30px"
}}
>


<div>

<RequirementList

requirements={requirements}

onSelect={selectRequirement}

/>

</div>


<div>


{
selectedRequirement &&

<h1>
{selectedRequirement.title}
</h1>

}


<TestCaseList

testcases={testcases}

/>


</div>


</div>

)

}


export default App;