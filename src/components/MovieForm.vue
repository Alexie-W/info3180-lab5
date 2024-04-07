<template>
    <form id="movieForm" @submit.prevent="saveMovie">
        <div class="form-group mb-3">
            <label for="title" class="form-label">Movie Title</label>
            <input type="text" v-model="movie.title" id="title" name="title" class="form-control" />
        </div>
        <div class="form-group mb-3">
            <label for="description" class="form-label">Description</label>
            <textarea v-model="movie.description" id="description" name="description" class="form-control"></textarea>
        </div>
        <div class="form-group mb-3">
            <label for="poster" class="form-label">Poster</label>
            <input type="file" ref="poster" id="poster" name="poster" class="form-control" />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</template>

<script setup>
import { ref, onMounted} from 'vue';

const movie = ref({ title: '', description: '', poster: null });

const saveMovie = () => {
    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);

    fetch("/api/v1/movies", {
        method: 'POST',
        body: form_data,
        headers: { 
        'X-CSRFToken': csrf_token.value 
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Display a success message
    })
    .catch(error => {
        console.error(error);
    });
};


let csrf_token = ref(""); 

function getCsrfToken() { 

fetch('/api/v1/csrf-token') 
.then((response) => response.json()) 
.then((data) => { 

    console.log(data); 
csrf_token.value = data.csrf_token; 
}) 
} 

onMounted(() => { 
    getCsrfToken(); 
}); 


</script>

