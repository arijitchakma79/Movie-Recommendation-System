import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [movieName, setMovieName] = useState('');
  const [recommendations, setRecommendations] = useState([]);
  const [status, setStatus] = useState('')
  const [movieDetails, setMovieDetails] = useState({});

  const handleInputChange = (e) => {
    setMovieName(e.target.value);
  }

const handleRecommendation = async () => {
  try {
    const response = await axios.get(`http://localhost:5000/?name=${movieName}`);
    const data = response.data;
    setRecommendations(data.movies);
    setStatus(data.status || '');
  } catch(e) {
    console.log('Error fetching recommendations: ', e);
  }
}
  return (
    <div>
      <h1>Movie Recommendation System</h1>
      <input 
        type="text"
        placeholder="Enter movie name"
        onChange={handleInputChange}
      />
      <button onClick={handleRecommendation}>Get Recommendations</button>
      {status === 'error' && <p>Error fetching recommendations. Please try again.</p>}
      {recommendations.length > 0 && (
        <div>
          <h2>Top 5 Recommendations:</h2>
          <ul>
            {recommendations.map((movie, index) => (
              <li key={index}>{movie}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
