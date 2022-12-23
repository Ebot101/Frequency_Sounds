import React, {useState, useEffect} from "react";
import axios from "axios";

const RecentPlay = () => {
    const [recentPlay, setRecentPlay] = useState(null);

    // make a function that will get the recent play when the button is clicked
    const getRecentPlay = () => {
        axios.get("http://localhost:5000/recently-played").then((response) => {
            setRecentPlay(response.data.items);
        }).catch((error) => {
            console.log(error);
        });
    }

    return (
        <div>
            <button onClick={getRecentPlay}>Get Recent Play</button>
            {/* map the items in recentPlay */}
            {recentPlay && recentPlay.map((item) => {
                return (
                    <div>
                        <img src={item.track.album.images[0].url} alt="album cover" />
                        <p>{item.track.name}</p>
                        <p>{item.track.artists[0].name}</p>
                        
                    </div>
                );
            })}
        </div>
    );
}

export default RecentPlay;