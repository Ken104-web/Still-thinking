import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom"


function Site(){
        const [ sites, setSites] = useState([])
        const { id } = useParams();

        useEffect(() => {
            fetch(`api/sites/${id}`)
            .then(resp => resp.json())
            .then(data => setSites(data))
        }, [id]);

        return(
            <div>
                <h2>Popular sites:</h2>
                <ul>
                    {sites.map(site => (<li key={site.id}>{site.location}</li>))}
                </ul>
            </div>
        )
}

export default Site;
