<template>
    <div>
    <h1>Movies</h1>
    <div class="movie-container">
        <div v-for="movie in movies" :key="movie.id" class="movie-card">
            <img :src="getPosterUrl(movie.poster)" alt="Movie Poster" class="poster-image">
        <div class="details">
            <h2>{{ movie.title }}</h2>
            <p>{{ movie.description }}</p>
        </div>
        </div>
    </div>
    </div>
</template>

<script setup> 
import { ref, onMounted } from "vue"; 
let movies = ref([]); 

const fetchMovies = () => {
    fetch("/api/v1/movies")
    .then(response => response.json())
    .then (data => {
        movies.value = data.movies;
    })
    .catch(error => {
        console.error("Error fetching movies:", error);
    });
};

onMounted(fetchMovies);

const getPosterUrl = (filename) => {
return `/api/v1/posters/${filename}`;
};


</script> 