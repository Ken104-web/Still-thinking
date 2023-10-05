import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function Home(){
const [sites, setSites] = useState([]);
const [selectedSite, setSelectedSite] = useState(null);

useEffect(() => {
    fetch('api/sites')
    .then((r) => r.json())
    .then(data => setSites(data));
}, [])

const handleSiteChange = (e) => {
    const selectedSiteId = e.target.value;
    setSelectedSite(selectedSiteId)
};

return (
        <div>
            <span>
                <label htmlFor="siteDropdown">Select a Site</label>
                <select
                    id="siteDropdown"
                     onChange={handleSiteChange}
                     value={selectedSite || ""}>
                         <option value="">Select a Site</option>
          {sites.map((site) => (
            <option key={site.id} value={site.id}>
              {site.location}
              <Link to={`specificsite/${site.id}`}>{site.location}</Link>
            </option>
          ))}
            </select>
            </span>
            <ul>
                <h1>Popular sites</h1>
            {sites.map((site) => (
          <li key={site.id}>
            <Link to={`specificsite/${site.id}`}>{site.location}</Link>
          </li>
            ))}
            </ul>
        </div>
    )
}
export default Home;