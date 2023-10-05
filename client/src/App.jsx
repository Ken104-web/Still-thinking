import {Route, Routes} from "react-router-dom";
import Header from './Header'
import Home from "./Home";
import ShowReviews from "./Review"
import Site from "./site";

import './App.css'

function App() {

  return (
    <>
      <div>
        <Header />
        <Routes>
          <Route exact path="/" element={<Home />}/>
          <Route exact path="/specificsite/:id" element={<Site/>}/>
          <Route exact path="/specificsite/:id/showreview/:id" element={<ShowReviews/>}/>
        </Routes>
       
      </div>
    </>
  )
}

export default App
