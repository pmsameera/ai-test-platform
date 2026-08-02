import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";


import Requirements from "./pages/Requirements";
import TestCases from "./pages/TestCases";



export default function App() {


  return (

    <BrowserRouter>

      <Routes>


        <Route
          path="/"
          element={<Requirements />}
        />


        <Route
          path="/requirements/:requirementId/testcases"
          element={<TestCases />}
        />


      </Routes>

    </BrowserRouter>

  );

}