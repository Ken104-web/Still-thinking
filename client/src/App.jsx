import {Route, Routes} from "react-router-dom";
import Header from './Header'
import Home from "./Home";

import './App.css'
import Site from "./site";

function App() {

  return (
    <>
      <div>
        <Header />
        <Routes>
          <Route exact path="/" element={<Home />}/>
          <Route exact path="/specificsite/:id" element={<Site/>}/>
        </Routes>
       
      </div>
    </>
  )
}

export default App
