import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Home(){
const [sites, setSites] = useState([]);

useEffect(() => {
    fetch('api/sites')
    .then((r) => r.json())
    .then(data => setSites(data));
})

return (
        <div>
            <ul>
            {sites.map((site) => (
          <li key={site.id}>
            <Link to={`api/sites/${site.id}`}>{site.location}</Link>
          </li>
            ))}
            </ul>
        </div>
    )
}
export default Home;