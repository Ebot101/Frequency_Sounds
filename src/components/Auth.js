import React, {useState, useEffect} from "react";
import axios from "axios";

const Auth = () => {
    const [auth, setAuth] = useState(null);

    useEffect(() => {
        axios.get("http://localhost:5000/authenticate").then((response) => {
            setAuth(response.data.url);
        });
    }, []);

    return (
        <div>
              <button><a href={auth}>Authenticate</a></button>
        </div>
    );
}

export default Auth;

