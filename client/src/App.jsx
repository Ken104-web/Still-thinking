import {Route, Routes} from "react-router-dom";
import Header from './Header'
import Home from "./Home";

import './App.css'

function App() {

  return (
    <>
      <div>
        <Header />
        <Routes>
          <Route exact path="/" element={<Home />}/>
        </Routes>
       
      </div>
    </>
  )
}

export default App
