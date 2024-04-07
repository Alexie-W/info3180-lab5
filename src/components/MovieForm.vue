<template>
    <form @submit.prevent="saveMovie">
        <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" v-model="movie.title" name="title" class="form-control" />
        </div>
    </form>
</template>

<script setup>
import {ref} from 'vue';

const movie = ref({title: ''});

const saveMovie = () => {

    fetch("api/v1/movies", {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(movie.value)
    })

    .then(response => response.json())
    .then(data => {
    console.log(data);
    movie.title = '';
    })
    
    .catch(error => {
    console.error(error);
    });
};
</script>