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

  const handleRecommendation = async () =>{
      try{
        const response = await axios.get(`http://localhost:5000/?name=${movieName}`);
        const data = response.data
        setRecommendations(data.recommendations);
        setStatus(data.status || '');
      } catch(e) {
        console.log('Error fetching recommendations: ', error);
      }
  };

  const fetchMovieDetails = async () => {
    try{
      const apiKey = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhY2Q0MDgwZDhlOTFkM2E2OGExODNmYzg3MTQ0OGQ2ZCIsInN1YiI6IjY1OWI2NThiMjE2MjFkMDA5NWI0MTM5NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.RADnMKFrNUcs7p8NGS0HO4MbsVKQc_1BnQqZ7QZ_rYQ';
      const tmdbResponse = await axios.get(
        `https://api.themoviedb.org/3/search/movie?api_key=${apiKey}&query=${movieTitle}`
      )
    } catch (e) {
      console.log('Error fetching movie details: ', error);
    }
  }

  return (
    <div>
      <h1>Movie Recommendation System</h1>
    </div>
  );
}

export default App;
